import os

os.environ["NOJIT"] = "false"

import argparse
import asyncio
import pprint
from time import time

import numpy as np
import pandas as pd
from types import SimpleNamespace

from downloader import Downloader
from njit_funcs import njit_backtest, round_
from plotting import dump_plots
from procedures import (
    prepare_backtest_config,
    make_get_filepath,
    load_live_config,
    add_argparse_args,
)
from pure_funcs import create_xk, denumpyize, ts_to_date, analyze_fills, spotify_config


def backtest(config: dict, data: np.ndarray, do_print=False) -> (list, bool):
    xk = create_xk(config)
    return njit_backtest(
        data,
        config["starting_balance"],
        config["latency_simulation_ms"],
        config["maker_fee"],
        **xk,
    )


def plot_wrap(config, data):
    print("n_days", round_(config["n_days"], 0.1))
    print("starting_balance", config["starting_balance"])
    print("backtesting...")
    sts = time()
    fills, stats = backtest(config, data, do_print=True)
    print(f"{time() - sts:.2f} seconds elapsed")
    if not fills:
        print("no fills")
        return
    fdf, sdf, result = analyze_fills(fills, stats, config)
    config["result"] = result
    config["plots_dirpath"] = make_get_filepath(
        os.path.join(config["plots_dirpath"], f"{ts_to_date(time())[:19].replace(':', '')}", "")
    )
    fdf.to_csv(config["plots_dirpath"] + "fills.csv")
    sdf.to_csv(config["plots_dirpath"] + "stats.csv")
    df = pd.DataFrame({**{"timestamp": data[:, 0], "qty": data[:, 1], "price": data[:, 2]}, **{}})
    print("dumping plots...")
    dump_plots(config, fdf, sdf, df)


async def do_backtest(backtest_config_path: str, live_config_path: str, start_date: str, end_date: str, symbol: str,
                      short_wallet_exposure_limit: float = None, long_wallet_exposure_limit: float = None,
                      base_dir: str = 'backtests', enable_shorts: bool = True, enable_longs: bool = True):
    args = SimpleNamespace(**{
        'backtest_config_path': backtest_config_path,
        'live_config_path': live_config_path,
        'start_date': start_date,
        'end_date': end_date,
        'symbol': symbol,
        'market_type': None,
        'nojit': False,
        'short_wallet_exposure_limit': short_wallet_exposure_limit,
        'long_wallet_exposure_limit': long_wallet_exposure_limit,
        'user': 'binance_01',
        'base_dir': base_dir
    })
    config = await prepare_backtest_config(args)
    live_config = load_live_config(args.live_config_path)

    live_config['short']['enabled'] = enable_shorts
    live_config['long']['enabled'] = enable_longs

    config.update(live_config)
    downloader = Downloader(config)
    print()
    for k in (
            keys := [
                "exchange",
                "spot",
                "symbol",
                "market_type",
                "config_type",
                "starting_balance",
                "start_date",
                "end_date",
                "latency_simulation_ms",
            ]
    ):
        if k in config:
            print(f"{k: <{max(map(len, keys)) + 2}} {config[k]}")
    print()
    data = await downloader.get_sampled_ticks()
    config["n_days"] = round_((data[-1][0] - data[0][0]) / (1000 * 60 * 60 * 24), 0.1)
    pprint.pprint(denumpyize(live_config))
    plot_wrap(config, data)


async def main():
    parser = argparse.ArgumentParser(prog="Backtest", description="Backtest given passivbot config.")
    parser.add_argument("live_config_path", type=str, help="path to live config to test")
    parser = add_argparse_args(parser)
    parser.add_argument(
        "-lw",
        "--long_wallet_exposure_limit",
        "--long-wallet-exposure-limit",
        type=float,
        required=False,
        dest="long_wallet_exposure_limit",
        default=None,
        help="specify long wallet exposure limit, overriding value from live config",
    )
    parser.add_argument(
        "-sw",
        "--short_wallet_exposure_limit",
        "--short-wallet-exposure-limit",
        type=float,
        required=False,
        dest="short_wallet_exposure_limit",
        default=None,
        help="specify short wallet exposure limit, overriding value from live config",
    )

    args = parser.parse_args()
    config = await prepare_backtest_config(args)
    live_config = load_live_config(args.live_config_path)
    config.update(live_config)

    if args.long_wallet_exposure_limit is not None:
        print(
            f"overriding long wallet exposure limit ({config['long']['wallet_exposure_limit']}) "
            f"with new value: {args.long_wallet_exposure_limit}"
        )
        config["long"]["wallet_exposure_limit"] = args.long_wallet_exposure_limit
    if args.short_wallet_exposure_limit is not None:
        print(
            f"overriding short wallet exposure limit ({config['short']['wallet_exposure_limit']}) "
            f"with new value: {args.short_wallet_exposure_limit}"
        )
        config["short"]["wallet_exposure_limit"] = args.short_wallet_exposure_limit

    if "spot" in config["market_type"]:
        live_config = spotify_config(live_config)
    downloader = Downloader(config)
    print()
    for k in (
            keys := [
                "exchange",
                "spot",
                "symbol",
                "market_type",
                "config_type",
                "starting_balance",
                "start_date",
                "end_date",
                "latency_simulation_ms",
            ]
    ):
        if k in config:
            print(f"{k: <{max(map(len, keys)) + 2}} {config[k]}")
    print()
    data = await downloader.get_sampled_ticks()
    config["n_days"] = round_((data[-1][0] - data[0][0]) / (1000 * 60 * 60 * 24), 0.1)
    pprint.pprint(denumpyize(live_config))
    plot_wrap(config, data)


if __name__ == "__main__":
    asyncio.run(main())

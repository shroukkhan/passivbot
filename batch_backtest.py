import asyncio
import glob
import os
import re
from datetime import datetime, timedelta

from backtest import do_backtest


def print_progress(total: int, current: int, avg: float = 0.0):
    progress = round((current / total) * 100.00, 2)
    print(f'[{current}]: ############################# {progress}% of {total}')
    if avg > 0.0:
        ms_left = (total - current) * avg
        will_finish_at = datetime.now() + timedelta(milliseconds=ms_left)
        print(f'ETA:{will_finish_at} (avg_ms: {avg}, ms_left: {ms_left})')


async def main():
    start = datetime.now()
    ## find latest config files for each symbols
    dirs = glob.glob('C:\\AgodaGit\\passivbot\\results_harmony_search/*/', recursive=True)

    total = len(dirs)
    i = 1

    allowed_symbols = ["ETHUSDT", "XRPUSDT", "1000SHIBUSDT", "DOGEUSDT", "ADAUSDT",
                       "BNBUSDT", "MATICUSDT", "DOTUSDT", "SANDUSDT", "FTMUSDT",
                       "LTCUSDT", "LINKUSDT", "MANAUSDT", "ETCUSDT", "EOSUSDT",
                       "ATOMUSDT", "FILUSDT", "ICPUSDT", "ALICEUSDT", "LRCUSDT",
                       "BCHUSDT", "SUSHIUSDT", "XTZUSDT", "THETAUSDT", "CRVUSDT",
                       "ALGOUSDT", "CHZUSDT", "TRXUSDT", "VETUSDT", "CHRUSDT",
                       "ONEUSDT", "OMGUSDT", "XLMUSDT", "RUNEUSDT", "ENJUSDT",
                       "CELRUSDT", "SXPUSDT", "1INCHUSDT", "SRMUSDT", "COTIUSDT",
                       "ZECUSDT", "QTUMUSDT", "GRTUSDT", "DENTUSDT", "SFPUSDT",
                       "STORJUSDT", "IOTAUSDT", "HOTUSDT", "NEOUSDT", "COMPUSDT",
                       "LINAUSDT", "KAVAUSDT", "BATUSDT", "WAVESUSDT", "IOSTUSDT",
                       "ALPHAUSDT", "RLCUSDT", "HBARUSDT", "DODOUSDT", "XMRUSDT",
                       "SNXUSDT", "ANKRUSDT", "DASHUSDT", "REEFUSDT", "ZENUSDT",
                       "CVCUSDT", "RENUSDT", "ICXUSDT", "RSRUSDT", "SKLUSDT",
                       "NKNUSDT", "BELUSDT", "ONTUSDT", "OGNUSDT", "BLZUSDT",
                       "MTLUSDT", "CTKUSDT", "RVNUSDT", "LITUSDT", "MKRUSDT",
                       "OCEANUSDT", "ZILUSDT", "UNFIUSDT", "BANDUSDT", "YFIIUSDT",
                       "TOMOUSDT", "TRBUSDT", "KNCUSDT", "STMXUSDT", "ZRXUSDT",
                       "SCUSDT", "AKROUSDT", "XEMUSDT", "FLMUSDT", "BALUSDT",
                       "BTSUSDT", "DGBUSDT", "DEFIUSDT"]

    for dir in dirs:
        files = [f for f in os.listdir(dir) if re.match(r'[0-9]+_best_config_.*', f)]
        symbol = dir.split('\\')[-2]
        symbol = symbol.split('_')[-1]
        if symbol not in allowed_symbols:
            print(f'Skipping {dir}')
            continue
        if len(files) > 0:
            files.sort(reverse=True)
            file = files[0]
            live_config_path = f'{dir}{file}'

            await do_backtest(
                backtest_config_path='C:\\AgodaGit\\passivbot\\configs\\backtest\\default.hjson',
                symbol=symbol,
                live_config_path=live_config_path,
                start_date='2021-08-01',
                end_date='2022-01-20',
            )
            end = datetime.now()
            time_taken = (end - start).total_seconds() * 1000
            avg = time_taken / i  # sum(self.post_process_q) / len(self.post_process_q)
            print_progress(total, i, avg)
            i = i + 1


if __name__ == '__main__':
    asyncio.run(main())
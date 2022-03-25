import asyncio
from datetime import datetime, timedelta

from backtest import do_backtest


def print_progress(total: int, current: int, avg: float = 0.0):
    progress = round((current / total) * 100.00, 2)
    print(f'[{current}]: ############################# {progress}% of {total}')
    if avg > 0.0:
        ms_left = (total - current) * avg
        will_finish_at = datetime.now() + timedelta(milliseconds=ms_left)
        print(f'[Default_config]ETA:{will_finish_at} (avg_ms: {avg}, ms_left: {ms_left})')


async def main():
    start = datetime.now()
    config_file = f'C:\\AgodaGit\\passivbot\\configs\\live\\static_grid_mode_auto_unstuck_enabled.example.json'
    # "EOS","XRP","LINK","ADA","DOT","UNI","SUSHI","AAVE","MATIC","BNB","THETA","AXS","LUNA","SAND","ATOM"
    allowed_symbols = ["EOS",
                       "XRP",
                       "BCH",
                       "LINK",
                       "ADA",
                       "DOT",
                       "DOGE",
                       "MATIC",
                       "BNB",
                       "THETA",
                       "AXS",
                       "LUNA",
                       "SAND",
                       "ATOM",
                       "RUNE",
                       "WAVES", ]
    allowed_symbols = [s + "USDT" for s in allowed_symbols]
    total = len(allowed_symbols)
    i = 1
    for symbol in allowed_symbols:
        live_config_path = config_file
        print(f'using file : {live_config_path}')

        start_date = '2021-08-01'
        end_date = '2022-03-23'

        await do_backtest(
            backtest_config_path='C:\\AgodaGit\\passivbot\\configs\\backtest\\default.hjson',
            symbol=symbol,
            live_config_path=live_config_path,
            short_wallet_exposure_limit=0.1,
            long_wallet_exposure_limit=0.1,
            start_date=start_date,
            end_date=end_date,
            user='bybit_01',
            enable_shorts=True,
            enable_longs=True
        )

        end = datetime.now()
        time_taken = (end - start).total_seconds() * 1000
        avg = time_taken / i  # sum(self.post_process_q) / len(self.post_process_q)
        print_progress(total, i, avg)
        i = i + 1


if __name__ == '__main__':
    asyncio.run(main())

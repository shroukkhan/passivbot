import asyncio
import glob
import shutil
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
    files = glob.glob('C:\\AgodaGit\\passivbot\\cfgs_live\\*', recursive=True)
    files.sort()
    total = len(files)
    i = 1
    start_from = "REN.json"
    should_start = True
    allowed_symbols = ['ALICEUSDT', 'XRPUSDT', 'HOTUSDT']
    for file in files:
        symbol = file.split('\\')[-1]
        # if not should_start:
        #     print(f"Skipping : {symbol}")
        #     path = f"C:\\AgodaGit\\passivbot\\backtests\\binance\\{symbol.replace('.json', 'USDT')}\\caches"
        #     if os.path.isdir(path):
        #         shutil.rmtree(path)
        #     if symbol == start_from:
        #         should_start = True
        #     continue

        symbol = symbol.replace('.json', 'USDT')

        if symbol not in allowed_symbols:
            continue

        live_config_path = file
        print(f'using file : {live_config_path}')

        start_date = '2021-05-01'
        end_date = '2022-03-15'

        await do_backtest(
            backtest_config_path='C:\\AgodaGit\\passivbot\\configs\\backtest\\default.hjson',
            symbol=symbol,
            live_config_path=live_config_path,
            start_date=start_date,
            end_date=end_date,
            user='binance_01',
            enable_shorts=True,
            enable_longs=True
        )

        end = datetime.now()
        time_taken = (end - start).total_seconds() * 1000
        avg = time_taken / i  # sum(self.post_process_q) / len(self.post_process_q)
        print_progress(total, i, avg)
        i = i + 1
        shutil.rmtree(f"C:\\AgodaGit\\passivbot\\backtests\\binance\\{symbol}\\caches")


if __name__ == '__main__':
    asyncio.run(main())

import asyncio
import glob
import os
import re

from backtest import do_backtest


async def main():
    ## find latest config files for each symbols
    dirs = glob.glob('C:\\AgodaGit\\passivbot\\results_harmony_search/*/', recursive=True)
    for dir in dirs:
        files = [f for f in os.listdir(dir) if re.match(r'[0-9]+_result_.*', f)]
        symbol = dir.split('\\')[-2]
        if len(files) > 0:
            files.sort(reverse=True)
            print(files[0])

    await do_backtest(
        backtest_config_path='C:\\AgodaGit\\passivbot\\configs\\backtest\\default.hjson',
        symbol='ADAUSDT',
        live_config_path='C:\\AgodaGit\\passivbot\\results_harmony_search\\2022-01-25T07-27-37_ADAUSDT\\000001_best_config_long_short.json',
        start_date='2022-01-01',
        end_date='2022-01-20',
    )


if __name__ == '__main__':
    asyncio.run(main())

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
    dirs = glob.glob('C:\\AgodaGit\\passivbot\\results_harmony_search_recursive_grid\\*', recursive=True)
    dirs.sort()
    dirs = dirs[-25:]  # take last xxx

    dirs2 = glob.glob('C:\\AgodaGit\\passivbot\\results_harmony_search_static_grid\\*', recursive=True)
    dirs2.sort()
    dirs2 = []  # dirs2[-25:]  # take last xx

    dirs3 = glob.glob('C:\\AgodaGit\\passivbot\\cfgs_live\\*', recursive=True)
    dirs3.sort()
    dirs3 = []

    dirs.extend(dirs2)
    dirs.extend(dirs3)
    total = len(dirs)
    i = 1

    allowed_symbols = ["ETHUSDT", "XRPUSDT", "DOGEUSDT", "ADAUSDT",
                       "BNBUSDT", "MATICUSDT", "DOTUSDT", "SANDUSDT", "FTMUSDT",
                       "LTCUSDT", "LINKUSDT", "MANAUSDT", "ETCUSDT", "EOSUSDT",
                       "ATOMUSDT", "FILUSDT", "ICPUSDT", "ALICEUSDT", "LRCUSDT",
                       "BCHUSDT", "SUSHIUSDT", "XTZUSDT", "THETAUSDT", "CRVUSDT",
                       "ALGOUSDT", "CHZUSDT", "TRXUSDT", "CHRUSDT", "VETUSDT",
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
    '''
    "OMG",
    "DUSK",
    "GTC",
    "LRC", 
    "--------------------------"
    "SNX", "RSR",
    "--------------------------",
    "CELO", "ROSE", "OCEAN","SXP","DENT",
    "--------------------------",
    "SFP","ENS","DODO","AKRO","REEF","NEO",
    "----------------------------------------",
    "1000XEC","AKRO","ALPHA","ANKR","BAKE","BAND","BEL","BTS","C98","COMP",
    "-----------------------------------",
    "DGB","DOGO","FLM","FLOW","HBAR",
    "-----------------------------------",
    "HOT","ICX","IOST","IOTA","KAVA","KLAY","LINA","LIT","MKR","MTL","NEO","NKN","OGN","ONT"
    --------------------------
   "QTUM","REEF","RLC","RVN","SC","SFP","STMX","TOMO","TRB","UNFI","WAVES", "ZIL", "ZRX"
    
    '''
    allowed_symbols = ["WAVES", "ZIL", "ZRX"]
    allowed_symbols = [s + "USDT" for s in allowed_symbols]

    for dir in dirs:
        if dir.endswith(".json"):
            json_file = dir
            files = [json_file.split("\\")[-1]]
            dir = os.path.dirname(json_file) + "\\"
            symbol = json_file.split("\\")[-1].replace(".json", "USDT")
        else:
            if dir[-1] != '\\':
                dir = dir + '\\'
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
            print(f'using file : {live_config_path}')

        start_date = '2021-07-01'
        end_date = '2022-04-05'
        starting_balance = 15.0

        await do_backtest(
            backtest_config_path='C:\\AgodaGit\\passivbot\\configs\\backtest\\default.hjson',
            symbol=symbol,
            starting_balance=starting_balance,
            live_config_path=live_config_path,
            long_wallet_exposure_limit=6.0 / starting_balance,
            short_wallet_exposure_limit=5.0 / starting_balance,
            start_date=start_date,
            end_date=end_date,
            user='binance_01',
            enable_shorts=True,
            enable_longs=True,
            production_backtest=False
        )

        end = datetime.now()
        time_taken = (end - start).total_seconds() * 1000
        avg = time_taken / i  # sum(self.post_process_q) / len(self.post_process_q)
        print_progress(total, i, avg)
        i = i + 1


if __name__ == '__main__':
    asyncio.run(main())

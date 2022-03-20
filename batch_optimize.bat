@echo off
for %%x in (
        LTCUSDT
        XTZUSDT
        LINKUSDT
        ADAUSDT
        DOTUSDT
        UNIUSDT
        SUSHIUSDT
        AAVEUSDT
        DOGEUSDT
        MATICUSDT
        BNBUSDT
        SOLUSDT
        THETAUSDT
        COMPUSDT
        AXSUSDT
        LUNAUSDT
        SANDUSDT
        MANAUSDT
        ATOMUSDT
        AVAXUSDT
        CHZUSDT
        CRVUSDT
        ENJUSDT
        GRTUSDT
        SHIB1000USDT
        ICPUSDT
        FTMUSDT
        ALGOUSDT
        DYDXUSDT
        NEARUSDT
        BITUSDT
        GALAUSDT
        ONEUSDT
        ALICEUSDT
        EGLDUSDT
        RUNEUSDT
        WOOUSDT
        ENSUSDT
        IOTXUSDT
        BATUSDT
        SLPUSDT
        ZECUSDT
        1INCHUSDT
        ARUSDT
        PEOPLEUSDT
        CELOUSDT
        WAVESUSDT
        KNCUSDT
        LOOKSUSDT
        JASMYUSDT
        XRPUSDT
       ) do (
         echo harmony_search.py -oh --symbol %%x -pm r   --start_date 2021-08-01 --end_date 2022-03-15 --n_cpus 8 -u bybit_01
         python harmony_search.py -oh --symbol %%x -pm r  --start_date 2021-08-01 --end_date 2022-03-15 --n_cpus 8 -u bybit_01

         echo =-=-=-=-=-=

         echo  python harmony_search.py --symbol %%x -pm s  --start_date 2021-08-01 --end_date 2022-03-15 --n_cpus 8 -u bybit_01
         python harmony_search.py --symbol %%x -pm s  --start_date 2021-08-01 --end_date 2022-03-15 --n_cpus 8 -u bybit_01

         echo.
         echo =-=-=-xxxxxxxxxxx=-=-=
         echo.
       )
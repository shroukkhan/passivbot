@echo off
for %%x in (
            XRPUSDT
            ADAUSDT
            SOLUSDT
            TRXUSDT
            AXSUSDT
            LUNAUSDT
            SANDUSDT
            AVAXUSDT
            FTMUSDT
            ALGOUSDT
            NEARUSDT
            GALAUSDT
            ENSUSDT
            WAVESUSDT
            KNCUSDT
            APEUSDT
            GMTUSDT
            DARUSDT
       ) do (

         echo harmony_search.py -oh --symbol %%x -pm s  --start_date 2021-08-01 --end_date 2022-03-28 --n_cpus 13 -u bybit_01
         python harmony_search.py -oh --symbol %%x -pm r  --start_date 2021-08-01 --end_date 2022-05-03 --n_cpus 13 -u bybit_01

         echo =-=-=-=-=-=

         ::echo harmony_search.py -oh --symbol %%x -pm s  --start_date 2021-08-01 --end_date 2022-03-28 --n_cpus 13 -u binance_01
         ::python harmony_search.py -oh --symbol %%x -pm s --start_date 2021-08-01 --end_date 2022-04-23 --n_cpus 13 -u binance_01

         ::echo =-=-=-xxxxxxxxxxx=-=-=
         echo.
       )
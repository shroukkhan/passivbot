@echo off
for %%x in (
            1000XECUSDT
            AKROUSDT
            ALPHAUSDT
            ANKRUSDT
            BAKEUSDT
            BANDUSDT
            BELUSDT
            BTSUSDT
            C98USDT
            COMPUSDT
            DGBUSDT
            DODOUSDT
            FLMUSDT
            FLOWUSDT
            HBARUSDT
            HOTUSDT
            ICXUSDT
            IOSTUSDT
            IOTAUSDT
            KAVAUSDT
            KLAYUSDT
            LINAUSDT
            LITUSDT
            MKRUSDT
            MTLUSDT
            NEOUSDT
            NKNUSDT
            OGNUSDT
            ONTUSDT
            QTUMUSDT
            REEFUSDT
            RLCUSDT
            RVNUSDT
            SCUSDT
            SFPUSDT
            STMXUSDT
            TOMOUSDT
            TRBUSDT
            UNFIUSDT
            WAVESUSDT
            ZILUSDT
            ZRXUSDT

       ) do (

         echo harmony_search.py -oh --symbol %%x -pm r  --start_date 2021-08-01 --end_date 2022-03-28 --n_cpus 13 -u binance_01
         python harmony_search.py -oh --symbol %%x -pm r  --start_date 2021-08-01 --end_date 2022-04-01 --n_cpus 13 -u binance_01

         echo =-=-=-=-=-=

         ::echo harmony_search.py -oh --symbol %%x -pm s  --start_date 2021-08-01 --end_date 2022-03-28 --n_cpus 13 -u binance_01
         ::python harmony_search.py -oh --symbol %%x -pm s  --start_date 2021-08-01 --end_date 2022-04-01 --n_cpus 13 -u binance_01

         ::echo =-=-=-xxxxxxxxxxx=-=-=
         echo.
       )
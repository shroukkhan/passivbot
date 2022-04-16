@echo off
for %%x in (
            BATUSDT
            BALUSDT
            RUNEUSDT
            SRMUSDT
            STORJUSDT
            UNIUSDT
            FTMUSDT
            FILUSDT
            LRCUSDT
            CVCUSDT
            CTKUSDT
            SKLUSDT
            SANDUSDT
            XEMUSDT
            BTCSTUSDT
            MANAUSDT
       ) do (

         echo harmony_search.py -oh --symbol %%x -pm r  --start_date 2021-08-01 --end_date 2022-03-28 --n_cpus 13 -u binance_01
         python harmony_search.py -oh --symbol %%x -pm r  --start_date 2021-08-01 --end_date 2022-04-15 --n_cpus 13 -u binance_01

         echo =-=-=-=-=-=

         ::echo harmony_search.py -oh --symbol %%x -pm s  --start_date 2021-08-01 --end_date 2022-03-28 --n_cpus 13 -u binance_01
         ::python harmony_search.py -oh --symbol %%x -pm s  --start_date 2021-08-01 --end_date 2022-04-01 --n_cpus 13 -u binance_01

         ::echo =-=-=-xxxxxxxxxxx=-=-=
         echo.
       )
@echo off
for %%x in (
            FLOWUSDT
            1000XECUSDT
            1000BTTCUSDT
            ROSEUSDT
            ARUSDT
            CELRUSDT
            DUSKUSDT
            C98USDT
            KLAYUSDT
       ) do (
         :: echo  harmony_search.py --symbol %%x -pm r  --start_date 2021-08-01 --end_date 2022-02-28 --n_cpus 12 -u bybit_01
         :: python harmony_search.py -oh --symbol %%x -pm r  --start_date 2021-08-01 --end_date 2022-02-28 --n_cpus 12 -u bybit_01

         echo =-=-=-=-=-=

         echo harmony_search.py -oh --symbol %%x -pm s --start_date 2021-08-01 --end_date 2022-02-25 --n_cpus 12
         python harmony_search.py --symbol %%x -pm s --start_date 2021-08-01 --end_date 2022-03-05 --n_cpus 12

         echo.
         echo =-=-=-xxxxxxxxxxx=-=-=
         echo.
       )
@echo off
for %%x in (
           WAVESUSDT
           SUSHIUSDT
           RLCUSDT
           BNBUSDT
       ) do (
         ::echo harmony_search.py  -oh --symbol %%x -pm r --start_date 2021-08-01 --end_date 2022-02-25 --n_cpus 12
         ::python harmony_search.py --symbol %%x -pm r --start_date 2021-08-01 --end_date 2022-02-25 --n_cpus 6


         echo =-=-=-=-=-=

         echo harmony_search.py  -oh --symbol %%x -pm s --start_date 2021-08-01 --end_date 2022-02-25 --n_cpus 12
         python harmony_search.py -oh --symbol %%x -pm s --start_date 2021-08-01 --end_date 2022-02-25 --n_cpus 12

         echo.
         echo =-=-=-xxxxxxxxxxx=-=-=
         echo.
       )
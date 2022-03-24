@echo off
for %%x in (
            LINKUSDT
            ADAUSDT
            DOTUSDT
            DOGEUSDT
            MATICUSDT
            BNBUSDT
            THETAUSDT
            AXSUSDT
            LUNAUSDT
            SANDUSDT
            ATOMUSDT
            RUNEUSDT
            WAVESUSDT
       ) do (

         ::echo harmony_search.py -oh --symbol %%x -pm r   --start_date 2021-08-01 --end_date 2022-03-15 --n_cpus 14 -u bybit_01
         ::python harmony_search.py -oh --symbol %%x -pm r  --start_date 2021-08-01 --end_date 2022-03-15 --n_cpus 14 -u bybit_01

         echo =-=-=-=-=-=

         echo python harmony_search.py -oh --symbol %%x -pm s  --start_date 2021-08-01 --end_date 2022-03-15 --n_cpus 13 -u bybit_01
         python harmony_search.py -oh --symbol %%x -pm s  --start_date 2021-08-01 --end_date 2022-03-22 --n_cpus 13 -u bybit_01

         echo =-=-=-xxxxxxxxxxx=-=-=
         echo.
       )
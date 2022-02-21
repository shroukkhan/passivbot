@echo off
for %%x in (
        VETUSDT
        1INCHUSDT
        CELRUSDT
        SXPUSDT
        SRMUSDT
        COTIUSDT
        ZECUSDT
       ) do (
         echo harmony_search.py --symbol %%x --start_date 2021-08-01 --end_date 2022-02-15 --n_cpus 12
         python harmony_search.py  --symbol %%x --start_date 2021-08-01 --end_date 2022-02-15 --n_cpus 12
         echo.
         echo =-=-=-=-=-=
         echo.
       )
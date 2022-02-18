@echo off
for %%x in (
        XRPUSDT
        RUNEUSDT
        OMGUSDT
        ENJUSDT
        DOGEUSDT
       ) do (
         echo harmony_search.py --symbol %%x --start_date 2021-08-01 --end_date 2022-02-15 --n_cpus 13
         python harmony_search.py  --symbol %%x --start_date 2021-08-01 --end_date 2022-02-15 --n_cpus 13
         echo.
         echo =-=-=-=-=-=
         echo.
       )
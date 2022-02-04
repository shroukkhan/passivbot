@echo off
for %%x in (
        RUNEUSDT
        OMGUSDT
        ENJUSDT
        CELRUSDT
        SXPUSDT
        1INCHUSDT
        SRMUSDT
        COTIUSDT
       ) do (
         echo Doing python harmony_search.py  --symbol %%x --end_date 2022-02-02 --n_cpus 12
         python harmony_search.py  --symbol %%x --end_date 2022-02-02 --n_cpus 12
         echo.
         echo =-=-=-=-=-=
         echo.
       )
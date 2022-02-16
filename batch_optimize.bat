@echo off
for %%x in (
        ADAUSDT
        ALGOUSDT
        ALICEUSDT
        ATOMUSDT
        CHZUSDT
        CRVUSDT
        ETCUSDT
        FTMUSDT
        ICPUSDT
        LINKUSDT
        LTCUSDT
        MATICUSDT
        ONEUSDT
        XRPUSDT
       ) do (
         echo Doing python harmony_search.py  --symbol %%x --end_date 2022-02-02 --n_cpus 12
         python harmony_search.py  --symbol %%x --start_date 2021-08-01 --end_date 2022-02-15 --n_cpus 12
         echo.
         echo =-=-=-=-=-=
         echo.
       )
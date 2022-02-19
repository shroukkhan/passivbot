@echo off
for %%x in (
        ADAUSDT
        ALGOUSDT
        ALICEUSDT
        CHZUSDT
        CRVUSDT
        1000SHIBUSDT
        DOGEUSDT
        ICPUSDT
        LINKUSDT
        MATICUSDT
        ONEUSDT
       ) do (
         echo harmony_search.py --symbol %%x --start_date 2021-08-01 --end_date 2022-02-15 --n_cpus 13
         python harmony_search.py  --symbol %%x --start_date 2021-08-01 --end_date 2022-02-15 --n_cpus 13
         echo.
         echo =-=-=-=-=-=
         echo.
       )
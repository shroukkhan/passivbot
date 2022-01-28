@echo off
for %%x in (
        ETCUSDT
        EOSUSDT
        ATOMUSDT
        FILUSDT
        ICPUSDT
        ALICEUSDT
        LRCUSDT
       ) do (
         echo Doing python harmony_search.py  --symbol %%x --end_date 2022-01-27 --n_cpus 12
         python harmony_search.py  --symbol %%x --end_date 2022-01-27 --n_cpus 12
         echo.
         echo =-=-=-=-=-=
         echo.
       )
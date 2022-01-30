@echo off
for %%x in (
        ::ADAUSDT
        ::BNBUSDT
        ::MATICUSDT
        DOTUSDT
        SANDUSDT
        FTMUSDT
        LTCUSDT
        LINKUSDT
        MANAUSDT
        ETCUSDT
        EOSUSDT
        CRVUSDT
        CHZUSDT
        THETAUSDT
        ALICEUSDT
        VETUSDT
        ETCUSDT
       ) do (
         echo Doing python harmony_search.py  --symbol %%x --end_date 2022-01-27 --n_cpus 12
         python harmony_search.py  --symbol %%x --end_date 2022-01-27 --n_cpus 12
         echo.
         echo =-=-=-=-=-=
         echo.
       )
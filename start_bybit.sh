screen -X -S ATOM_bybit kill
screen -dmS ATOM_bybit ./run_bybit.sh ATOM

screen -X -S BCH_bybit kill
screen -dmS BCH_bybit ./run_bybit.sh BCH

screen -X -S EOS_bybit kill
screen -dmS EOS_bybit ./run_bybit.sh EOS

screen -X -S MATIC_bybit kill
screen -dmS MATIC_bybit ./run_bybit.sh MATIC

screen -X -S XRP_bybit kill
screen -dmS XRP_bybit ./run_bybit.sh XRP

screen -X -S LUNA_bybit kill
screen -dmS LUNA_bybit ./run_bybit.sh LUNA

screen -X -S WAVES_bybit kill
screen -dmS WAVES_bybit ./run_bybit.sh WAVES

screen -X -S API3_binance kill
screen -dmS API3_binance  ./run_long_short.sh API3

screen -X -S FLOW_binance kill
screen -dmS FLOW_binance  ./run_long_short.sh FLOW

screen -X -S KLAY_binance kill
screen -dmS KLAY_binance  ./run_long_short.sh KLAY
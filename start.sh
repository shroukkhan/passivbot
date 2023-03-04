screen -X -S ETH_binance_v5_9_3_clock kill
chmod +x cfgs_runtime/ETH.sh
screen -dmS ETH_binance_v5_9_3_clock ./cfgs_runtime/ETH.sh ETH

screen -X -S BNB_binance_v5_9_3_clock kill
chmod +x cfgs_runtime/BNB.sh
screen -dmS BNB_binance_v5_9_3_clock ./cfgs_runtime/BNB.sh BNB

screen -X -S ADA_binance_v5_9_3_clock kill
chmod +x cfgs_runtime/ADA.sh
screen -dmS ADA_binance_v5_9_3_clock ./cfgs_runtime/ADA.sh ADA
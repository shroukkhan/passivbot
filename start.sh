screen -X -S XMR_binance_v5_8 kill
chmod +x cfgs_runtime/XMR.sh
screen -dmS XMR_binance_v5_8 ./cfgs_runtime/XMR.sh XMR

screen -X -S NEAR_binance_v5_8 kill
chmod +x cfgs_runtime/NEAR.sh
screen -dmS NEAR_binance_v5_8 ./cfgs_runtime/NEAR.sh NEAR
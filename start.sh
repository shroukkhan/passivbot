screen -X -S EOS_binance_v5_9_0 kill
chmod +x cfgs_runtime/EOS.sh
screen -dmS EOS_binance_v5_9_0 ./cfgs_runtime/EOS.sh EOS

screen -X -S LINK_binance_v5_9_0 kill
chmod +x cfgs_runtime/LINK.sh
screen -dmS LINK_binance_v5_9_0 ./cfgs_runtime/LINK.sh LINK

screen -X -S XTZ_binance_v5_9_0 kill
chmod +x cfgs_runtime/XTZ.sh
screen -dmS XTZ_binance_v5_9_0 ./cfgs_runtime/XTZ.sh XTZ
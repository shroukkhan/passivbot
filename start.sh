screen -X -S DOGE_binance kill
chmod +x cfgs_runtime/DOGE.sh
screen -dmS DOGE_binance ./cfgs_runtime/DOGE.sh DOGE

screen -X -S HBAR_binance kill
chmod +x cfgs_runtime/HBAR.sh
screen -dmS HBAR_binance ./cfgs_runtime/HBAR.sh HBAR

screen -X -S LINK_binance kill
chmod +x cfgs_runtime/LINK.sh
screen -dmS LINK_binance ./cfgs_runtime/LINK.sh LINK

screen -X -S MATIC_binance kill
chmod +x cfgs_runtime/MATIC.sh
screen -dmS MATIC_binance ./cfgs_runtime/MATIC.sh MATIC

screen -X -S XRP_binance kill
chmod +x cfgs_runtime/XRP.sh
screen -dmS XRP_binance ./cfgs_runtime/XRP.sh XRP
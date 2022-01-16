#!/bin/bash
cd /home/skhan/passivbot/
source /home/skhan/passivbot/bin/activate
echo Runing : $1 ...
python3 passivbot.py binance_01 $1USDT cfgs_live/$1.json
#sleep 100

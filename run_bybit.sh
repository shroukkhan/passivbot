#!/bin/bash
cd /home/skhan/passivbot_5_5/
source /home/skhan/passivbot_5_5/bin/activate
echo Runing : $1 ...
python3 passivbot.py bybit_01 $1USDT cfgs_live_bybit/$1.json
#sleep 100
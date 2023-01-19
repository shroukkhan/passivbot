#!/bin/bash
cd /root/passivbot_5_8/
source /root/passivbot_5_8/.venv/bin/activate
echo Runing : $1 ...
while true; do
  python3 passivbot.py -sm tp -sw 0.03 -lm tp -lw 0.04 binance_01 $1USDT ./cfgs_live/$1.json
  echo died..restarting in 5
  sleep 1
  echo died..restarting in 4
  sleep 1
  echo died..restarting in 3
  sleep 1
  echo died..restarting in 2
  sleep 1
  echo died..restarting in 1
  sleep 1
done
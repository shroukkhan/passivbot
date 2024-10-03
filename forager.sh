#!/bin/bash
cd ~/passivbot2
source bin/activate
echo Runing : python3 forager.py configs/forager/forager.hjson ...
while true; do
  python3 forager.py configs/forager/forager.hjson
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
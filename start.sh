screen -X -S ALICE kill
screen -X -S ALICE_5_4 kill
screen -X -S ALICE_5_5 kill
screen -dmS ALICE_5_5 ./run.sh ALICE

screen -X -S GRT kill
screen -X -S GRT_5_4 kill
screen -X -S GRT_5_5 kill
screen -dmS GRT_5_5 ./run.sh GRT

screen -X -S ATOM kill
screen -X -S ATOM_5_4 kill
screen -X -S ATOM_5_5 kill
screen -dmS ATOM_5_5 ./run.sh ATOM

screen -X -S IOST kill
screen -X -S IOST_5_4 kill
screen -X -S IOST_5_5 kill
screen -dmS IOST_5_5 ./run.sh IOST

screen -X -S NEO kill
screen -X -S NEO_5_4 kill
screen -X -S NEO_5_5 kill
screen -dmS NEO_5_5 ./run.sh NEO


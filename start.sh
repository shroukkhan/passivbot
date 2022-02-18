screen -X -S ADA kill
screen -X -S ADA_5_4 kill
screen -dmS ADA_5_4 ./run.sh ADA

screen -X -S ALICE kill
screen -X -S ALICE_5_4 kill
screen -dmS ALICE_5_4 ./run.sh ALICE

screen -X -S CRV kill
screen -X -S CRV_5_4 kill
screen -dmS CRV_5_4 ./run.sh CRV

screen -X -S DOGE kill
screen -X -S DOGE_5_4 kill
screen -dmS DOGE_5_4 ./run.sh DOGE

screen -X -S ICP kill
screen -X -S ICP_5_4 kill
screen -dmS ICP_5_4 ./run.sh ICP

screen -X -S LINK kill
screen -X -S LINK_5_4 kill
screen -dmS LINK_5_4 ./run.sh LINK

screen -X -S MATIC kill
screen -X -S MATIC_5_4 kill
screen -dmS MATIC_5_4 ./run.sh MATIC

screen -X -S ONE kill
screen -X -S ONE_5_4 kill
screen -dmS ONE_5_4 ./run.sh ONE

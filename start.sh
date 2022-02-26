screen -X -S ALICE kill
screen -X -S ALICE_5_4 kill
screen -X -S ALICE_5_5 kill
screen -dmS ALICE_5_5 ./run.sh ALICE

screen -X -S COTI kill
screen -X -S COTI_5_4 kill
screen -X -S COTI_5_5 kill
screen -dmS COTI_5_5 ./run.sh COTI

screen -X -S GRT kill
screen -X -S GRT_5_4 kill
screen -X -S GRT_5_5 kill
screen -dmS GRT_5_5 ./run.sh GRT

screen -X -S ETC kill
screen -X -S ETC_5_4 kill
screen -X -S ETC_5_5 kill
screen -dmS ETC_5_5 ./run.sh ETC

screen -X -S IOST kill
screen -X -S IOST_5_4 kill
screen -X -S IOST_5_5 kill
screen -dmS IOST_5_5 ./run.sh IOST

screen -X -S OMG kill
screen -X -S OMG_5_4 kill
screen -X -S OMG_5_5 kill
screen -dmS OMG_5_5 ./run.sh OMG


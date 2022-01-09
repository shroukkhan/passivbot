for i in {1..26}
do
    for dir in backtests/binance/*; do
        if [ -d "$dir" ]; then
            echo "Doing : ${dir##*/} $i"
            python3 optimize.py -o configs/optimize/default.hjson --symbol ${dir##*/} -sd 2021-05-01 -ed 2021-12-31
        fi
    done
done

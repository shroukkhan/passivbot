# iterate over backtests/binance/**/plots folder and delete all subfolders insider plots folder

import os
import shutil
import glob

# find ROOT_PATH. root path is one level above current path
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def delete_cache_files():
    old_backtest = glob.glob(ROOT_PATH + '/backtests/binance/**/*_ohlcv_cache.npy', recursive=True)
    # now delete all folders containing backtest_result.txt
    for file in old_backtest:
        directory_to_delete = os.path.dirname(file)
        if os.path.exists(directory_to_delete):
            print('deleting directory: ', directory_to_delete)
            shutil.rmtree(directory_to_delete)


def delete_image_files():
    long_files = glob.glob(ROOT_PATH + '/backtests/binance/**/backtest_long*.png', recursive=True)
    # now delete all folders containing backtest_result.txt
    for file in long_files:
        print('deleting file: ', file)
        os.remove(file)

    # do the same for short
    short_files = glob.glob(ROOT_PATH + '/backtests/binance/**/backtest_short*.png', recursive=True)
    for file in short_files:
        print('deleting file: ', file)
        os.remove(file)


    


if __name__ == '__main__':
    #delete_cache_files()
    delete_image_files()

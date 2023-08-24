# iterate over backtests/binance/**/plots folder and delete all subfolders insider plots folder

import os
import shutil
import glob

# find ROOT_PATH. root path is one level above current path
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def create_backtest_command():
    '''
    Read content of ROOT_PATH\bbacktest_commands_donewithdollar.bat into an array ( each line one row )
    split it equally into 8 parts, last part contains the extra line or so
    write them into 8 different files 
    '''
    backtest_commands = []
    with open(os.path.join(ROOT_PATH, 'backtest_commands_donewithdollar.bat'), 'r') as f:
        backtest_commands = f.readlines()
    # now split backtest_commands into 8 different arrays and write them into 8 different files
    each_file_length = len(backtest_commands) // 8
    for i in range(8):
        with open(os.path.join(ROOT_PATH, 'backtest_commands_donewithdollar_{}.bat'.format(i)), 'w') as f:
            if i == 7:
                f.writelines(backtest_commands[i * each_file_length:])
            else:
                f.writelines(backtest_commands[i * each_file_length: (i + 1) * each_file_length])

    


if __name__ == '__main__':
    create_backtest_command()
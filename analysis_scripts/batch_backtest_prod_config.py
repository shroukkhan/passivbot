# iterate over backtests/binance/**/plots folder and delete all subfolders insider plots folder

import os
import shutil
import glob

# find ROOT_PATH. root path is one level above current path
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# def delete_old_backtests():
#     old_backtest = glob.glob(ROOT_PATH + '/backtests/binance/**/backtest_result.txt', recursive=True)
#     # now delete all folders containing backtest_result.txt
#     for file in old_backtest:
#         directory_to_delete = os.path.dirname(file)
#         print('deleting directory: ', directory_to_delete)
#         shutil.rmtree(directory_to_delete)
# 



def create_backtest_command():
    '''
    now list all *.json file in ROOT_PATH\configs\live\older_versions 's subfolders and create a list of dictionary, 
    where key is the filename and value is the full path to the json
    '''
    live_configs = glob.glob(ROOT_PATH + '/configs/live/older_versions/**/*.json', recursive=True)
    
    # now create a list of dictionary, where key is the filename ( replace .json ) and value is the full path to the json
    live_configs_dict = {}
    for config in live_configs:
        live_configs_dict[os.path.basename(config).replace('.json','USDT')] = config

    # now create a list of shell command to execute, each command loooks like this : python backtest.py -s {key} value 
    # where key value comes from live_configs_dict
    command_list = []
    allowed_coins = ['SANDUSDT', 'AVAXUSDT', 'BNBUSDT', 'RUNEUSDT']
    for key, value in live_configs_dict.items():
        if key in allowed_coins:
            command_list.append('python backtest.py -s {} {}'.format(key, value))
    
    # now write the command_list to a file
    with open(ROOT_PATH + '/backtest_commands.bat', 'w') as f:
        for command in command_list:
            f.write(command + '\n')

    


if __name__ == '__main__':
    #delete_old_backtests()
    create_backtest_command()
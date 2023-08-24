# iterate over backtests/binance/**/plots folder and delete all subfolders insider plots folder

import os
import shutil
import glob

# find ROOT_PATH. root path is one level above current path
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def create_backtest_command():
    '''
    now list all *.json file in ROOT_PATH\configs\live\older_versions 's subfolders and create a list of dictionary, 
    where key is the filename and value is the full path to the json
    '''
    live_configs = glob.glob(ROOT_PATH + '/downloaded_configs/passivbot_v5.9.x/configs/**/config.json', recursive=True)
    
    # now create a list of dictionary, where key is the filename ( replace .json ) and value is the full path to the json
    live_configs_dict = {}
    for config in live_configs:
            symbol = os.path.dirname(config).split('\\')[-1] # MATICUSDT_20230120160334_bac70
            # split symbol by _ and get the first part
            symbol = symbol.split('_')[0] # MATICUSDT
            
            if symbol not in live_configs_dict:
                live_configs_dict[symbol] = []
            live_configs_dict[symbol].append(config)
            
            

    # now create a list of shell command to execute, each command loooks like this : python backtest.py -s {key} value 
    # where key value comes from live_configs_dict
    command_list = []
    for key, value in live_configs_dict.items():
        for config in value:
            command_list.append('python backtest.py -s {} {}'.format(key, config))
    
    print(command_list)
    
    # now write the command_list to a file
    with open(ROOT_PATH + '/backtest_commands_donewithdollar.bat', 'w') as f:
        for command in command_list:
            f.write(command + '\n')

    


if __name__ == '__main__':
    create_backtest_command()
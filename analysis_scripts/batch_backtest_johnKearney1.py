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
    live_configs = glob.glob(ROOT_PATH + '/downloaded_configs/JohnKearney1_config/**/*.json', recursive=True)
    
    # now create a list of dictionary, where key is the filename ( replace .json ) and value is the full path to the json
    live_configs_dict = {}
    for config in live_configs:
        # if the path contains v5.9 , only then add it to the list
        if 'v5.9.11' in config:
            symbol = os.path.basename(config).replace('.json','')
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
    with open(ROOT_PATH + '/backtest_commands_jonhkearney1.bat', 'w') as f:
        for command in command_list:
            f.write(command + '\n')

    


if __name__ == '__main__':
    create_backtest_command()
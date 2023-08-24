text = '''
C:/AgodaGit/passivbot/backtests/binance/ZILUSDT/plots/2023-08-22T104604/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZECUSDT/plots/2023-08-22T102333/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZILUSDT/plots/2023-08-22T105650/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZENUSDT/plots/2023-08-22T103855/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZECUSDT/plots/2023-08-22T102633/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZILUSDT/plots/2023-08-22T105407/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZILUSDT/plots/2023-08-22T104733/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZILUSDT/plots/2023-08-22T104911/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZILUSDT/plots/2023-08-22T105053/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZILUSDT/plots/2023-08-22T105530/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZECUSDT/plots/2023-08-22T102754/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZECUSDT/plots/2023-08-22T102914/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZECUSDT/plots/2023-08-22T102504/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZECUSDT/plots/2023-08-22T101845/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZECUSDT/plots/2023-08-22T102027/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZECUSDT/plots/2023-08-22T102201/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZENUSDT/plots/2023-08-22T103727/live_config.json
C:/AgodaGit/passivbot/backtests/binance/ZENUSDT/plots/2023-08-22T103537/live_config.json

'''

import shutil
import os

l_s = 'short'

def copy_files(text):
    for line in text.split('\n'):
        if line:
            line = line.replace('\\', '/')
            # find an image file called balance_and_equity_sampled_long.png in the same folder as the live_config.json
            image_file = line.replace('live_config.json', f'balance_and_equity_sampled_{l_s}.png')
            # get the directory name containing the image file
            file_name = image_file.split('/')[-2]
            coin_name = image_file.split('/')[-4]
            # copy the image file to the C:\AgodaGit\passivbot\tmp folder
            src = image_file
            dst = f'C:/AgodaGit/passivbot/tmp/test/{coin_name}-{file_name}-{l_s}.png'
            if os.path.isfile(src):
                shutil.copyfile(src, dst)
            

def delete_files():
    # delete all png files in C:\AgodaGit\passivbot\tmp\test folder
    for file in os.listdir('C:/AgodaGit/passivbot/tmp/test'):
        if file.endswith('.png'):
            os.remove(f'C:/AgodaGit/passivbot/tmp/test/{file}')

delete_files()
copy_files(text)
#exit app normally
exit()

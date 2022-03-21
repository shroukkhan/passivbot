# --------------------------------------------------------------
# bybit volM and notional and symbol and binance listed check
import glob

import requests

files = glob.glob('C:\\AgodaGit\\passivbot\\cfgs_live_bybit\\*', recursive=True)
files.sort()
existing_symbols = []
for file in files:
    symbol = file.split('\\')[-1]
    symbol = symbol.replace('.json', 'USDT')
    existing_symbols.append(symbol)

symboldata_url = "https://api.bybit.com/v2/public/symbols"
symboldata = requests.get(symboldata_url).json()
tickerdata_url = "https://api.bybit.com/v2/public/tickers"
tickerdata = requests.get(tickerdata_url).json()
binsymbols_url = "https://fapi.binance.com/fapi/v1/exchangeInfo"
binsymbols = requests.get(binsymbols_url).json()

binsymbollist = []
for k in binsymbols['symbols']:
    binsymbollist.append(k['symbol'])

resultlist = []
resultlistnotional = []
coins = []
for i in symboldata['result']:
    if 'USDT' in i['name']:
        symbol = i['name']
        if symbol not in existing_symbols:
            continue

        # print (f"symbol:{symbol}")
        min_qty = float(i['lot_size_filter']['min_trading_qty'])

        for j in tickerdata['result']:
            if j['symbol'] == symbol:
                price = float(j['last_price'])
                volm = str((int(float(j["turnover_24h"]) / 1000000))).zfill(4)

                min_notional = min_qty * price

        if symbol in binsymbollist:
            bin_listed = "Yes"
        else:
            bin_listed = "No"

        #if min_notional <= 20 and float(volm) > 2:
        coins.append(symbol)
        resultlist.append(f"{volm}\t\t{min_notional:.2f}\t\t{symbol.ljust(13, ' ')}\t{bin_listed}")
        resultlistnotional.append(f"{min_notional:.2f}\t\t{volm}\t\t{symbol.ljust(13, ' ')}\t{bin_listed}")
# list1: sort on volM
resultlist.sort(reverse=True)
print("volM$\t\tnotional\tsymbol\t\tBinance Listed")
for i in resultlist:
    print(i)

# print("\n------------------------------------------------")
# for i in coins:
#     print(i)

# # list2: sort on notional
# resultlistnotional.sort(reverse=True)
# print("notional\tvolM$\t\tsymbol\t\tBinance Listed")
#
# c = []
# for i in resultlistnotional:
#     print(i)

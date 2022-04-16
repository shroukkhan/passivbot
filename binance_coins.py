# binance
import datetime
import glob

import requests

resultlist = []
resultlistnotional = []

files = glob.glob('C:\\AgodaGit\\passivbot\\cfgs_live\\*', recursive=True)
files.sort()

existing_symbols = []
for file in files:
    symbol = file.split('\\')[-1]
    symbol = symbol.replace('.json', 'USDT')
    existing_symbols.append(symbol)


data_url = "https://fapi.binance.com/fapi/v1/exchangeInfo"
data = requests.get(data_url).json()
prices_url = "https://fapi.binance.com/fapi/v1/ticker/price"
pricedata = requests.get(prices_url).json()
volume_url = "https://fapi.binance.com//fapi/v1/ticker/24hr"
volume_data = requests.get(volume_url).json()

min_listing_date = datetime.datetime(2021, 7, 1, )
must_be_listed_before = datetime.datetime.timestamp(min_listing_date) * 1000

coinlist = []
try:
    for datas in data["symbols"]:
        if "USDT" in datas["pair"]:
            ts = datas['onboardDate']
            listed_on = datetime.datetime.utcfromtimestamp(ts / 1000).strftime(
                '%Y-%m-%d %H:%M:%S')
            symbol = datas["pair"]

            if symbol not in existing_symbols:
                if ts > must_be_listed_before:
                    continue
                min_qty = float(datas["filters"][1]["minQty"])
                min_notional_fixed = float(datas["filters"][5]["notional"])

                price = 0
                for i in pricedata:
                    if i["symbol"] == symbol:
                        price = i["price"]

                for i in volume_data:
                    if i["symbol"] == symbol:
                        volm = str((int(float(i["quoteVolume"]) / 1000000))).zfill(4)

                min_notional_calc = min_qty * float(price)

                if min_notional_calc <= min_notional_fixed:
                    min_notional = min_notional_fixed
                else:
                    min_notional = min_notional_calc

                if min_notional <= 10 and float(volm) > 10:
                    resultlist.append(f"{volm}\t\t{min_notional:.2f}\t\t{symbol.ljust(13, ' ')}\t\t{listed_on}")
                    resultlistnotional.append(f"{min_notional:.2f}\t\t{volm}\t\t{symbol.ljust(13, ' ')}\t\t{listed_on}")
                    coinlist.append(symbol)

except Exception as e:
    print(f'Error: {e}')
    pass

# list1: sort on volM
resultlist.sort(reverse=True)
print("volM$\t\tnotional\tsymbol\tlisted_on")
for i in resultlist:
    print(i)

print("\n")

for coin in coinlist:
    print(coin)

# # list2: sort on notional
# resultlistnotional.sort(reverse=True)
# print("notional\tvolM$\t\tsymbol")
# for i in resultlistnotional:
#     print(i)

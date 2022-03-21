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



# existing_symbols = ["ETHUSDT", "XRPUSDT", "DOGEUSDT", "ADAUSDT",
#                     "BNBUSDT", "MATICUSDT", "DOTUSDT", "SANDUSDT", "FTMUSDT",
#                     "LTCUSDT", "LINKUSDT", "MANAUSDT", "ETCUSDT", "EOSUSDT",
#                     "ATOMUSDT", "FILUSDT", "ICPUSDT", "ALICEUSDT", "LRCUSDT",
#                     "BCHUSDT", "SUSHIUSDT", "XTZUSDT", "THETAUSDT", "CRVUSDT",
#                     "ALGOUSDT", "CHZUSDT", "TRXUSDT", "CHRUSDT", "VETUSDT",
#                     "ONEUSDT", "OMGUSDT", "XLMUSDT", "RUNEUSDT", "ENJUSDT",
#                     "CELRUSDT", "SXPUSDT", "1INCHUSDT", "SRMUSDT", "COTIUSDT",
#                     "ZECUSDT", "QTUMUSDT", "GRTUSDT", "DENTUSDT", "SFPUSDT",
#                     "STORJUSDT", "IOTAUSDT", "HOTUSDT", "NEOUSDT", "COMPUSDT",
#                     "LINAUSDT", "KAVAUSDT", "BATUSDT", "WAVESUSDT", "IOSTUSDT",
#                     "ALPHAUSDT", "RLCUSDT", "HBARUSDT", "DODOUSDT", "XMRUSDT",
#                     "SNXUSDT", "ANKRUSDT", "DASHUSDT", "REEFUSDT", "ZENUSDT",
#                     "CVCUSDT", "RENUSDT", "ICXUSDT", "RSRUSDT", "SKLUSDT",
#                     "NKNUSDT", "BELUSDT", "ONTUSDT", "OGNUSDT", "BLZUSDT",
#                     "MTLUSDT", "CTKUSDT", "RVNUSDT", "LITUSDT", "MKRUSDT",
#                     "OCEANUSDT", "ZILUSDT", "UNFIUSDT", "BANDUSDT", "YFIIUSDT",
#                     "TOMOUSDT", "TRBUSDT", "KNCUSDT", "STMXUSDT", "ZRXUSDT",
#                     "SCUSDT", "AKROUSDT", "XEMUSDT", "FLMUSDT", "BALUSDT",
#                     "BTSUSDT", "DGBUSDT", "DEFIUSDT"]



_d = datetime.datetime(2021, 8, 1, )
must_be_listed_before = datetime.datetime.timestamp(_d) * 1000

try:
    for datas in data["symbols"]:
        if "USDT" in datas["pair"]:
            ts = datas['onboardDate']
            listed_on = datetime.datetime.utcfromtimestamp(ts / 1000).strftime(
                '%Y-%m-%d %H:%M:%S')
            symbol = datas["pair"]

            # if ts > must_be_listed_before:
            #     continue
            if symbol not in existing_symbols:
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

            #if min_notional <= 20 and float(volm) > 3:
            resultlist.append(f"{volm}\t\t{min_notional:.2f}\t\t{symbol.ljust(13, ' ')}\t\t{listed_on}")
            resultlistnotional.append(f"{min_notional:.2f}\t\t{volm}\t\t{symbol.ljust(13, ' ')}\t\t{listed_on}")

except Exception as e:
    print(f'Error: {e}')
    pass

# list1: sort on volM
resultlist.sort(reverse=True)
print("volM$\t\tnotional\tsymbol\tlisted_on")
for i in resultlist:
    print(i)

print("\n")

# # list2: sort on notional
# resultlistnotional.sort(reverse=True)
# print("notional\tvolM$\t\tsymbol")
# for i in resultlistnotional:
#     print(i)

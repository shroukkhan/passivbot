# binance
import requests

resultlist = []
resultlistnotional = []

data_url = "https://fapi.binance.com/fapi/v1/exchangeInfo"
data = requests.get(data_url).json()
prices_url = "https://fapi.binance.com/fapi/v1/ticker/price"
pricedata = requests.get(prices_url).json()
volume_url = "https://fapi.binance.com//fapi/v1/ticker/24hr"
volume_data = requests.get(volume_url).json()

try:
    for datas in data["symbols"]:
        if "USDT" in datas["pair"]:
            symbol = datas["pair"]
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

            if min_notional <= 6 and float(volm) > 5:
                resultlist.append(f"{volm}\t\t{min_notional:.2f}\t\t{symbol.ljust(13, ' ')}")
                resultlistnotional.append(f"{min_notional:.2f}\t\t{volm}\t\t{symbol.ljust(13, ' ')}")

except Exception as e:
    print(f'Error: {e}')
    pass

# list1: sort on volM
resultlist.sort(reverse=True)
print("volM$\t\tnotional\tsymbol")
for i in resultlist:
    print(i)

print("\n")

# # list2: sort on notional
# resultlistnotional.sort(reverse=True)
# print("notional\tvolM$\t\tsymbol")
# for i in resultlistnotional:
#     print(i)

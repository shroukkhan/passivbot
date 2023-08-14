#binance
import requests

#set these:
balance = 10000
we = 0.05
initial_qty_pct = 0.0171146

#dont touch these
iec = balance * we * initial_qty_pct
print (f"Binance:\nIEC: ${iec:.2f} \n ")

list = []

data_url = "https://fapi.binance.com/fapi/v1/exchangeInfo"
data = requests.get(data_url).json()
prices_url = "https://fapi.binance.com/fapi/v1/ticker/price"
pricedata = requests.get(prices_url).json()

try:
    for datas in data["symbols"]:
        if "USDT" in datas["pair"]:
            symbol = datas["pair"]
            min_qty = float(datas["filters"][1]["minQty"] )
            min_notional_fixed =  float(datas["filters"][5]["notional"])

            for i in pricedata:
                if i["symbol"] == symbol:
                    price = i["price"]

            min_notional_calc = min_qty * float(price)

            if min_notional_calc <= min_notional_fixed:
                min_notional = min_notional_fixed
            else:
                min_notional = min_notional_calc

            if iec >= min_notional:
                list.append(f"{symbol.ljust(13)}\t min_notional: ${min_notional:.2f}\t GRID OK")
            else:
                list.append(f"{symbol.ljust(13)}\t min_notional: ${min_notional:.2f}\t GRID NOT OK")

except Exception as e:
    print(f'Error: {e}')
    pass

list.sort()
for i in list:
    print (i)

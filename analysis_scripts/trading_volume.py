import requests

def get_24h_trading_volume(symbol):
    base_url = "https://api.binance.com/api/v3/ticker/24hr"
    params = {"symbol": symbol}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        trading_volume = float(data["quoteVolume"]) / 10**6
        return trading_volume
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    symbol = "BTCUSDT"
    trading_volume = get_24h_trading_volume(symbol)
    if trading_volume is not None:
        print(f"Last 24-hour trading volume for {symbol}: {trading_volume:.2f} million USD")

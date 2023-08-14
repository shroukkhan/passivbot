import requests
from datetime import datetime, timedelta

def get_trading_volume_in_usd(symbol):
    api_url = "https://api.binance.com/api/v3/klines"
    interval = "1d"

    end_time = int(datetime.now().timestamp() * 1000)
    start_time = int((datetime.now() - timedelta(days=7)).timestamp() * 1000)

    params = {
        "symbol": symbol,
        "interval": interval,
        "startTime": start_time,
        "endTime": end_time
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        trading_volume_in_usd = 0

        for entry in data:
            open_price = float(entry[1])
            close_price = float(entry[4])
            high_price = float(entry[2])
            low_price = float(entry[3])
            trading_volume = float(entry[5])

            weighted_avg_price = (open_price + close_price + high_price + low_price) / 4
            trading_volume_in_usd += weighted_avg_price * trading_volume

        return trading_volume_in_usd
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

symbol = "BTCUSDT"  # Replace with the symbol you're interested in
trading_volume_usd = get_trading_volume_in_usd(symbol)

if trading_volume_usd is not None:
 print(f"Last 7 days trading volume in USD for {symbol}: {trading_volume_usd / 1000000:.2f} million")



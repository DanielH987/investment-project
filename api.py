import requests, json

def get_stock_prices(api_key, symbol):
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": api_key
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if "Time Series (Daily)" in data:
        return data["Time Series (Daily)"]
    else:
        return {"Error": "Invalid symbol or API key."}

# Example usage
api_key = "apikey"
symbol = "AAPL"
stock_prices = get_stock_prices(api_key, symbol)
print(json.dumps(stock_prices, indent=4))
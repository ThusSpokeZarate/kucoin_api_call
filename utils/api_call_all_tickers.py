# Import required libraries and dependencies

import pandas as pd
import os
import json
import requests
from dotenv import load_dotenv
%matplotlib inline
import time
import base64
import hmac
import hashlib

# Load .env enviroment variables into the notebook
load_dotenv()

# Get the API key from the environment variable and store as Python variable
kucoin_api_key = os.getenv("KUCOIN_API_KEY")
kucoin_secret_key = os.getenv("KUCOIN_SECRET_KEY")
kucoin_passphrase = os.getenv("KUCOIN_PASSPHRASE")


#pull user account filled spot trade orders data with kucoin api call format
api_key = kucoin_api_key
api_secret = kucoin_secret_key
api_passphrase = kucoin_passphrase
url = 'https://api.kucoin.com/api/v1/market/allTickers'
now = int(time.time() * 1000)
str_to_sign = str(now) + 'GET' + '/api/v1/market/allTickers'
signature = base64.b64encode(
    hmac.new(api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
passphrase = base64.b64encode(hmac.new(api_secret.encode('utf-8'), api_passphrase.encode('utf-8'), hashlib.sha256).digest())
headers = {
    "KC-API-SIGN": signature,
    "KC-API-TIMESTAMP": str(now),
    "KC-API-KEY": api_key,
    "KC-API-PASSPHRASE": passphrase,
    "KC-API-KEY-VERSION": "2"
}

kucoin_response = requests.request('get', url, headers=headers)
print(kucoin_response.status_code)
kucoin_all_tickers = kucoin_response.json()
print(json.dumps(kucoin_all_tickers, indent=2, sort_keys=True))



tickers_json = kucoin_all_tickers["data"]["ticker"][:]
all_tickers = []

index = 0
for index in range(len(tickers_json)):
    for key in tickers_json[index]:
        if key == "symbol":
            all_tickers.append(str(tickers_json[index][key]))

print(all_tickers)
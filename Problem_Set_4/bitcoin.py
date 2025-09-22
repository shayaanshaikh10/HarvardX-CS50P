import requests
import sys
import json

if len(sys.argv)==1:
    sys.exit("Missing command-line argument")

try:
    no_of_bit=float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")

response=requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey=26f60c0fcd8f350b317edd0314bd4b9acf29d506a949d3bf71e00c9e7681f4f0")
o=response.json()
bitcoin_data=o['data']
value=bitcoin_data["priceUsd"]
value=float(value)
value=no_of_bit*value
print(f"${value:,.4f}")
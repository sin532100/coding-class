import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

print(type(btc['opening_price']))

a = float(btc['opening_price']) + (float(btc['max_price']) - float(btc['min_price']))

if a > float(btc['max_price']):
    print('상승장')
else:
    print('하락장')
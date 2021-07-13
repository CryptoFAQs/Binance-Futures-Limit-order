
# pip install python-binance

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

symbol = "DOGEUSDT"
contract_size = 100
api_key = ''
api_secret = ''
client = Client(api_key, api_secret)

def limit_buy(contract, contract_size, price):
    try:
        limit_buy = client.futures_create_order(
        symbol = contract,
        side = Client.SIDE_BUY,
        type = Client.ORDER_TYPE_LIMIT,
        timeInForce = 'GTC',
        quantity = contract_size,
        price = price)

    except BinanceAPIException as e:
        print(e)
    except BinanceOrderException as e:
        print(e)

def limit_sell(contract, contract_size, price):
    try:
        limit_sell = client.futures_create_order(
        symbol = contract,
        side = Client.SIDE_SELL,
        type = Client.ORDER_TYPE_LIMIT,
        timeInForce = 'GTC',
        quantity = contract_size,
        price = price)

    except BinanceAPIException as e:
        print(e)
    except BinanceOrderException as e:
        print(e)


limit_buy(symbol, contract_size, 0.1)


import requests
# from bs4 import BeautifulSoup as BS


def get_btc():
    bitcoin_api_url = 'https://api.blockchair.com/bitcoin/stats'
    response = requests.get(bitcoin_api_url)
    response_json = response.json()
    btc = response_json['data']['market_price_usd']
    return btc


def get_eth():
    ethereum_api_url = 'https://api.blockchair.com/ethereum/stats'
    response_eth = requests.get(ethereum_api_url)
    response_eth_json = response_eth.json()
    eth = response_eth_json['data']['market_price_usd']
    return eth


# bitcoin_api_url = 'https://api.blockchair.com/bitcoin/stats'
# response = requests.get(bitcoin_api_url).json()
# btc = response_json['data']['market_price_usd']
# print(response.text)
print(get_btc())

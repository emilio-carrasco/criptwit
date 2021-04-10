
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

def dict_currencies():
    return [ 
        {'symbol' :'BTC', 'name' : 'Bitcoin' },
    {'symbol' :'ETH', 'name' : 'Ethereum' },
    {'symbol' :'BTC', 'name' : 'Bitcoin' },
    {'symbol' :'Tether', 'name' : 'USDT' },
    {'symbol' :'ADA', 'name' : 'Cardano' },
    {'symbol' :'DOT', 'name' : 'Polkadot' },
    {'symbol' :'LTC', 'name' : 'Litecoin' },
    ]

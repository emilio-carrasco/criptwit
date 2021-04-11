
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
from time import sleep


def read_currencies(file_):
    """
    This function read a txt from its path and return a dictionary with names and symbols of cripto currencies.
    file_: pacth to the txt file

    """
    try:
        dict_ = dict()
        open_file=open(file_)
        symbol = open_file.readline()[:-1]
        name = open_file.readline()[:-1]
        while symbol:
            dict_[symbol] = name
            
            symbol = open_file.readline()[:-1]
            name = open_file.readline()[:-1]
        return dict_
    except:
        raise IOError("File reading error") 

def appears(x, set_):
    """
    this function returns boolean if x in in set_ comparing lower cases
    x:string
    set_: set of strings
    """
    set_lower=set([element.lower() for element in list(set_)])
    return x.lower() in set_lower

def sub_current(df,dict_):
    df_sub=dict()
    for symbol, name  in dict_.items():
        columns_=list(df.columns[:-1])
        
        df_sub[name] = df[df.MATCHING.apply(lambda set_currencies:appears(name,set_currencies))][columns_]
    return df_sub

def currencies_prices(dict_df, vs_):
    """
    takes a dict of data frames wwith all the subsets and adds current values
    
    """
    for name,df  in dict_df.items():        
        if not df.empty:
            df[name]=current_prices_df('before','after',df,name)

def consult_api(name,vs_,from_, to_):
    return cg.get_coin_market_chart_range_by_id(name, vs_, from_, to_)

def current_prices_df(before,after,df,name):
    """
    """
    hour_ut = 3600
    num_hours = 6
    intervale = hour_ut * num_hours
    from_= x - interval
    to_ = x - intervale
    df[before]=df.ut
    df[after]=df.ut
    df.before=df.befor.appy(lambda x:consult_api(name,vs_,from_, x))
    df.after=df.after.appy(lambda x:consult_api(name,vs_,x, to_))

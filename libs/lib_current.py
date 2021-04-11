
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
            dict_df[name]=current_prices_df(df,name,vs_)
            

    return dict_df

def consult_api(name, vs_, ut,b_a):
    """
    returs a miutely list for the name of the currency with price and utc
    name: strin currency name
    
    vs_: currency name to exchange with
    ut: unix time of twt
    b_a='before' or 'after'

    """
    hour_ut = 3600
    num_hours = 6
    interval = hour_ut * num_hours
    
    if b_a == 'before':
        from_= int(ut - interval)
        to_ = int(ut)
    elif b_a == 'after':
        from_= int(ut)
        to_ = int(ut + interval)
    
    return cg.get_coin_market_chart_range_by_id(name, vs_, from_, to_)['prices']

def current_prices_df(df,name,vs_):
    """

    """

    df['before']=df.UT
    df['after']=df.UT
    df.before=df.before.apply(lambda x:consult_api(name,vs_,x,'before'))
    df.after=df.after.apply(lambda x:consult_api(name,vs_,x,'after'))
    return df
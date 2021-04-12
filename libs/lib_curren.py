
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
from time import sleep

def read_currencies(file_):
    """
    This function read a txt from its path and return a dictionary with names and symbols of cripto currencies.
    file_: pacth to the txt file

    return dict {symbol:name}
    """
    try:
        dict_ = dict()
        open_file = open(file_)
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

    returns:boolean
    """
    set_lower = set([element.lower() for element in list(set_)])
    return x.lower() in set_lower

def sub_curren(df,dict_):
    """
    this funcion takes a df and crates a dictionary with subdta frames of every cripto current
    df: datafram
    dict_: dictionary with {symbol:name} of criptcurrencies

    return: dictionary {<name_currency>:<subdata_frame>}
    """
    df_sub = dict()
    for symbol, name  in dict_.items():
        columns_ = list(df.columns[:-1])
        df_aux = df[df.MATCHING.apply(lambda set_currencies:appears(name, set_currencies))][columns_]
        df_sub[name] = df_aux.drop_duplicates().reset_index(drop=True)
    return df_sub

def currencies_prices(dict_df, vs_):
    """
    takes a dict of data frames with all the subsets and adds current values
    
    """
    for name,df  in dict_df.items():        
        if not df.empty:
            dict_df[name] = before_after_prices_df(df, name,vs_)
    return dict_df

def before_after_prices_df(df,name,vs_):
    """
    this function add before and after columns in df and consults API for the price vs our currency

    df: dataframe
    name: criptcurrency name to consult
    vs_: currency to compare with

    """
    df['prices'] = df.UT
    df.prices = df.prices.apply(lambda x:consult_api_price(name, vs_, x))
    df.dropna(subset=['prices'], inplace=True)
    (df)
    
    df.reset_index(inplace=True, drop=True)
    return df

def consult_api_price(name, vs_, ut):
    """
    returs a miutely list for the name of the currency with price and utc
    name: strin currency name
    
    vs_: currency name to exchange with
    ut: unix time of twt
    b_a='before' or 'after'
    """
    
    hour_ut = 3600
    num_hours = 72
    interval = hour_ut * num_hours
    
    from_before = int(ut - interval)
    to_before = int(ut)

    from_after = int(ut)
    to_after = int(ut + interval)

    before = cg.get_coin_market_chart_range_by_id(name.lower(), vs_, from_before, to_before)['prices']

    after = cg.get_coin_market_chart_range_by_id(name.lower(), vs_, from_after, to_after)['prices']
    
    price_before = [b[1] for b in before]
    price_after= [a[1] for a in after]

    if not price_before or not price_before  or (len(price_before) < 10) or (len(price_after) < 10):
        return None
    else: 
        return {'before':price_before,'after':price_after}




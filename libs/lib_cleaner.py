import pandas as pd
import re
import lib_ini
import time
import datetime
from lib_current import sub_current

def twcleaner(df, lista_columnas, dict_currency):
    """
    This function takes twwet data frame and return a clean dictionary with every current 
    and its subdata frame
    df: data frame de pandas
    lista de columnas: lista de strings
    dict_currency: dictionary {symbol:name}

    Devuelve df procesado
    """

    df2 = df[lista_columnas]
    df2['MATCHING'] = df2[lista_columnas[0]]

    df2.MATCHING=df2.MATCHING.apply(lambda x: is_a_word(dict_currency, x))
    df2.dropna(subset=['MATCHING'], inplace=True)
    df3 = df2.rename(columns={'created_at':'UT', 'date':'DATE','tweet':'TWEET'}, inplace = False)
    df3.UT=df3.UT.apply(lambda x: round(x/1000))
    return sub_current(df3,dict_currency)

def twt2set(twt):
    """
    This functions takes a string replace a set with all the word only with chars in upper case

    twt: string
    """
    twt_char=(re.findall(r"[a-zA-Z]+", twt))
    tw_char_set={char_.upper() for char_ in twt_char}
    return tw_char_set

def is_a_word(dict_, twt):
    """
    This function returns the set with the currents appearing in twt
    dict_: dictionary of currencies {symbal:name}
    twt:string
    """
    twt_set=twt2set(twt)
    matching= {name for symbol,name  in dict_.items()  if (symbol.upper() in twt_set) or (name.upper() in twt_set) }
    if not matching:
        matching=None
    
    return matching
    


def time2unix(time_string):
    """     
    This function takes a YYYY-MM-DD HH:MM:SS format into unix format

    time string in YYYY-MM-DD HH:MM:SS FORMAT
    """
    return time.mktime(datetime.datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S").timetuple())

def unix_column(df,string_):
    """
    This functions takes a df expecting its column 'string_' is in YYYY-MM-DD HH:MM:SS 
    and turns it into UNIX format

    sf: data frame
    string_: string in YYYY-MM-DD HH:MM:SS format

    """
    df[string_]=df[string_].apply(time2unix)
    return df
    
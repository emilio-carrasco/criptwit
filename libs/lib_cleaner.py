import pandas as pd
import re
import lib_ini
import time
import datetime


def twcleaner(df, lista_columnas, dict_currency):
    """
    Esa función recoge una data frame. De él se quedará con las columnas contenidad en la lista de columnas
    Quedará con las palabras contenidas en la 'lista_palabras'
    Añadirá además tantas columnas como "lista_palabras" con valor booleano para indicar qué palabras aparecen en ese tweet

    df: data frame de pandas
    lista de columnas: lista de strings
    lista de palabras: lista de strings

    Devuelve df procesado
    """

    df2 = df[lista_columnas]
    df2['MATCHING'] = df2[lista_columnas[0]]
    
    df2.MATCHING=df2.MATCHING.apply(lambda x: is_a_word(dict_currency, x))
    df2.dropna(subset=['MATCHING'], inplace=True)
    print(lista_columnas[1])
    df2.sort_values(by=['date'])

    return df2.rename(columns={'created_at':'UT', 'date':'DATE','tweet':'TWEET'}, inplace = False)
   



def is_a_word(dicc, x):
    """
    This function returns the sub list from list appearing in x
    list: list if strings
    x: string
    """
    x1 = (re.findall("[a-zA-Z]+", x))
    x2={element.upper() for element in x1}
 
    matching= {c['name'] for c  in dicc  if (c['symbol'] in x2) or (c['name'] in x2) }

   
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
    
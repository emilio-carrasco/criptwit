import sys
sys.path.append('./libs')

import pandas as pd
pd.options.mode.chained_assignment = None 

from lib_ini import read_batch_csv
from lib_ini import download_dataset

from lib_cleaner import twcleaner

from lib_curren import read_currencies
from lib_curren import currencies_prices

from lib_calc import calculus

from lib_visual import visual_criptwit
from lib_visual import plot_percent
"""
Data set:
https://www.kaggle.com/ayhmrba/elon-musk-tweets-2010-2021
Public domain dataset.
"""


# Downlod, unzip and move DB
print("Downloading DB")
url= 'https://www.kaggle.com/ayhmrba/elon-musk-tweets-2010-2021'
download_dataset(url,'data')
print("- DB ok\n")


# Read csv and merge it all
print("Readin csv.")
df = read_batch_csv(2010, 2021, './data/')
print("-csv ok\n")

#Read currencies from .txt
print("Readin currencies file.")
currencies = read_currencies('./src/currencies_list_symbol_name.txt') 
print("-Currencies file ok\n")

#Clean de data frame
print("Building DF")
df_currencies = twcleaner(df,['tweet','date','created_at'],currencies)
print("-DF ok\n")

#Get prices from the api
print("Consulting API currencies prices")
dict_df_prices = currencies_prices(df_currencies,'eur')
print("-API ok\n")

#Calculate time above before twit price
print("Calculating curves")
dict_df_calculus = calculus(dict_df_prices)
print("-Curves ok\n")

#Bar plot and saving
print("Plotting bars")
plot_percent(dict_df_calculus,'./outputs/')
print("- Plot bar ok\n")

#Curve plot and saving
print("Plotting curves")
visual_criptwit(dict_df_calculus,'./outputs/')
print("-Curves ok\n")

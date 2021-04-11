import pandas as pd
from csv import DictReader

def read_batch_csv(start, end, lib):
    """
    this function reads csv files name XXXX.csv from xxxx=strat to end in the 'lib' folder from actual path
    start,end: 4 digits int
    lib: rlative path
    """
    df = pd.read_csv(lib + str(start) + '.csv')
    for file in range(start + 1, end + 1):
        df_aux = pd.read_csv(lib + str(file) + '.csv')
        df=df.append(df_aux)
    return df



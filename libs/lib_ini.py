import pandas as pd
import os

def download_dataset(url,data):
    '''Downloads a dataset from kaggle and only keeps the csv in your data file. Beware of your own data structure:
    this creates a data directory and also moves all the .csv files next to your jupyter notebooks to it.
    Takes: url from kaggle
    Returns: a folder with the downloaded and unzipped csv
    '''

    #Gets the name of the dataset.zip
    endopint = url.split("/")[-1]
    user = url.split("/")[-2]
    
    #Download, decompress and leaves only the csv
    download = f"kaggle datasets download -d {user}/{endopint}"
    decompress = f"unzip {endopint}.zip"
    delete = f"rm -rf {endopint}.zip"
    make_directory = f"mkdir {data}"
    move_and_delete = f"mv *.csv {data}"
    for i in [download, decompress, delete, make_directory, move_and_delete]:
        os.system(i)
    return 

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



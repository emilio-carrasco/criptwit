import matplotlib.pyplot as plt
import numpy as np

def plot_intervals(before,after,i):
    plt.figure(i)
    
    a0=[a-after[0] for a in after]
    b0=[b-before[0] for b in before]
    plt.plot(a0,color='red')
    plt.plot(b0,color='green')
    return i+1

def visual_currency(df,folder,i):
    (rows_,columns_) = df.shape  
    for r in range(rows_-1): 
        b = df.before[r]
        a = df.after[r]
        i= plot_intervals(b['price'],a['price'],i)

def visual_criptwit(dict_,folder_):
    i=1
    for name, df  in dict_.items():
        if not df.empty:   
            
            plt.xlabel(f"{name}") 
            visual_currency(df, folder_,i)
            

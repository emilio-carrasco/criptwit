import matplotlib.pyplot as plt
import numpy as np

def plot_intervals(before,after):
    before_0=[b-before[0] for b in before]
    after_0=[a-before[0] for a in after]
    
    plt.plot(before_0,color='red')
    plt.plot(after_0,color='green')





def visual_currency(df,folder):
    (rows_,columns_) = df.shape  
    for r in range(rows_-1): 
    

        b=df.before[r]
        a=df.after[r]

        plot_intervals(b['price'],a['price'])


def visual_criptwit(dict_,folder_):
    i = 0
    for name, df  in dict_.items():
        if not df.empty:   
            plt.figure(i)
            plt.xlabel(name) 
            visual_currency(df, folder_)
            i+=1

import matplotlib.pyplot as plt
import numpy as np

def plot_intervals(before,after):
    before_0=[b-before[0] for b in before]
    after_0=[a-after[0] for a in after]

    plt.plot(before)
    plt.plot(after)





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
            visual_currency(df, folder_)
            i+=1

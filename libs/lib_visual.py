import matplotlib.pyplot as plt
import numpy as np
"""
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
"""        
def plot_currency(dict_,j):
    
    before=dict_['before']
    after=dict_['after']
    before0=[b - before[0] for b in before] 
    after0=[a - after[0] for a in after]

    line_before, =plt.plot(before0,color='red', label = "Before twit")
    line_after, =plt.plot(after0,color='green', label = "After twit")
    plt.grid(True)
    plt.legend([line_before, (line_before, line_after)], ["Before twit", "After twit"])

    

    plt.xlabel('72 h before/after')
    plt.ylabel('Price refered to twit moment')
    plt.show()

def visual_criptwit(dict_, folder_):
    j=1
    for name, df  in dict_.items(): 
        if not df.empty: 
                (rows, columns) = df.shape
                for i in range(rows-1):
                    plt.figure(j)
                    plt.title(f"{name} {df.DATE[i]}")
                    plot_currency(df.prices[i],plt)
                    
                    j+=1

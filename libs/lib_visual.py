
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})
plt.rcParams.update({'figure.autolayout': True})

def plot_currency(dict_, plt):
    """
    This function revices a dict whit prices before and after the twit and prints its figure

    dict_: dictionary
s
    plt: figure handler 
    """
    before=dict_['before']
    after=dict_['after']
    before0=[b - before[0] for b in before] 
    after0=[a - after[0] for a in after]

    line_before, =plt.plot(before0,color='C1', label = "Before twit")
    line_after, =plt.plot(after0,color='green', label = "After twit")
    plt.grid(True)
    plt.legend([line_before, (line_before, line_after)], ["Before twit", "After twit"])

    plt.xlabel('72 h before/after')
    plt.ylabel('Price refered to twit moment')
    
def plot_percent(dict_, folder_):
    """
    This function takes a full dictionary with all the currents, plots its bars of time aboce the curve and saves the files for each currency
    dict_: dictionary of currencies
    folder: path to save into

    """
    for name, df  in dict_.items(): 
            if not df.empty: 
                df = df.sort_values(by=['DATE'])    
                labels = list(df.DATE)
                fig, ax = plt.subplots(figsize=[12,8])
                plt.title(f"{name} - % After above before twit")
                plt.xlabel('Date - time of the twitter')
                df.percent_higher.plot.bar()
                plt.axhline(0, color="k")
                ax.set_xticklabels(labels, rotation = 30)
                plt.savefig(f"{folder_}Percent-above-{name}.png", transparent=False)

        

def visual_criptwit(dict_, folder_):
    """
    This function takes a full dictionary with all the currents, plots its price curves and saves the files for each currency
    dict_: dictionary of currencies
    folder: path to save into
    """
    for name, df  in dict_.items():
        if not df.empty: 
            (rows, columns) = df.shape
            for i in range(rows-1):
                plt.figure()
                f, ax = plt.subplots(figsize=[12,8])
                plt.title(f"{name} {df.DATE[i]}")
                plot_currency(df.prices[i],plt)
                plt.savefig(f"{folder_}{name}-{df.DATE[i].strip()}.png", transparent=False)
            

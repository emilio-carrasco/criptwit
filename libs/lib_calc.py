
def calc_percent(price):
    """
    this function returns the calculation of the price cell

    price: dictionary with before and after keys:

    return % after above befor round 1

    """
    before=price['before']
    after=price['after']
    before0=[b - before[0] for b in before] 
    after0=[a - after[0] for a in after]

    list_after_above=[]


    for (before, after) in zip(before0, after0  ):
        list_after_above.append(after>before)
    percent=sum(list_after_above)/len(list_after_above)
    return round(percent*100,1)

def calculus(dict_):
    """
    this function takes a currency dictionary and calculates percentage above and ander the price after/before

    returns a dict with the column 'percent_higher' inclued
    """
    for name, df  in dict_.items():
        if not df.empty: 
            df['percent_higher']=df['prices']
            df.percent_higher=df.percent_higher.apply(calc_percent)
    return dict_
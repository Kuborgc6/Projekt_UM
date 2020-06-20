def Vote(decisions):
    dict = {} 
    count, itm = 0, '' 
    for item in reversed(decisions): 
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count : 
            count, itm = dict[item], item 
    return(itm) 
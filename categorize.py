from forest_vote import forest_vote

def categorize(data, forest):
    length = len(data)
    how_much = 0
    for i in range(length):
        choosen, truth = forest_vote(forest, data[i])    
        if (choosen == truth):
            how_much = how_much+1
    percent = how_much/length
    return percent
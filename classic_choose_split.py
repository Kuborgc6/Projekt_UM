from Question import Question
from info_gain import info_gain
from Question_gain import Question_gain
from partition import partition
import random

def classic_choose_split(data,treshold):
    """Find the best question to ask by iterating over every feature / value
    and calculating the information gain."""
    n_features = len(data[0]) - 1  # number of columns
    quest_gain = [] # keep track of the gains and questions

    for col in range(1,n_features):  # for each feature
        values = set([row[col] for row in data])  # unique values in the column
        for val in values:  # for each value
            question = Question(col, val)
            
            # try splitting the dataset
            true_rows, false_rows = partition(data, question)

            # Skip this split if it doesn't divide the dataset.
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            # Calculate the information gain from this split
            gain = info_gain(data, true_rows, false_rows)
            quest_gain.append(Question_gain(gain,question))

    n_quest_gain = len(quest_gain)

    if n_quest_gain == 0:
        return float('Inf'), float('NaN') #

    ##########

    index = 0
    max_gain = 0
    for x in range(n_quest_gain):
        if (quest_gain[x].gain >= max_gain):
            max_gain = quest_gain[x].gain
            index = x
    
    return quest_gain[index].gain, quest_gain[index].question
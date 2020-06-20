from classify import classify
import numpy as np

def decide(test, tree):
    """Makes decision of what class is the data"""
    decision = classify(test, tree)

    names=[]
    numbers=[]  

    for name,dict_ in decision.items():
        names.append(name)
        numbers.append(dict_)

    index = np.argmax(numbers)
    selected_class = names[index]

    return selected_class
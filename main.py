import pandas as pd
import math
import os
from categorize import categorize
from make_training_data import make_training_data
from build_forest import build_forest

import numpy as np
import matplotlib.pyplot as plt

currentDirectory = os.getcwd()
data_temp = pd.read_csv(currentDirectory+"/Data_for_UCI_named.csv") 
data = data_temp.iloc[:, :].values

classic = 0 # 1 - classic version of building decision tree 0 - my version of building tree
no_trees = 1
size = 5
treshold = 0.3
print(len(data))

#######
training_data = make_training_data(data,no_trees,size)
test = data[(size*no_trees):]
forest = build_forest(training_data,treshold,no_trees, classic)
q = categorize(test, forest)
print (q)


######

notrees_test = [1,2,5,10,15,25,50,100,200,400]
treshold_test = [-0.5,-0.3,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
size_test = [1,2,3,5,10,20,50]

repetition = 5
efficiency = np.empty((len(test_no),repetition))

training_data = make_training_data(data,test_no[-1],size)
test = data[(size*test_no[-1]):]

for index, no_i in enumerate(test_no):
    for x in range(repetition):
        temp_forest = build_forest(training_data,treshold,no_i, classic)
        efficiency[index,x] = categorize(test, temp_forest)
print(efficiency)


fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
ax1.boxplot(efficiency)
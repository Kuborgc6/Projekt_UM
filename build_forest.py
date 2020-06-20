from build_tree import build_tree
from Tree_forest import Tree_forest
from print_tree import print_tree

def build_forest(data_array,treshold,no_trees, classic):
    """Builds the forest.

    Builds "no_trees" trees, which everyone have difrent trening data.
    """
    forest = []

    for x in range(no_trees):
        temp_tree = build_tree(data_array[x].training_data,treshold, classic)# [x].training_data
        forest.append(Tree_forest(temp_tree))
        #print_tree(temp_tree)
    
    return forest
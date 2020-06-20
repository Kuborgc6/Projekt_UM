from choose_split import choose_split
from Leaf import Leaf
from partition import partition
from Decision_Node import Decision_Node
from classic_choose_split import classic_choose_split

def build_tree(data,treshold, classic):
    """Builds the tree."""

    # Try partitioing the dataset on each of the unique attribute,
    # calculate the information gain, and return the question.
    if classic == 1:
        gain, question = classic_choose_split(data, treshold)
    else:    
        gain, question = choose_split(data, treshold)

    # No more questions, so it return a leaf.
    if gain ==  float('Inf'): #
        return Leaf(data)

    true_data, false_data = partition(data, question)

    # Recursively build the true branch.
    true_branch = build_tree(true_data, treshold, classic)

    # Recursively build the false branch.
    false_branch = build_tree(false_data, treshold, classic)

    # Return a Question node.
    return Decision_Node(question, true_branch, false_branch)
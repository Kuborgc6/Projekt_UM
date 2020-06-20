from decide import decide
from Vote import Vote

def forest_vote(forest, data):
    truth = data[-1]
    no_trees = len(forest)
    votes = []
    for x in range(no_trees):
        temp = forest[x]
        temp_tree = temp.inside_tree
        votes.append(decide(data, temp_tree))
    
    decision = Vote(votes)
    return decision, truth
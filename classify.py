from Leaf import Leaf

def classify(test, my_tree):
    """Predicts the class of example."""

    # Base case: we've reached a leaf
    if isinstance(my_tree, Leaf):
        return my_tree.predictions

    # Decide whether to follow the true-branch or the false-branch.
    if my_tree.question.match(test):
        return classify(test, my_tree.true_branch)
    else:
        return classify(test, my_tree.false_branch)
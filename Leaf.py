from class_counts import class_counts

class Leaf:
    """A Leaf node classifies data.

    This holds a dictionary of class -> number of times
    it appears in the rows from the training data that reach this leaf.
    """

    def __init__(self, rows):
        self.predictions = class_counts(rows)
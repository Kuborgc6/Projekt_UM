from Question import Question

class Question_gain:
    """Used to control which questions can be asked."""
    def __init__(self, gain, question):
        self.gain = gain #information gain of question
        self.question = question # which question is asked

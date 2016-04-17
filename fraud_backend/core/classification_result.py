class ClassificationResult(object):

    """This class describes the classification result.

    It basically consists of a label such as
    'FRAUD / NOT_FRAUD' and a value/score that is a
    probability of the predicted label.
    """

    def __init__(self, label = None, score = None):
        """Create a ClassificationResult object.

        :param label: a label 'FRAUD', 'NOT_FRAUD'
        :param score: a probability
        :type label: str
        :type score: float
        """
        self.label = label
        self.score = score

    @property
    def label(self):
        """Get the label."""
        return self.__label

    @label.setter
    def label(self, label):
        """Set the label."""
        self.__label = label

    @property
    def score(self):
        """Get the score."""
        return self.__score

    @score.setter
    def score(self, score):
        """Set the score."""
        self.__score = score

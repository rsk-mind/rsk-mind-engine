class Transaction(object):
    """This class describes a Transaction.

    A Transaction is the most important data source
    and it is expressed as a list of features.
    The characteristics of the Transaction class are described
    bellow.

    """

    def __init__(self):
        """Create a new Transaction object."""

        """The list of features."""
        self.transaction = []
        self.__size = 0


    def add_feature(self, feature):
        """Add a feature to the transaction.

        :param feature: the feature object to be added to a transaction
        """

        self.transaction.append(feature)
        self.__size += 1


    def get_feature(self, index):
        """Get a feature from transaction.

        :param index: the index of the feature object to be retrieved
        :returns: a feature
        :rtype: Feature
        """

        if index >= 0 and index < self.__size:
            return self.transaction[index]


    def number_of_features(self):
        """Get the number of features.

        :returns: the number of features of a transaction
        :rtype: int
        """
        return self.__size

    def __repr__(self):
        """Represent a Transaction as a string."""

        result = ""
        for index in range(0, self.__size):
            result += str(self.transaction[index])+"\n"
        result += "Size: {}".format(self.__size)

        return result

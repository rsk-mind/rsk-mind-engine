class Insight(object):

    """This class describes an insight.

    An insight may be a statistical metric
    calculated from a transaction or any other
    information about the transaction that is
    considered to be important.

    """


    def __init__(self, description = None,
                 name = None, value = None):
        """Create a new Insight object.

        :param description: a text description of the insight
        :param name: name of the insight
        :param value: value of insight

        """

        self.description = description
        self.name = name
        self.value = value


    @property
    def description(self):
        """Return the insight's description."""
        return self.__description

    @description.setter
    def description(self, description):
        """Set insight's description."""
        self.__description = description


    @property
    def name(self):
        """Return the insight's name."""
        return self.__name

    @name.setter
    def name(self, name):
        """Set insight's name."""
        self.__name = name


    @property
    def value(self):
        """Return the insight's value."""
        return self.__value

    @value.setter
    def value(self, value):
        """Set insight's value."""
        self.__value = value


    def __repr__(self):
        """Represent an insight as a string."""
        return "Description: {}, Name: {}, Value: {}".format(
            self.description, self.name, self.value
        )

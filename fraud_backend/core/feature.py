class Feature(object):
    """This class describes a feature.

    A Feature is essentially an attribute of a more
    concrete data collection that is called Transaction.
    The characteristics of the Feature class are described
    bellow.

    """

    def __init__(self, description = None, kind = None,
                 name = None, value = None, position = None):
        """Create a new Feature object.

        :param description: a text description of feature
        :param kind: type of a feature  e.g. numerical
        :param name: name of feature
        :param value: value of feature
        :param position: position of feature inside a transaction

        """

        self.description = description
        self.kind = kind
        self.name = name
        self.value = value
        self.position = position


    @property
    def description(self):
        """Return the feature's description."""
        return self.__description

    @description.setter
    def description(self, description):
        """Set feature's description."""
        self.__description = description


    @property
    def kind(self):
        """Return the feature's type."""
        return self.__kind

    @kind.setter
    def kind(self, kind):
        """Set feature's type."""
        self.__kind = kind


    @property
    def name(self):
        """Return the feature's name."""
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def value(self):
        """Return the feature's value."""
        return self.__value

    @value.setter
    def value(self, value):
        """Set feature's value."""
        self.__value = value


    @property
    def position(self):
        """Return the feature's order."""
        return self.__position

    @position.setter
    def position(self, position):
        """Set feature's order."""
        self.__position = position

    def __repr__(self):
        """Represent a feature as a string."""
        return "Description: {}, Type: {}, Name: {}, Value: {}, Order: {}".format(
            self.description, self.kind, self.name, self.value, self.position
        )

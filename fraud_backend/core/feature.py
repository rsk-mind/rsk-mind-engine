from .feature_type import FeatureType

class Feature(object):
    """This class describes a feature.

    A Feature is essentially an attribute of a more
    concrete data collection that is called Transaction.
    The characteristics of the Feature class are described
    bellow.

    """

    def __init__(self, description = None, kind = None,
                 name = None, value = None, position = None,
                 is_target = None):
        """Create a new Feature object.

        :param description: a text description of feature
        :param kind: type of a feature  e.g. numerical
        :param name: name of feature
        :param value: value of feature
        :param position: position of feature inside a transaction
        :param is_target: shows if feature is target variable or predictor
        :type description: str
        :type kind: int
        :type name: str
        :type value: float
        :type position: int
        :type is_target: bool
        """

        self.description = description
        self.kind = kind
        self.name = name
        self.value = value
        self.position = position
        self.is_target = is_target


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
        if kind in FeatureType.types.keys():
            self.__kind = kind
        else:
            self.kind = FeatureType.BINARY


    @property
    def name(self):
        """Return the feature's name."""
        return self.__name

    @name.setter
    def name(self, name):
        """Set feature's name."""
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


    @property
    def is_target(self):
        """Return true if feature is a target variable."""
        return self.__is_target

    @is_target.setter
    def is_target(self, is_target):
        """Set feature's state."""
        self.__is_target = is_target

    def __repr__(self):
        """Represent a feature as a string."""
        return "Description: {}, Type: {}, Name: {}, Value: {}, Order: {}, Target Variable: {}".format(
            self.description, FeatureType.types[self.kind],
            self.name, self.value, self.position, self.is_target
        )

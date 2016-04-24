class FeatureType(object):

    """ This class represents the type of a feature.

    Several types exist but the basic types are
    BINARY e.g 0/1 BOY/GIRL, NUMERICAL  are real
    values meaning variables that can be measured
    e.g 15.87 USD and CATEGORICAL are variables
    that are enumerable e.g colors.
    """

    BINARY = 1
    NUMERICAL = 2
    CATEGORICAL = 3

    types = {
        BINARY: "BINARY",
        NUMERICAL: "NUMERICAL",
        CATEGORICAL: "CATEGORICAL"
    }

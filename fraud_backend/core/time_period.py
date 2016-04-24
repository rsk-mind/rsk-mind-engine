class TimePeriod(object):

    """ This class represents the periods of day.

    Possible values are MORNING, AFTERNOON,
    EVENING, NIGHT.
    """

    MORNING = 1
    AFTERNOON = 2
    EVENING = 3
    NIGHT = 4

    NUM_TO_STR = {
        MORNING: "MORNING",
        AFTERNOON: "AFTERNOON",
        EVENING: "EVENING",
        NIGHT: "NIGHT"
    }

    STR_TO_NUM = {
        "MORNING": MORNING,
        "AFTERNOON": AFTERNOON,
        "EVENING": EVENING,
        "NIGHT": NIGHT
    }

    MORNING_RANGE = xrange(5, 12)
    AFTERNOON_RANGE = xrange(12, 17)
    EVENING_RANGE = xrange(17, 22)

    @classmethod
    def time_period_from_hour(cls, hour):
        """ Returns a time period.

        Given an hour of the day it returns
        the appropriate time period.
        """
        if hour in cls.MORNING_RANGE:
            return cls.MORNING
        elif hour in cls.AFTERNOON_RANGE:
            return cls.AFTERNOON
        elif hour in cls.EVENING_RANGE:
            return cls.AFTERNOON
        else:
            return cls.NIGHT

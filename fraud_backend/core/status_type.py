class StatusType(object):

    """ This class represents the status of a transaction.

    Possible values are DRAFT, APPROVED, PAUSED,
    CANCELLED, COMPLETED.
    """

    DRAFT = 1
    APPROVED = 2
    PAUSED = 3
    CANCELLED = 4
    COMPLETED = 5

    NUM_TO_STR = {
        DRAFT: "DRAFT",
        APPROVED: "APPROVED",
        PAUSED: "PAUSED",
        CANCELLED: "CANCELLED",
        COMPLETED: "COMPLETED"
    }

    STR_TO_NUM = {
        "DRAFT": DRAFT,
        "APPROVED": APPROVED,
        "PAUSED": PAUSED,
        "CANCELLED": CANCELLED,
        "COMPLETED": COMPLETED
    }

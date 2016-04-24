class StatusType(object):

    """ This class represents the status of a transaction.

    Possible values are DRAFT, APPROVED, PAUSED,
    CANCELLED, COMPLETED.
    """

    DRAFT = 0
    APPROVED = 1
    PAUSED = 2
    CANCELLED = 3
    COMPLETED = 4

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

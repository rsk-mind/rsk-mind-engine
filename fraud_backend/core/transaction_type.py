class TransactionType(object):

    """This class represents a transaction type.

    We follow paypals example described here:
    https://www.paypalobjects.com/en_US/vhelp/paypalmanager_help/transaction_type_codes.htm
    """

    S = 1
    C = 2
    A = 3
    D = 4
    V = 5
    F = 6
    P = 7

    NUM_TO_STR = {
        S: "S",
        C: "C",
        A: "A",
        D: "D",
        V: "V",
        F: "F",
        P: "P"
    }

    STR_TO_NUM = {
        "S": S,
        "C": C,
        "A": A,
        "D": D,
        "V": V,
        "F": F,
        "P": P
    }

class RandomGenerator(object):

    """Random generator class.

    This class can be used to generate
    random transaction data either annotated
    or not.
    """

    def __init__(self, total=100, labeled=True, fraud_n=2):
        """Create a RandomGenerator object.

            :param total: total number of transactions
            :param labeled: declares if transactions will be labeled
            :param fraud_n: number of transactions that will be labeled as fraud
            :type total: int
            :param labeled: bool
            :param fraud_n: int
        """
        self.total = total
        self.labeled = labeled
        self.fraud_n = fraud_n

    def generate_data(self):
        #TODO implement later
        if not labeled:
        else:
        pass

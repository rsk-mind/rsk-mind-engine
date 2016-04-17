class FraudScoreEngine(object):

    """ Fraud Score Engine.

    This class is an abstract class that
    will be subclassed for important ML
    algorithms.
    """

    def train():
        """Train a model."""
        raise NotImplementedError("Subclasses must implement train()")

    def test():
        """ Test the model against a test data set."""
        raise NotImplementedError("Subclasses must implement test()")

    def validate(thresshold):
        """Validate the model.

        :param thresshold: the thresshold to be set
        :type thresshold: float
        """
        raise NotImplementedError("Subclasses must implement validate()")

    def classify(transaction_instance):
        """Classify a transaction as fraud or not.

        :param transaction_instance: the instance to be clasified
        :type transaction_instance: Transaction
        """
        raise NotImplementedError("Subclasses must implement classify()")

    def set_training_data(self, training_data):
        """Set the training data set.

        :param training_data: the set of transactions to use for training.
        :type training_data: list of Transaction
        """
        raise NotImplementedError("Subclasses must implement set_training_data()")

    def set_test_data(self, test_data):
        """Set the test data set.

        :param test_data: the set of transactions to use for testing.
        :type test_data: list of Transaction
        """
        raise NotImplementedError("Subclasses must implement set_test_data()")


import numpy as np
from ..basic_features_config import basic_features_list
# from basic_features_config import basic_features_list
from .feature import Feature
from .transaction import Transaction

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
        data = []
        # from config get number of predictor values
        num_predictors = len(basic_features_list)-1
        # generate data in noth cases
        # row_data = np.random.rand(self.total, num_predictors)
        for tr_index in xrange(0, self.total):
            # for every transaction
            t = Transaction()
            for feat_index in xrange(0, num_predictors):
                # for every predictor feature
                f = Feature()
                f.description = basic_features_list[feat_index]['description']
                f.kind = basic_features_list[feat_index]['kind']
                f.name = basic_features_list[feat_index]['name']
                f.position = basic_features_list[feat_index]['position']
                f.is_target = basic_features_list[feat_index]['is_target']
                # set value
                if f.kind == 1: # BINARY
                    f.value = np.random.randint(2, size=1)
                elif f.kind == 2: # NUMERICAL
                    f.value = np.random.rand()*1000
                elif f.kind == 3: #CATEGORICAL
                    min = 1
                    max = 5
                    f.value = (np.random.rand() * (max - min) ) + min
                t.add_feature(f)
            data.append(t)

        return data

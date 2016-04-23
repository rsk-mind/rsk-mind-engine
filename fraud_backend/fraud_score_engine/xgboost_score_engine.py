import xgboost as xgb
import numpy as np
from .fraud_score_engine import FraudScoreEngine
from ..core.classification_result import ClassificationResult

class XgboostScoreEngine(FraudScoreEngine):

    def __init__(self):
        # default parameters
        self.params = {
            'eta': 0.15,
            'objective': 'binary:logistic',
            'max_depth': 5,
            'subsample': 0.5,
            'eval_metric': 'auc',
            'silent': 1,
        }
        # default number of rounds
        self.num_rounds = 300
        self.training_data = []
        self.training_numpy_data = None
        self.training_numpy_labels = None
        self.trained_model = None
        self.test_data = []

    def set_training_data(self, training_data):
        self.training_data = training_data
        data = []
        labels = []
        for tr in training_data:
            # get predictors
            predictors_values = tr.get_predictors_values()
            data.append(np.array(predictors_values))
            # get target
            target_value = tr.get_target_value()
            labels.append(target_value)
        # transform data to numpy format
        self.training_numpy_data = np.array(data)
        # transform labels to numpy array
        self.training_numpy_labels = np.array(labels)

    def set_test_data(self, test_data):
        self.test_data = test_data

    def train(self):
        # DMatrix
        dtrain = xgb.DMatrix(self.training_numpy_data, self.training_numpy_labels)
        # train model
        self.trained_model = xgb.train(self.params, dtrain, self.num_rounds)

    def classify(self, transaction_instance):
        """Classify an unlabeled transaction."""
        predictors = transaction_instance.get_predictors_values()
        predictors_numpy = np.array(predictors)
        predictors_dmatrix = xgb.DMatrix(predictors_numpy)
        fraud_score = self.trained_model.predict(predictors_dmatrix)
        result = ClassificationResult('SUSPICIOUS', fraud_score)
        return result

    def test(self):
        pass

    def validate(self, thresshold):
        pass

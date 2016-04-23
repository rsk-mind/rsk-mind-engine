from ..transformation_engine import Transformation
from ..fraud_score_engine import XgboostScoreEngine


class Api(object):

    """Api interface for the backend."""
    def __init__(self):
        self.xgb_score_engine = XgboostScoreEngine()

    def train(self, transactions, algorithm="XGBOOST"):
        """Train a model from a list of dictionaries."""
        if algorithm == "XGBOOST":
            transformed_transactions = Transformation.transform(transactions)
            self.xgb_score_engine.set_training_data(transformed_transactions)
            self.xgb_score_engine.train()
        return {"STATUS": "OK"}

    def classify_transaction(self, transaction):
        """Classify a transaction/dictionary."""
        transformed_transaction = Transformation.transform_row(transaction)
        result = self.xgb_score_engine.classify(transformed_transaction)
        return {result.label: result.score}

    def transform_transaction(self, transaction):
        """ Transaction is a dictionary."""
        transformed = Transformation.transform_row(transaction)
        return transformed.to_json()

    def transform_transactions(self, transactions):
        """ Transform a list of dictionaries."""
        response = []
        for tr in transactions:
            transformed = self.transform_transaction(tr)
            response.append(transformed)
        return response

    def insights(self):
        """Unclear for now."""
        pass

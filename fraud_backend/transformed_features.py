transformed_features_list = [

    {'description': "Status of transaction",
     'kind': 3,
     'name': "STATUS",
     'position': 0,
     'is_target': False
    },

    {'description': "Matching ips",
     'kind': 1,
     'name': "MATCHING_IPS",
     'position': 1,
     'is_target': False
    },

    {'description': "Type of transaction (see https://www.paypalobjects.com/en_US/vhelp/paypalmanager_help/transaction_type_codes.htm)",
     'kind': 3,
     'name': "TRANSACTION_TYPE",
     'position': 2,
     'is_target': False
    },

    {'description': "Check if the description of the transaction is empty",
     'kind': 1,
     'name': "EMPTY_DESCRIPTION",
     'position': 3,
     'is_target': False
    },

    {'description': "Time period of posted transaction (MORNING, AFTERNOON, NIGHT)",
     'kind': 3,
     'name': "POSTED_TIME_PERIOD",
     'position': 4,
     'is_target': False
    },

    {'description': "Time period the transaction was completed",
     'kind': 3,
     'name': "COMPLETED_TIME_PERIOD",
     'position': 5,
     'is_target': False
    },

    {'description': "The balance in user's account",
     'kind': 2,
     'name': "BALANCE",
     'position': 6,
     'is_target': False
    },

    {'description': "The amount engaged in the transaction",
     'kind': 2,
     'name': "AMOUNT",
     'position': 7,
     'is_target': False
    },

    {'description': "This is the predicted label 0/1 NOT_FRAUD/FRAUD",
     'kind': 1,
     'name': "FRAUD",
     'position': 8,
     'is_target': True
    },
]

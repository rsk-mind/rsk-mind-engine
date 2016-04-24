original_features_list = [

    {'description': "Source account IBAN",
     'name': "SRC_ACCOUNT_IBAN",
     'position': 0,
     'is_target': False
    },

    {'description': "Destination account IBAN",
     'name': "DST_ACCOUNT_IBAN",
     'position': 1,
     'is_target': False
    },

    {'description': "Status of transaction (DRAFT, APPROVED, PAUSED, CANCELLED, COMPLETED)",
     'name': "STATUS",
     'position': 2,
     'is_target': False
    },


    {'description': "Posted by ip address",
     'name': "POSTED_BY_IP_ADDRESS",
     'position': 3,
     'is_target': False
    },


    {'description': "Approved by ip address",
     'name': "APPROVED_BY_IP_ADDRESS",
     'position': 4,
     'is_target': False
    },

    {'description': "Paused by ip address",
     'name': "PAUSED_BY_IP_ADDRESS",
     'position': 5,
     'is_target': False
    },

    {'description': "Cancelled by ip address",
     'name': "CANCELLED_BY_IP_ADDRESS",
     'position': 6,
     'is_target': False
    },


    {'description': "Type of transaction (see https://www.paypalobjects.com/en_US/vhelp/paypalmanager_help/transaction_type_codes.htm)",
     'name': "TRANSACTION_TYPE",
     'position': 7,
     'is_target': False
    },

    {'description': "A short description of what happened in the transaction",
     'name': "DESCRIPTION",
     'position': 8,
     'is_target': False
    },


    {'description': "When was the transaction posted (UTC datetime)",
     'name': "POSTED",
     'position': 9,
     'is_target': False
    },


    {'description': "When was the transaction completed (UTC datetime)",
     'name': "COMPLETED",
     'position': 10,
     'is_target': False
    },


    {'description': "The balance in user's account",
     'name': "BALANCE",
     'position': 11,
     'is_target': False
    },

    {'description': "The amount spent in the transaction",
     'name': "AMOUNT",
     'position': 12,
     'is_target': False
    },


    {'description': "This is the predicted label 0/1 NOT_FRAUD/FRAUD",
     'kind': 1,
     'name': "FRAUD",
     'position': 13,
     'is_target': True
    },
]

basic_features_list = [

    {description: "Transaction was made behind a proxy or not",
     kind: 1,
     name: "PROXY_DETECTED",
     position: 0,
     is_target: False
    },

    {description: "Transaction was made from computer in TOR Network",
     kind: 1,
     name: "TOR_NODE",
     position: 1,
     is_target: False
    },

    {description: "Time period of transaction (MORNING, AFTERNOON, NIGHT)",
     kind: 3,
     name: "TIME_PERIOD",
     position: 2,
     is_target: False
    },

    {description: "The amount spent in the transaction",
     kind: 2,
     name: "AMOUNT_SPENT",
     position: 3,
     is_target: False
    },

    {description: "The current balance in user's account",
     kind: 2,
     name: "CURRENT_BALANCE",
     position: 4,
     is_target: False
    },

    {description: "User works or is unemployed",
     kind: 1,
     name: "UNEMPLOYED",
     position: 5,
     is_target: False
    },

    {description: "User is male or female",
     kind: 1,
     name: "MALE",
     position: 6,
     is_target: False
    },

    {description: "The age of the user",
     kind: 2,
     name: "USER_AGE",
     position: 7,
     is_target: False
    },

    {description: "This is the predicted label 0/1 NOT_FRAUD/FRAUD",
     kind: 1,
     name: "FRAUD",
     position: 8,
     is_target: True
    },
]

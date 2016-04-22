from .status_type import StatusType
from .geoip_country_wrapper import GeoipCountryWrapper
from .transaction_type import TransactionType
from .time_period import TimePeriod
from .feature import Feature
from .transaction import Transaction
import datetime

class Transformation(object):

    """ This is the transformation class.

    It transforms an original transaction row
    to a specific format in order to feed the
    classifiers.
    """

    def __init__(self):
        pass

    def transform_row(self, transaction_row):
        """Transform a row.

        :param transaction_row: a transaction as a python dictionary
        """
        # row is a dictionary
        transformed = Transaction()

        # iso code source iban
        # transaction_row['src_iban_iso']

        # iso code destination iban
        # transaction_row['dst_iban_iso']

        # skip ibans index: [0, 1]

        # status index: 2
        status = transaction_row['status']
        new_status = StatusType.STR_TO_NUM[status]
        status_feature = Feature(name='STATUS', position=2, value=new_status, is_target=False)
        transformed.add_feature(status_feature)

        # geoipwrapper
        gw = GeoipCountryWrapper()

        ips = []
        # posted by ip address
        posted_ip = transaction_row['posted_by_ip_address']
        # new_posted_gid = gw.geoname_id(posted_ip)
        ips.append(posted_ip)

        # approved by ip address
        approved_ip = transaction_row['approved_by_ip_address']
        # new_approved_gid = gw.geoname_id(approved_ip)
        ips.append(approved_ip)

        # paused by ip address
        paused_ip = transaction_row['paused_by_ip_address']
        # new_paused_gid = gw.geoname_id(paused_ip)
        ips.append(paused_ip)

        # cancelled by ip address
        cancelled_ip = transaction_row['cancelled_by_ip_address']
        # new_cancelled_gid = gw.geoname_id(cancelled_ip)
        ips.append(cancelled_ip)

        matching_ips_feature = Feature(name='MATCHING_IPS', position=3,
        value=matching_ips(ips), is_target=False)
        transformed.add_feature(matching_ips_feature)

        # transaction type
        transaction_type =  transaction_row['transaction_type']
        new_transaction_type = TransactionType.STR_TO_NUM[transaction_type]
        new_tr_type_feature = Feature(name='TRANSACTION_TYPE', position=4,
        value=new_tr_type_feature, is_target=False)
        transformed.add_feature(new_tr_type_feature)

        # description
        descrpiption = transaction_row['description']
        empty_description = 1 if len(a) == 0 else 0
        emp_descr_feature = Feature(name='EMPTY_DESCRIPTION', position=5,
        value=emp_descr_feature, is_target=False)
        transformed.add_feature(emp_descr_feature)

        fmt = "%Y-%m-%dT%H:%M:%SZ"
        # posted transaction timestamp

        posted = transaction_row['posted']
        posted_datetime = datetime.datetime.strptime(posted, fmt)
        posted_time_period = TimePeriod.time_period_from_hour(posted_datetime.hour)
        posted_time_per_feature = Feature(name='POSTED_TIME_PERIOD', position=6,
        value=posted_time_per_feature, is_target=False)
        transformed.add_feature(posted_time_per_feature)

        # completed transaction timestamp
        completed = transaction_row['completed']
        completed_datetime = datetime.datetime.strptime(completed, fmt)
        completed_time_period = TimePeriod.time_period_from_hour(completed_datetime.hour)
        completed_time_per_feature = Feature(name='COMPLETED_TIME_PERIOD', position=7,
        value=completed_time_per_feature, is_target=False)
        transformed.add_feature(completed_time_per_feature)

        # balance
        balance = transaction_row['balance']
        balance_feature = Feature(name='BALANCE', position=8,
        value=balance, is_target=False)
        transformed.add_feature(balance_feature)

        # amount
        amount = transaction_row['amount']
        amount_feature = Feature(name='AMOUNT', position=9,
        value=amount, is_target=False)
        transformed.add_feature(amount_feature)

        return transformed

    def transform(self, transactions):
        """Transform a list of transactions."""
        transformed_transactions = []

        for transaction in transactions:
            transformed_transactions.append(transaction)

        return transformed_transactions

    def matching_ips(ips):
        match = ps[1:] == ips[:-1]
        1 if match else 0

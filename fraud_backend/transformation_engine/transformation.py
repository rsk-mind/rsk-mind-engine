from ..core.status_type import StatusType
from ..core.geoip_country_wrapper import GeoipCountryWrapper
from ..core.transaction_type import TransactionType
from ..core.time_period import TimePeriod
from ..core.feature import Feature
from ..core.transaction import Transaction
from ..iso_codes import geoname
from ..iban_decode import decode
import datetime

class Transformation(object):

    """ This is the transformation class.

    It transforms an original transaction row
    to a specific format in order to feed the
    classifiers.
    """

    @classmethod
    def transform_row(cls, transaction_row):
        """Transform a row.

        :param transaction_row: a transaction as a python dictionary
        """
        # row is a dictionary
        transformed = Transaction()

        # source iban
        src_geonameid = int(decode(transaction_row['src_account_iban'])[1])
        src_geonameid_feature = Feature(name='SRC_GEONAME_ID', position=0, value=src_geonameid, is_target=False)
        transformed.add_feature(src_geonameid_feature)

        # iso code destination iban
        # transaction_row['dst_iban_iso']
        dst_geonameid = int(decode(transaction_row['dst_account_iban'])[1])
        dst_geonameid_feature = Feature(name='DST_GEONAME_ID', position=1, value=dst_geonameid, is_target=False)
        transformed.add_feature(dst_geonameid_feature)

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

        # target/class/outcome
        if transaction_row.has_key('outcome'):
            target = 1 if transaction_row['outcome']==True else 0
            target_feature = Feature(name='TARGET', position=10,
            value=target, is_target=True)
            transformed.add_feature('target_feature')

        return transformed

    @classmethod
    def transform(cls, transactions):
        """Transform a list of transactions."""
        transformed_transactions = []

        for transaction in transactions:
            transformed_transactions.append(transaction)

        return transformed_transactions

    @classmethod
    def matching_ips(cls, ips):
        match = 1 if (ips[1:] == ips[:-1]) else 0
        return match

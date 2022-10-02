from .payments import Payment
from .payouts import Payout


class Client:

    def __init__(self):
        pass

    @staticmethod
    def payment(payment_key: str, merchant_uuid: str) -> Payment:
        """
        :param str payment_key: Api Key from merchant settings
        :param str merchant_uuid: Merchant ID
        :return class Payment
        """

        return Payment(payment_key, merchant_uuid)

    @staticmethod
    def payout(payout_key: str, merchant_uuid: str) -> Payout:
        """
        :param str payout_key:
        :param str merchant_uuid:
        :return Payout:
        """

        return Payout(payout_key, merchant_uuid)

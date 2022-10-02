from .request_builder import RequestBuilder


class Payout:

    def __init__(self, payout_key: str, merchant_uuid: str):
        self.payment_key = payout_key
        self.merchant_uuid = merchant_uuid
        self.version = 'v1'
        self.request_builder = RequestBuilder(payout_key, merchant_uuid)

    def create(self, data):
        """
        :param dict data:
                        str amount: Amount to payout
                        str currency: Currency
                        str network: Network
                        str order_id: Your id
                        str address: Wallet number
                        str is_subtract: From where to withdraw the commission (1 - from the balance, 0 - from the amount)
                        str url_callback: Callback link
        :return Optional(bool):
        :raise RequestBuilderException
        """

        uri = self.version + '/payout'
        return self.request_builder.send_request(uri, data)

    def info(self, data):
        """
        :param data:
                    str uuid
        :return Optional(bool):
        :raise RequestBuilderException
        """

        uri = self.version + '/payout/info'
        return self.request_builder.send_request(uri, data)

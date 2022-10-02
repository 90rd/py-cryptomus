from .request_builder import RequestBuilder


class Payment:

    def __init__(self, payment_key: str, merchant_uuid: str):
        self.payment_key = payment_key
        self.merchant_uuid = merchant_uuid
        self.version = 'v1'
        self.requestBuilder = RequestBuilder(payment_key, merchant_uuid)

    def create(self, data: dict):
        """
        :param dict data:
                         str amount: Amount to pay
                         str currency: Payment currency
                         str network: Payment network
                         str order_id: Order ID in your system
                         str url_return: Redirect link
                         str url_callback: Callback link
                         bool is_payment_multiple: Allow surcharges on payment *
                         str lifetime: Payment lifetime in seconds
                         str to_currency: Currency to convert amount to
        :return Optional(bool):
        :raise RequestBuilderException
        """

        uri = self.version + '/payment'
        return self.requestBuilder.send_request(uri, data)

    def info(self, data: dict):
        """
        :param data:
                    str uuid: Transaction uuid
                    str order_id: Order id
        :return : request answer in JSON format
        """

        uri = self.version + '/payment/info'
        return self.requestBuilder.send_request(uri, data)

    def history(self, page: int = 1, **parameters):
        """
        :param int page: Pagination cursor
        :param dict parameters: Additional parameters
        :return json : request answer in JSON format
        :raise RequestBuilderException
        """
        if parameters is None:
            parameters = {}

        uri = self.version + '/payment/list'
        parameters['cursor'] = str(page)

        return self.requestBuilder.send_request(uri, data=parameters)

    def services(self, **parameters):
        """
        :param dict parameters: Additional parameters
        :return request answer in JSON format
        :raise RequestBuilderException
        """
        if parameters is None:
            paramenters = {}

        uri = self.version + '/payment/services'
        return self.requestBuilder.send_request(uri, parameters)

    def balance(self, **parameters):
        """
        :param parameters:
        :return json balance:
        :raise RequestBuilderException
        """
        if parameters is None:
            parameters = {}

        uri = self.version + '/balance'
        return self.requestBuilder.send_request(uri, parameters)

    def resend_notification(self, data: dict):
        """
        :param dict data:
                        str uuid: Payment's UUID
                        str order_id: Order ID in your system
        :return Optional bool
        :raise RequestBuilderException
        """
        uri = self.version + '/payment/resend'
        return self.requestBuilder.send_request(uri, data)

    def create_wallet(self, data: dict):
        """
        :param dict data:
                        str network: Network
                        str currency: Payment currency
                        str order_id: Order ID in your system
                        str url_callback: Callback url
        :return Optional(bool): returns Bool or mixed data
        :raise RequestBuilderException
        """
        uri = self.version + '/wallet'
        return self.requestBuilder.send_request(uri, data)








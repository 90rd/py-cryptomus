class RequestExceptionsBuilder(Exception):

    def __init__(self, message: str, response_code: int, uri: str, errors: list = None):
        """
        :param str message:
        :param int response_code:
        :param str uri:
        :param errors:
        :return Exception
        """

        self.method = uri
        self.errors = errors if errors else []
        super(RequestExceptionsBuilder, self).__init__(message, response_code)

    def get_method(self):
        return self.method

    def get_errors(self):
        return self.errors

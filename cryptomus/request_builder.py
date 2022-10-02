import requests
import json
import hashlib
import base64
from .request_exceptions import RequestExceptionsBuilder


class RequestBuilder:

    def __init__(self, secret_key: str, merchant_uuid: str):
        """
        :param str secret_key:
        :param str merchant_uuid:
        :param
        """
        self.api_url = 'https://api.cryptomus.com/'
        self.secret_key = secret_key
        self.merchant_uuid = merchant_uuid

    def send_request(self, uri: str, data: dict):
        """
        :param str uri: uri is the piece of link added to main Api Url to make strict request
        :param dict data: body data of request
        :return JSON result:
        """

        url = self.api_url + uri

        json_body_data = json.dumps(data, separators=(',', ':'))
        json_body_data_binary = json_body_data.encode('utf-8')

        encoded_data = base64.b64encode(json_body_data_binary)
        sign_md5_obj = hashlib.md5(encoded_data + self.secret_key.encode('utf-8'))
        sign = sign_md5_obj.hexdigest()

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json;charset=UTF-8",
            "Content-Legth": str(len(json_body_data)),
            "merchant": self.merchant_uuid,
            "sign": sign
        }

        try:
            response = requests.post(url=url, headers=headers, data=json_body_data)
        except Exception as e:
            raise RequestExceptionsBuilder('Problems with requests library', response_code=0, uri=uri, errors=[e])

        response_code = response.status_code

        try:
            response_json = response.json()
        except Exception as e:
            raise RequestExceptionsBuilder(str(e), response_code=response_code, uri=uri)

        if response_json:
            if response_code != 200 or (response_json['state'] is not None and response_json['state'] != 0):
                if 'message' in response_json:
                    raise RequestExceptionsBuilder(response_json['message'], response_code, uri)
                if 'errors' in response_json:
                    raise RequestExceptionsBuilder('Validation error', response_code, uri,
                                                   errors=response_json['errors'])

            if 'result' in response_json and response_json['state'] is not None and response_json['state'] == 0:
                return response_json['result']

        return True

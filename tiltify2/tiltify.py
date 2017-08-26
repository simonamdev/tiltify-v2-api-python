import json
import requests

from enum import Enum
from tiltify2.exceptions import RequestException, InvalidApiKeyException


class Tiltify2:
    api_url = 'https://tiltify.com/api_test/v2/'
    campaign_url = '{}campaign/'.format(api_url)
    donations_url = '{}donations'.format(campaign_url)
    rewards_url = '{}rewards'.format(campaign_url)

    def __init__(self, api_key, timeout=2):
        self._api_key = api_key
        self.__timeout = timeout
        self.__validate_api_key()

    def __validate_api_key(self):
        if not isinstance(self._api_key, str):
            raise ValueError('API Key must be a string')
        if not len(self._api_key) == 32:
            raise ValueError('Invalid API Key length of {}. API key must be 32 characters long'.format(len(self._api_key)))

    def get_donations(self, limit=None, order_by=None, donation_order=None):
        params = {}
        if params is not None:
            if limit is not None:
                params['donation_limit'] = limit
            if order_by is not None:
                param_values = {
                    Order.AMOUNT: 'amount',
                    Order.CREATED_AT: 'created'
                }
                params['donation_order_by'] = param_values[order_by]
            if donation_order is not None:
                params['donation_order'] = 'desc' if donation_order == Order.DESC else 'asc'
        data = self.__make_request(url=self.donations_url, params=params)
        return data

    def __make_request(self, url, params=None):
        response = requests.get(
            url=url,
            params=params if params is not None else {},
            headers=self.__get_request_headers(),
            timeout=self.__timeout
        )
        if response.status_code == 401:
            raise InvalidApiKeyException('Tiltify rejected the given API key: {}'.format(self._api_key))
        if not response.status_code == 200:
            raise RequestException('Unable to reach Tiltify API. Returned status code: {}'.format(response.status_code))
        return json.loads(response.text)

    def __get_request_headers(self):
        return {'Authorization': 'Token token={}'.format(self._api_key)}


class Order(Enum):
    ASC = 1
    DESC = 2
    AMOUNT = 'amount'
    CREATED_AT = 'created'

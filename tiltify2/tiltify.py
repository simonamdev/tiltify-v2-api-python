class Tiltify2:
    def __init__(self, api_key):
        self._api_key = api_key
        self.__validate_api_key()

    def __validate_api_key(self):
        if not isinstance(self._api_key, str):
            raise ValueError('API Key must be a string')
        if not len(self._api_key) == 32:
            raise ValueError('Invalid API Key length of {}. API key must be 32 characters long'.format(len(self._api_key)))



class Api(object):
    BASE_URL = "http://api.thenounproject.com"

    def __init__(self, api_key, secret_key, **kwargs):
        self.base_url = self.BASE_URL
        self.api_key = api_key
        self.secret_key = secret_key

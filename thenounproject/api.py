from thenounproject.collection import Collection
from thenounproject.enterprise import Enterprise
from thenounproject.icon import Icon
from thenounproject.usage import Usage
from thenounproject.user import User


class Api(object):
    BASE_URL = "http://api.thenounproject.com"

    def __init__(self, api_key, secret_key, **kwargs):
        self.base_url = self.BASE_URL
        self.api_key = api_key
        self.secret_key = secret_key

    @property
    def collection(self):
        return Collection(api=self)

    @property
    def icon(self):
        return Icon(api=self)

    @property
    def usage(self):
        return Usage(api=self)

    @property
    def user(self):
        return User(api=self)

    @property
    def enterprise(self):
        return Enterprise(api=self)

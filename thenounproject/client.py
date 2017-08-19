import json
import requests

from requests_oauthlib import OAuth1

from thenounproject.expections import TheNounProjectException, ConnectionError


class Client(object):
    """
    The NounProject Client

    HTTP connections to and communication with the The NounProject API.
    """

    def __init__(self, api, **kwargs):
        self.api = api
        self.auth = self._auth()

    def _auth(self):
        return OAuth1(self.api.api_key, self.api.secret_key)

    def _request(self, url, method, params=None, data=None, headers=None, **kwargs):
        url = "%s%s" % (self.api.base_url, url)
        if data:
            data = json.dumps(data)

        try:
            response = requests.request(
                method, url, params=params, data=data, headers=headers, auth=self.auth, **kwargs
            )
        except Exception as e:
            raise ConnectionError(e)

        try:
            if self._is_404(response.status_code):
                result = None
            elif not self._is_2xx(response.status_code):
                raise TheNounProjectException()
            else:
                result = response.json()
        except ValueError:
            result = None
        return result

    def _get(self, url, params=None, **kwargs):
        return self._request(url, "get", params=params, **kwargs)

    def _post(self, url, data=None, **kwargs):
        return self._request(url, "post", data=data, **kwargs)

    def _delete(self, url, **kwargs):
        return self._request(url, "delete", **kwargs)

    def _put(self, url, data=None, **kwargs):
        return self._request(url, "put", data=data, **kwargs)

    @staticmethod
    def _is_1xx(status_code):
        return 100 <= status_code <= 199

    @staticmethod
    def _is_2xx(status_code):
        return 200 <= status_code <= 299

    @staticmethod
    def _is_3xx(status_code):
        return 300 <= status_code <= 399

    @staticmethod
    def _is_4xx(status_code):
        return 400 <= status_code <= 499

    @staticmethod
    def _is_404(status_code):
        return 404 == status_code

    @staticmethod
    def _is_5xx(status_code):
        return 500 <= status_code <= 599

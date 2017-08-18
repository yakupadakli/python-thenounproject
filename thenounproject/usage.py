# coding=utf-8
from thenounproject.client import Client
from thenounproject.models import Usage as UsageModel


class Usage(Client):

    def __init__(self, **kwargs):
        super(Usage, self).__init__(**kwargs)
        self.url = "oauth/usage"

    def get(self):
        result = self._get("/%s" % self.url)
        usage = result.get("usage")
        if usage:
            usage['limits'] = result.get("limits", {})
        return UsageModel.parse(usage)

# coding=utf-8
from thenounproject.client import Client
from thenounproject.models import Collection as CollectionModel
from thenounproject.models import Icon as IconModel


class Enterprise(Client):

    def __init__(self, **kwargs):
        super(Enterprise, self).__init__(**kwargs)
        self.url = "notify/publish"

    def report_usage(self, icon_ids, is_test=True):
        icons = ",".join(map(lambda x: str(x), icon_ids))
        url = self.url
        if is_test:
            url = "%s?test=1" % self.url
        result = self._post("/%s" % url, data={"icons": icons})

        licenses_consumed = 0
        if result and result.get("result") == "success":
            licenses_consumed = result.get("licenses_consumed")
        return "%s licenses consumed." % licenses_consumed

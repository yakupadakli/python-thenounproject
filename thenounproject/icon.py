# coding=utf-8
from thenounproject.client import Client
from thenounproject.models import Icon as IconModel


class Icon(Client):

    def __init__(self, **kwargs):
        super(Icon, self).__init__(**kwargs)
        self.url = "icon"
        self.url_list = "icons"

    def list(self, term, limit_to_public_domain=None, limit=None, offset=None, page=None):
        params = {"limit_to_public_domain": limit_to_public_domain, "limit": limit, "offset": offset, "page": page}
        result = self._get("/%s/%s" % (self.url_list, term), params=params)
        return IconModel.parse_list(result.get("icons"))

    def _get_icon(self, icon_id_or_slug):
        result = self._get("/%s/%s" % (self.url, icon_id_or_slug))
        return IconModel.parse(result.get("icon"))

    def get(self, icon_id):
        return self._get_icon(icon_id)

    def get_by_term(self, term):
        return self._get_icon(term)

    def recent_uploads(self, limit=None, offset=None, page=None):
        params = {"limit": limit, "offset": offset, "page": page}
        result = self._get("/%s/recent_uploads" % self.url_list, params=params)
        return IconModel.parse_list(result.get("recent_uploads"))


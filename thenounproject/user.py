# coding=utf-8
from thenounproject.client import Client
from thenounproject.models import Collection as CollectionModel
from thenounproject.models import Icon as IconModel


class User(Client):

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.url = "user"

    def collections(self, user_id):
        result = self._get("/%s/%s/collections" % (self.url, user_id))
        return CollectionModel.parse_list(result.get("collections"))

    def collection_by_slug(self, user_id, collection_slug):
        result = self._get("/%s/%s/collections/%s" % (self.url, user_id, collection_slug))
        return CollectionModel.parse(result.get("collection"))

    def uploads(self, user_slug, limit=None, offset=None, page=None):
        params = {"limit": limit, "offset": offset, "page": page}
        result = self._get("/%s/%s/uploads" % (self.url, user_slug), params=params)
        return IconModel.parse_list(result.get("uploads"))

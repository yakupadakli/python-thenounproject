# coding=utf-8
from thenounproject.client import Client
from thenounproject.models import Collection as CollectionModel
from thenounproject.models import Icon as IconModel


class Collection(Client):

    def __init__(self, **kwargs):
        super(Collection, self).__init__(**kwargs)
        self.url = "collection"
        self.url_list = "collections"

    def list(self, limit=None, offset=None, page=None):
        params = {"limit": limit, "offset": offset, "page": page}
        result = self._get("/%s" % self.url_list, params=params)
        return CollectionModel.parse_list(result.get("collections"))

    def _get_collection(self, collection_id_or_slug):
        result = self._get("/%s/%s" % (self.url, collection_id_or_slug))
        return CollectionModel.parse(result.get("collection"))

    def get(self, collection_id):
        return self._get_collection(collection_id)

    def get_by_slug(self, slug):
        return self._get_collection(slug)

    def _icons(self, collection_id_or_slug, limit=None, offset=None, page=None):
        params = {"limit": limit, "offset": offset, "page": page}
        result = self._get("/%s/%s/icons" % (self.url, collection_id_or_slug), params=params)
        return IconModel.parse_list(result.get("icons"))

    def icons(self, collection_id, limit=None, offset=None, page=None):
        return self._icons(collection_id, limit=limit, offset=offset, page=page)

    def icons_by_slug(self, slug, limit=None, offset=None, page=None):
        return self._icons(slug, limit=limit, offset=offset, page=page)

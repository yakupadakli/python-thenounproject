# -*- coding: utf-8 -*-

import unittest

from tests import config
from thenounproject.api import Api
from thenounproject.models import Collection, Icon


class CollectionTests(unittest.TestCase):

    def setUp(self):
        self.api = Api(config.API_KEY, config.SECRET_KEY)

    def test_collection_list(self):
        collection_list = self.api.collection.list()
        self.assertIsInstance(collection_list, list)
        self.assertIsInstance(collection_list[0], Collection)

    def test_collection_get(self):
        collection = self.api.collection.get(4)
        self.assertIsInstance(collection, Collection)

    def test_collection_get_by_slug(self):
        collection = self.api.collection.get_by_slug("national-park-service")
        self.assertIsInstance(collection, Collection)

    def test_collection_icons(self):
        icon_list = self.api.collection.icons(55)
        self.assertIsInstance(icon_list, list)
        self.assertIsInstance(icon_list[0], Icon)

    def test_collection_icons_by_slug(self):
        icon_list = self.api.collection.icons_by_slug("bicycle")
        self.assertIsInstance(icon_list, list)
        self.assertIsInstance(icon_list[0], Icon)

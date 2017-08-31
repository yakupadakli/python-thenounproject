# -*- coding: utf-8 -*-

import unittest

from tests import config
from thenounproject.api import Api
from thenounproject.models import Collection


class CollectionTests(unittest.TestCase):

    def setUp(self):
        self.api = Api(config.API_KEY, config.SECRET_KEY)

    def test_collection_list(self):
        collection_list = self.api.collection.list()
        self.assertIsInstance(collection_list, list)
        self.assertIsInstance(collection_list[0], Collection)

    def test_show_get(self):
        collection = self.api.collection.get(1)
        self.assertIsInstance(collection, Collection)

    def test_show_get_by_slug(self):
        collection = self.api.collection.get()
        self.assertIsInstance(collection, Collection)

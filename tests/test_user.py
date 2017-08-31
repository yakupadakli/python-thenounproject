# -*- coding: utf-8 -*-

import unittest

from tests import config
from thenounproject.api import Api
from thenounproject.models import Collection, Icon


class IconTests(unittest.TestCase):

    def setUp(self):
        self.api = Api(config.API_KEY, config.SECRET_KEY)

    def test_user_collections(self):
        collection_list = self.api.user.collections(6)
        self.assertIsInstance(collection_list, list)
        self.assertIsInstance(collection_list[0], Collection)

    def test_user_collection_by_slug(self):
        collection = self.api.user.collection_by_slug(1, "bicycle")
        self.assertIsInstance(collection, Collection)

    def test_user_uploads(self):
        icon_list = self.api.user.uploads("edward")
        self.assertIsInstance(icon_list, list)
        self.assertIsInstance(icon_list[0], Icon)

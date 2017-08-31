# -*- coding: utf-8 -*-

import unittest

from tests import config
from thenounproject.api import Api
from thenounproject.models import Icon


class IconTests(unittest.TestCase):

    def setUp(self):
        self.api = Api(config.API_KEY, config.SECRET_KEY)

    def test_icon_list(self):
        icon_list = self.api.icon.list("fish")
        self.assertIsInstance(icon_list, list)
        self.assertIsInstance(icon_list[0], Icon)

    def test_icon_get(self):
        icon = self.api.icon.get(15)
        self.assertIsInstance(icon, Icon)

    def test_icon_get_by_term(self):
        icon = self.api.icon.get_by_term("globe")
        self.assertIsInstance(icon, Icon)

    def test_icon_recent_uploads(self):
        icon_list = self.api.icon.recent_uploads()
        self.assertIsInstance(icon_list, list)
        self.assertIsInstance(icon_list[0], Icon)

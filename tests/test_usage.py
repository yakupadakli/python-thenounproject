# -*- coding: utf-8 -*-

import unittest

from tests import config
from thenounproject.api import Api
from thenounproject.models import Usage


class UsageTests(unittest.TestCase):

    def setUp(self):
        self.api = Api(config.API_KEY, config.SECRET_KEY)

    def test_usage_get(self):
        usage = self.api.usage.get()
        self.assertIsInstance(usage, Usage)

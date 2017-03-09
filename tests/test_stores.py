#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from accountnt import stores


class BaseStoreTestCase(unittest.TestCase):

    def test_cannot_be_initialized_directly(self):

        with self.assertRaises(TypeError):
            stores.BaseStore()

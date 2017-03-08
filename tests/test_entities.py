#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from accountnt import entities


class CategoryTestCase(unittest.TestCase):

    def test_name_normalization(self):

        cases = {
            "foo": "Foo",
            "professional services": "Professional Services",
            "RENT": "Rent",
            "Household   Goods": "Household Goods",
        }

        for k, v in cases.items():
            self.assertEqual(
                entities.Category.normalized_name(k),
                v)


if __name__ == "__main__":
    unittest.main()

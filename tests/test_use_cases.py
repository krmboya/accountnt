#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from mock import Mock

from accountnt import use_cases as usc, entities as ent


# mock objects
catg_store = Mock()
catg_store.get_or_create = Mock()
user_catg_store = Mock()
user_catg_store.add = Mock()
user_catg_store.exists = Mock()


class AddCategoryTestCase(unittest.TestCase):

    def test_category_added(self):
        """Tests that a new category is successfully added"""

        category_name, user_id = "motor maintenance", 1

        # prepare mock objects
        catg_store.get_or_create.return_value = (
            ent.Category(category_name, 2),
            True)

        user_catg_store.exists.return_value = False

        add_catg = usc.AddCategoryUseCase(
            catg_store, user_catg_store)

        add_catg.execute("motor maintenance", user_id)

        catg_store.get_or_create.assert_called_with("Motor Maintenance")

        user_catg_store.add.assert_called_with(user_id, 2)

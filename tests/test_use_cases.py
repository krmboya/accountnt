#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from mock import Mock

from accountnt import use_cases as usc, entities as ent


class AddCategoryTestCase(unittest.TestCase):

    class UseCase(usc.AddCategoryUseCase):
        add_user_category = Mock()
        get_or_create = Mock()
        user_category_exists = Mock()

    def setUp(self):

        # create a use case subclass with mocked methods
        self.use_case = self.__class__.UseCase()

    def test_category_added(self):
        """Tests that a new category is successfully added"""

        category_name, user_id = "motor maintenance", 1

        # prepare mock objects
        self.use_case.get_or_create.return_value = ent.Category(
            category_name, 2)

        self.use_case.user_category_exists.return_value = False

        # execute use case
        self.use_case.execute_with(category_name, user_id)

        # assert methods
        category_name = ent.Category.normalized_name(category_name)
        self.use_case.get_or_create.assert_called_with(category_name)
        self.use_case.add_user_category.assert_called_with(1, 2)

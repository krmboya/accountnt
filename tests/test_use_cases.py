#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from mock import Mock

from accountnt import use_cases as usc, entities as ent


class AddCategoryTestCase(unittest.TestCase):

    class UseCase(usc.AddCategoryUseCase):
        pass

    def setUp(self):

        # create a use case subclass with mocked methods
        self.use_case = self.__class__.UseCase()

        # todo: patch relevant use case methods
        # to make the test below work

    def test_category_added(self):
        """Tests that a new category is successfully added"""

        category_name, user_id = "motor maintenance", 1

        # prepare mock objects
        self.user_case.get_or_create.return_value = ent.Category(
            category_name, 2)

        # execute use case
        self.user_case.execute_with("motor maintenance", user_id)

        # assert methods
        self.use_case.get_or_create.assert_called_with("Motor Maintenance")
        self.use_case.add.assert_called_with(1, 2)

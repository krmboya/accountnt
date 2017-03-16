#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import io
import tempfile
import os

from accountnt import entities
from accountnt.adapters import commandline_adapters as cmd


class AddCategoryFileSystemTestCase(unittest.TestCase):

    def test_can_add_user_category(self):

        # a path to tmp storage location
        storage_dir = os.path.join(
            tempfile.gettempdir(), ".accountnt")

        category_name = 'professional services'

        # initialize use case with tmp storage
        use_case = cmd.AddCategory(storage_dir)

        # execute use case
        use_case.execute_with(category_name, 1001)

        # check that category name exists in tmp storage
        normalized_name = entities.Category.normalized_name(category_name)
        with io.open(use_case.categories_file) as f:
            matching_lines = [line for line in f
                              if line.strip() == normalized_name]
        self.assertTrue(len(matching_lines) > 0)

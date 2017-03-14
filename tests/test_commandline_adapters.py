#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import io
import tempfile
import os

from accountnt import entities
from adapters import commandline_adapters as cmd_adapters


class AddCategoryFileSystemTestCase(unittest.TestCase):

    def test_can_add_user_category(self):

        storage_dir = os.path.join(
            tempfile.gettempdir(), ".accountnt")
        category_name = 'professional services'

        use_case = cmd_adapters.AddCategory(storage_dir)

        use_case.execute_with(category_name, 1001)
        normalized_name = entities.Category.normalized_name(category_name)
        with io.open(use_case.categories_file) as f:
            matching_lines = [line for line in f
                              if line.strip() == normalized_name]

        self.assertTrue(len(matching_lines) > 0)

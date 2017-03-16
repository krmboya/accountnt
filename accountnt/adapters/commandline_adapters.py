#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Override use cases for the commandline environment"""
import io
import os

from accountnt import entities, use_cases


def ensure_dir(dirname):
    """Create directory dirname if it doesn't exist"""
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def ensure_file(filename):
    """Create file `filename` if it doesn't exist"""
    with open(filename, 'a'):
        os.utime(filename, None)


class AddCategory(use_cases.AddCategoryUseCase):

    def __init__(self, storage_directory):
        """Initializes storage"""
        self._categories_filename = "categories.txt"
        self._user_categories_filename = "ucategories.txt"

        # Ensure the directory exists
        ensure_dir(storage_directory)

        # set full path to storage files
        self.categories_file = os.path.join(
            storage_directory,
            self._categories_filename)

        self.user_categories_file = os.path.join(
            storage_directory,
            self._user_categories_filename)

        # ensure they exists
        ensure_file(self.categories_file)
        ensure_file(self.user_categories_file)

    def get_or_create(self, category_name):
        """Get a category via its name

        Creates it if it doesn't exist"""
        with io.open(self.categories_file, 'r+t') as f:

            for i, line in enumerate(f):
                if line == category_name:
                    return entities.Category(category_name, i)

            f.write(category_name + u"\n")
            f.flush()
            return entities.Category(category_name, i+1)

    def user_category_exists(self, user_id, category_id):
        """Checks that user has added the particular category"""
        with io.open(self.user_categories_file) as f:
            matching_category = [line for line in f
                                 if line.strip() == str(category_id)]

            return len(matching_category) > 0

    def add_user_category(self, user_id, category_id):
        """Associates the category with the user"""
        with io.open(self.user_categories_file, 'at') as f:
            f.write(unicode(category_id) + "\n")

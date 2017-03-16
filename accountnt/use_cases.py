#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Use Cases for the app """
import abc

import entities


class AddCategoryUseCase:
    __metaclass__ = abc.ABCMeta

    def execute_with(self, category_name, user_id):
        """Executes the use case with the provided arguments

        The abstract helper methods should be overriden with the
        actual functionality
        """

        category_name = entities.Category.normalized_name(category_name)
        category = self.get_or_create(category_name)

        if self.user_category_exists(user_id, category.uid):
            msg = "You've already added '{}'"
            return msg.format(category.name)

        self.add_user_category(user_id, category.uid)
        return "Category '{}' has been added".format(category.name)

    @abc.abstractmethod
    def get_or_create(self, category_name):
        """Retrieves or creates`category_name`"""
        pass

    @abc.abstractmethod
    def user_category_exists(self, user_id, category_id):
        """Checks whether user already has the category"""
        pass

    @abc.abstractmethod
    def add_user_category(self, user_id, category_id):
        """Adds category for the user"""
        pass

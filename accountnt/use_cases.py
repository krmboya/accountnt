#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Use Cases for the app """
import abc

import entities


class AddCategoryUseCase:
    __metaclass__ = abc.ABCMeta

    def execute_with(self, category_name, user_id):

        category_name = entities.Category.normalized_name(category_name)
        category = self.get_or_create(category_name)

        if self.user_category_exists(category_name, user_id):
            msg = "You've already added '{}'"
            return msg.format(category.name)

        self.add_user_category(user_id, category.uid)
        return "Category '{}' has been added".format(category.name)

    @abc.abstractmethod
    def get_or_create(self, category_name, user_id):
        pass

    @abc.abstractmethod
    def user_category_exists(self, category_name, user_id):
        pass

    @abc.abstractmethod
    def add_user_category(self, category_name, user_id):
        pass

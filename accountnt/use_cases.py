#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Use Cases for the app """
import entities


class AddCategoryUseCase(object):

    def __init__(self, category_store, user_category_store):
        self.category_store = category_store
        self.user_category_store = user_category_store

    def execute(self, category_name, user_id):

        category_name = entities.Category.normalized_name(category_name)
        category, __ = self.category_store.get_or_create(category_name)

        if self.user_category_store.exists(
                user_id, category.uid):
            return "You've already added '{}'".format(category.name)

        self.user_category_store.add(user_id, category.uid)
        return "Category '{}' has been added".format(category.name)

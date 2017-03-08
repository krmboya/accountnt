#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Core of the application"""
from collections import namedtuple

# Entities
User = namedtuple('User', ['uid', 'name'])
UserCategory = namedtuple('UserCategory', ['user_id', 'category_id'])


class Category(object):

    def __init__(self, name, uid=None):
        self.uid = uid
        self.name = name

    @staticmethod
    def normalized_name(name):
        """Standardizes category name format"""

        return " ".join(name.split()).title()

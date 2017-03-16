#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Core Entities of the application"""

from collections import namedtuple

# Entities
User = namedtuple('User', ['uid', 'name'])
UserCategory = namedtuple('UserCategory', ['user_id', 'category_id'])


class Category(object):
    """Represents a spending category"""

    def __init__(self, name, uid=None):
        self.uid = uid
        self.name = self.normalized_name(name)

    @staticmethod
    def normalized_name(name):
        """Standardizes category name format

        e.g. professional services -> Professional Services
             RENT -> Rent"""

        return " ".join(name.split()).title()

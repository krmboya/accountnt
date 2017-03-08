#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Store(object):
    """Defines an interface via which data is retrieved from storage"""

    def add(self, **kwargs):
        pass

    def exists(self, **kwargs):
        pass

    def get_or_create(self, **kwargs):
        pass

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Adapters interfaces for various external representations"""
import stores


class MemoryStore(stores.Store):
    """Adapts Store interface to an in-memory store"""

    def add(self, **kwargs):
        self.list_.append(**kwargs)

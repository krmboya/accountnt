#!/usr/bin/env python
# -*- coding: utf-8 -*-
import abc


class BaseStore:
    """Defines an interface via which data is retrieved from storage"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def add(self, **kwargs):
        pass

    @abc.abstractmethod
    def exists(self, **kwargs):
        pass

    @abc.abstractmethod
    def get_or_create(self, **kwargs):
        pass

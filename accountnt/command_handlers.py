#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Defines decorators that map commands to callables"""


command_handlers = {}


class CommandNotFound(Exception):
    """Raised for a missing command """
    pass


def addcategory(f):
    command_handlers["addcategory"] = f
    return f


def get(command_name):
    try:
        return command_handlers[command_name]
    except KeyError:
        raise CommandNotFound(command_name)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Defines decorators that map commands to callables"""


command_handlers = {}


class CommandNotFound(Exception):
    """Raised for a missing command """
    pass


def addcategory(f):
    """Registers 'addcategory' handler"""
    command_handlers["addcategory"] = f
    return f


def get(command_name):
    """Retrieves handler for command `command_name`

    Raises `CommandNotFound` exception when missing"""
    try:
        return command_handlers[command_name]
    except KeyError:
        raise CommandNotFound(command_name)

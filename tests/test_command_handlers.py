#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from accountnt import command_handlers as handlers


class CommandTestCase(unittest.TestCase):

    def test_add_category(self):

        command = "addcategory"

        # define a dummy handler
        @handlers.addcategory
        def foo(*args, **kwargs):
            return "foo"

        # should be able to retrieve `foo` as command handler
        cmd_handler = handlers.get(command)

        self.assertIs(cmd_handler, foo)
        self.assertEqual(cmd_handler(), "foo")

    def test_missing_command(self):

        command = "somerandomcommand"

        with self.assertRaises(handlers.CommandNotFound):
            handlers.get(command)

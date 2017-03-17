#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from commandline import client


class ClientTestCase(unittest.TestCase):

    def test_unknown_command_msg(self):

        command = "foobar"

        response = client.execute_command(*[command])

        self.assertTrue(client.unknown_command_msg in response)
        self.assertTrue(client.usage in response)

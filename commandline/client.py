#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides the commandline app

usage: accountnt <command> [<arguments>..]
"""
import sys
import os

from accountnt import command_handlers as handlers


usage = """usage: accountnt <command> [<arguments>..]

Try `accountnt help` to view available commands."""

unknown_command_msg = "Could not understand your command."


def exit_with_error(msg):
    """Writes error message to stdout"""

    sys.stderr.write(msg + "\n")
    sys.exit(1)


def execute_command(*args):
    """Given the user arguments, invoke the appropriate command"""

    command_name, command_args = args[0], args[1:]

    try:
        command_handler = handlers.get(command_name)
    except handlers.CommandNotFound:
        return "\n".join([unknown_command_msg, usage])

    response = command_handler(*command_args)
    return response


if __name__ == "__main__":
    args = sys.argv

    if len(args) < 2:
        exit_with_error(usage)

    response = execute_command(*args[1:])
    sys.stdout.write(response + "\n")

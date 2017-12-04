"""Distributed supervision suite.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import tempfile
import traceback

import click
import kazoo
import kazoo.exceptions
import ldap3

import treadmill
from treadmill import restclient
from treadmill import cli
from treadmill import context
from treadmill import yamlwrapper as yaml


def init():
    """Return top level command handler."""

    @click.group(cls=cli.make_commands(__name__))
    def run():
        """Cross-cell supervision tools."""
        cli.init_logger('daemon.conf')

    return run
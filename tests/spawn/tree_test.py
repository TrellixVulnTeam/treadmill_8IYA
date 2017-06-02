"""Unit test for treadmill.spawn.tree.
"""

import os
import shutil
import unittest

import mock

from treadmill import fs
from treadmill import utils
from treadmill.spawn import tree as spawn_tree


class TreeTest(unittest.TestCase):
    """Tests for teadmill.spawn.tree."""

    @mock.patch('os.listdir', mock.Mock())
    @mock.patch('shutil.rmtree', mock.Mock())
    @mock.patch('treadmill.fs.mkdir_safe', mock.Mock())
    @mock.patch('treadmill.utils.create_script', mock.Mock())
    def test_create(self):
        """Tests creating tree."""
        os.listdir.side_effect = [
            ['testing'], ['testing'],
        ]

        tree = spawn_tree.Tree('/does/not/exist', 2, 5)
        tree.create()

        self.assertEqual(8, fs.mkdir_safe.call_count)
        self.assertEqual(6, utils.create_script.call_count)
        self.assertEqual(2, shutil.rmtree.call_count)


if __name__ == '__main__':
    unittest.main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

# Your test case class goes here


class TestEcho(unittest.TestCase):
    def setUp(self):
        self.parser = echo.create_parser()

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper_flag(self):
        """Tests if --upper flag stores upper in Namespace as True
        and that 'hello' becomes 'HELLO' when program is run."""
        echo.sys.argv = ['echo.py', 'hello', '--upper']
        self.assertTrue(self.parser.parse_args().upper)
        self.assertEqual(echo.main(), "HELLO")

    def test_u_flag(self):
        """Tests if -u flag stores upper in Namespace as True
        and that 'hello' becomes 'HELLO' when program is run."""
        echo.sys.argv = ['echo.py', 'hello', '-u']
        self.assertTrue(self.parser.parse_args().upper)
        self.assertEqual(echo.main(), "HELLO")

    def test_missing_u_upper_flags(self):
        """Tests if missing both -u and --upper flags,
        upper in Namespace is stored as False
        and 'hello' does not become 'HELLO' when program is run."""
        echo.sys.argv = ['echo.py', 'hello']
        self.assertFalse(self.parser.parse_args().upper)
        self.assertNotEqual(echo.main(), "HELLO")

    def test_lower_flag(self):
        """Test if --lower flag stores lower in Namespace as True
        and that 'HELLO' becomes 'hello' when program is run."""
        echo.sys.argv = ['echo.py', 'HELLO', '--lower']
        self.assertTrue(self.parser.parse_args().lower)
        self.assertEqual(echo.main(), "hello")

    def test_l_flag(self):
        """Test if -l flag stores lower in Namespace as True
        and that 'HELLO' becomes 'hello' when program is run."""
        echo.sys.argv = ['echo.py', 'HELLO', '-l']
        self.assertTrue(self.parser.parse_args().lower)
        self.assertEqual(echo.main(), "hello")

    def test_missing_l_lower_flags(self):
        """Tests if missing both -l and --lower flags,
        lower in Namespace is stored as False
        and 'HELLO' does not become 'hello' when program is run."""
        echo.sys.argv = ['echo.py', 'HELLO']
        self.assertFalse(self.parser.parse_args().lower)
        self.assertNotEqual(echo.main(), "hello")

    def test_title_flag(self):
        """Test if --title flag stores title in Namespace as True
        and that 'hello' becomes 'HELLO' when program is run."""
        echo.sys.argv = ['echo.py', 'hello', '--title']
        self.assertTrue(self.parser.parse_args().title)
        self.assertEqual(echo.main(), "Hello")

    def test_t_flag(self):
        """Test if -t flag stores title in Namespace as True
        and that 'hello' becomes 'HELLO' when program is run."""
        echo.sys.argv = ['echo.py', 'hello', '-t']
        self.assertTrue(self.parser.parse_args().title)
        self.assertEqual(echo.main(), "Hello")

    def test_missing_t_title_flags(self):
        """Tests if missing both -t and --title flags,
        title in Namespace is stored as False
        and 'hello' does not become 'Hello' when program is run."""
        echo.sys.argv = ['echo.py', 'hello']
        self.assertFalse(self.parser.parse_args().title)
        self.assertNotEqual(echo.main(), "Hello")

    def test_all_flags(self):
        """Test if when all flags are provided,
        'heLLo' becomes 'Hello'"""
        echo.sys.argv = ['echo.py', 'heLLo', '-ult']
        self.assertEqual(echo.main(), "Hello")

    def test_no_flags(self):
        """Test if when no flags are provided,
        'heLLo' is returned as 'heLLo'"""
        echo.sys.argv = ['echo.py', 'heLLo']
        self.assertEqual(echo.main(), "heLLo")


if __name__ == '__main__':
    unittest.main()

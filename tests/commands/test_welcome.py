"""Tests for our `twitment welcome` subcommand."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase


class TestHello(TestCase):
    def test_returns_multiple_lines(self):
        output = popen(['twitment', 'welcome'], stdout=PIPE).communicate()[0]
        lines = output.split('\n')
        self.assertTrue(len(lines) != 1)

    def test_returns_hello_world(self):
        output = popen(['twitment', 'welcome'], stdout=PIPE).communicate()[0]
        self.assertTrue('Welcome to twitter sentiment analysis tool' in output)

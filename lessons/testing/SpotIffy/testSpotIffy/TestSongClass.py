import unittest

from lessons.testing.SpotIffy.spottify import *


class TestSongInit(unittest.TestCase):
    def test_init_name(self):
        song = Song("name", 0, "artist", "Genre")


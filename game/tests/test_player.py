import unittest
import unittest.mock
from game.Game import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self._player_under_test = Player('Tester')
        pass

    def __init__(self):
        pass

    def test_initialized_with_provided_name(self):
        self.assertEqual(self._player_under_test.name, 'Tester')
import unittest
import unittest.mock
from game.Game import Game
from game.Game import Player


class TestGame(unittest.TestCase):

    def setUp(self):
        self._player1 = Player()
        self._player2 = Player()
        self._players = [self._player1, self._player2]
        self._game_under_test = Game(self._players)

    def __init__(self):
        pass

    def test_initialized_with_correct_current_player(self):
        self.assertEqual(self._game_under_test.current_player, self._player1)

    def test_initialized_with_correct_number_of_players(self):
        self.assertEqual(len(self._game_under_test.players), len(self._players))

    def test_initialized_with_first_turn(self):
        self.assertEqual(self._game_under_test.is_last_turn, False)
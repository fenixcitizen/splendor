import unittest
import unittest.mock
from game.Game import Game
from game.Game import Player


class TestGame(unittest.TestCase):

    def setUp(self):
        self._player1 = Player()
        self._player2 = Player()
        self._players = [self._player1, self._player2]
        self._gameUnderTest = Game(self._players)

    def __init__(self):
        pass

    def test_initialized_with_correct_number_of_players(self):
        self.assertEqual(self._gameUnderTest.current_player, self._player1)

    def test_initialized_with_first_turn(self):
        self.assertEqual(self._gameUnderTest.isLastTurn, False)
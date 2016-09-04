import unittest
import unittest.mock
from game.Game import Game
from game.Game import Player
from game.Game import GameException

class TestGame(unittest.TestCase):

    def setUp(self):
        self._player1 = Player('Player1')
        self._player2 = Player('Player2')
        self._players = [self._player1, self._player2]
        self._game_under_test = Game(self._players)

    def __init__(self):
        pass

    def test_throws_when_number_of_players_is_below_two(self):
        one_player = [self._player1]
        self.assertRaises(GameException, Game(one_player))

    def test_throws_when_number_of_players_is_below_two(self):
        five_players = [self._player1, self._player2, Player('Player3'), Player('Player4'), Player('Player5')]
        self.assertRaises(GameException, Game(five_players))

    def test_throws_when_players_contains_same_player_twice(self):
        duplicated_players = [self._player1, self._player2, self._player2]
        self.assertRaises(GameException, Game(duplicated_players))

    def test_initialized_with_correct_current_player(self):
        self.assertEqual(self._game_under_test.current_player, self._player1)

    def test_initialized_with_correct_players(self):
        self.assertListEqual(self._game_under_test.players, self._players)

    def test_initialized_with_first_turn(self):
        self.assertEqual(self._game_under_test.is_last_turn, False)

    # def test_initialize_with_correct_number_of_tokens(self):
    #     self.assertEqual(self._game_under_test.is_last_turn, False)
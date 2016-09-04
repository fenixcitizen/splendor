# game
# turn_number
# players
# current_player
# display_draw (levels)
# display_cards (levels)
# display_nobles
# tokens
# is last turn

from game import get_mudule_logger

logger = get_mudule_logger(__name__)


class Game:
    max_num_players = 4

    def __init__(self, players):
        if not self._checkNumberofPlayers(len(players)):
            raise GameException('The number of plays exceeds the maxium allowed. No more than {0} players.'.format(self.max_num_players))
        self._players = players
        # TODO - define tokens based on the number of players

    @property
    def players(self):
        return self._players

    @property
    def current_player(self):
        return self._current_player

    @property
    def tokens(self):
        return self._tokens

    @property
    def isLastTurn(self):
        return self._isLastTurn

    @current_player.setter
    def current_player(self, v):
        self._current_player = v

    @isLastTurn.setter
    def isLastTurn(self, v):
        self._isLastTurn = v

    def display_nobles(self):
        pass

    def display_cards(self, level):
        pass

    def display_draw(self, level):
        pass

    def _checkNumberofPlayers(self, v):
        if v > self.max_num_players or v==1:
            return False
        else:
            return True


class Player:
    def __init__(self,name):
        self._name=name
    @property
    def name(self):
        return self._name


class GameException(Exception):
    pass

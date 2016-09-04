# game
# turn_number
# players
# current_player
# display_draw (levels)
# display_cards (levels)
# display_nobles
# tokens
# is last turn


class Game:
    def __init__(self, players, current_player, tokens, isLastTurn=False):
        self._players = players
        self._current_player = current_player
        self._tokens = tokens
        self._isLastTurn = isLastTurn

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

    def display_nobles(self):
        pass

    def display_cards(self, level):
        pass

    def display_draw(self, level):
        pass

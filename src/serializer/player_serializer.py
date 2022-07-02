from copy import deepcopy
from json import dumps

from model.player import Player

class PlayerSerializer:

    @staticmethod
    def serialize(player: Player):
        serialized_player: str = deepcopy(player)
        serialized_player.bet = vars(serialized_player.bet)
        return dumps(vars(player))

    @staticmethod
    def serialize_list(players: list[Player]):
        serialized_players_list: str = deepcopy(players)
        for player in serialized_players_list: player.bet = vars(player.bet)
        serialized_players_list = [vars(player) for player in serialized_players_list]

        return dumps(serialized_players_list)

from copy import deepcopy
from json import dumps

from model.game import Game

class GameSerializer:

    def serialize(game: Game):
        serialized_game: str = deepcopy(game)
        for player in serialized_game.players: player.bet = vars(player.bet)
        serialized_game.teams = [vars(competitor) for competitor in serialized_game.teams]
        serialized_game.players = [vars(player) for player in serialized_game.players]
        return dumps(vars(serialized_game))

    def serialize_list(games: list[Game]):
        serialized_games_list: list[str] = deepcopy(games)
        for game in serialized_games_list:
            for player in game.players: player.bet = vars(player.bet)
            game.teams = [vars(competitor) for competitor in game.teams]
            game.players = [vars(player) for player in game.players]
        serialized_games_list = [vars(game) for game in serialized_games_list]

        return dumps(serialized_games_list)

from uuid import UUID

from model.game import Game

from service.utils import to_game

from model.exceptions.invalid_uuid import InvalidUUID
from model.exceptions.resource_not_found import ResourceNotFound

from repository.games_dao import GamesDAO

from validator.game_validator import GameValidator

from serializer.game_serializer import GameSerializer

class GameService:

    @staticmethod
    def list_games(open_only: bool=True):
        games: list[Game] = GamesDAO.list(open_only)
        return GameSerializer.serialize_list(games)

    @staticmethod
    def get_game(id: str):
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID

        game = GamesDAO.retrieve(id)
        if not game: raise ResourceNotFound

        return GameSerializer.serialize(game)

    @staticmethod
    def create_game(request):
        game = to_game(request)
        GameValidator.validate(game)

        GamesDAO.insert(game)
        return GameSerializer.serialize(game)

    @staticmethod
    def close_game(id):
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID

        GamesDAO.close(id)

    @staticmethod
    def update_game(id, request):
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID

        game_update = to_game(request)
        GameValidator.validate(game_update)

        GamesDAO.update(game_update)

    @staticmethod
    def delete_game(id):
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID

        GamesDAO.delete(id)

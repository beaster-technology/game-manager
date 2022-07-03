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
    def list(open_only: bool=True) -> str:
        games: list[Game] = GamesDAO.list(open_only)
        return GameSerializer.serialize_list(games)

    @staticmethod
    def get(id: str) -> str:
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID

        game: Game = GamesDAO.retrieve(id)
        if not game: raise ResourceNotFound

        return GameSerializer.serialize(game)

    @staticmethod
    def create(request) -> str:
        game: Game = to_game(request)
        GameValidator.validate(game)

        GamesDAO.insert(game)
        return GameSerializer.serialize(game)

    @staticmethod
    def close(id) -> str:
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID

        '''
        Here you need to determine the winners
        and split the absolute pot within them

        you can write the calculation at pot_splitter.py
        and use it here - this way we decouple the calculation
        from the game service

        here you will also need to build a Result object and
        post it in the results collection at firestore.
        to do it you can use insert() method of ResultService :)

        good luck!
        '''

        GamesDAO.close(id)

    @staticmethod
    def update(id, request) -> str:
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID

        game_update: Game = to_game(request)
        GameValidator.validate(game_update)

        GamesDAO.update(game_update)

    @staticmethod
    def delete(id) -> str:
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID

        GamesDAO.delete(id)

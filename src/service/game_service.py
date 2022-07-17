from typing import Union
from uuid import UUID
from operator import attrgetter

from src.model.game import Game
from src.model.result import Result
from src.model.player import Player

from src.service.utils import to_game

from src.model.exception.invalid_uuid import InvalidUUID
from src.model.exception.resource_not_found import ResourceNotFound

from src.validator.game_validator import GameValidator
from src.serializer.game_serializer import GameSerializer
from src.repository.games_dao import GamesDAO

from src.service.result_service import ResultService
from src.serializer.result_serializer import ResultSerializer

from src.calculator.pot_splitter import PotSplitter

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
    def create(request: dict[str, Union[str, float, int, bool]]) -> str:
        game: Game = to_game(request)
        GameValidator.validate(game)

        GamesDAO.insert(game)
        return GameSerializer.serialize(game)

    @staticmethod
    def close(id: str) -> str:
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID

        target_game: Game = GamesDAO.retrieve(id)
        if not target_game: raise ResourceNotFound

        champion_name: str = max(target_game.teams, key=attrgetter('goals')).name

        distribution: list[Player] = PotSplitter.calculate_pot_distribution(
            target_game.players,
            champion_name
        )

        game_result: Result = Result(
            id=target_game.id,
            winners=distribution,
            champion=champion_name
        ) 
        
        ResultService.insert(game_result)
        GamesDAO.close(id)

        return ResultSerializer.serialize(game_result)

    @staticmethod
    def update(id: str, request: dict[str, Union[str, float, int, bool]]) -> str:
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID

        game_update: Game = to_game(request)
        GameValidator.validate(game_update)

        GamesDAO.update(game_update)

    @staticmethod
    def delete(id: str) -> str:
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID

        GamesDAO.delete(id)

from uuid import UUID

from src.model.game import Game
from src.model.result import Result

from src.model.exception.invalid_uuid import InvalidUUID
from src.model.exception.resource_not_found import ResourceNotFound

from src.repository.results_dao import ResultsDAO

from src.serializer.result_serializer import ResultSerializer

class ResultService:
    
    @staticmethod
    def get(id: str) -> str:
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID
        
        result: Result = ResultsDAO.retrieve(id)
        if result == '': raise ResourceNotFound

        return ResultSerializer.serialize(result)

    @staticmethod
    def insert(game: Game) -> str:
        ResultsDAO.insert(game)

    @staticmethod
    def delete(id: str) -> str:
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID
        
        ResultsDAO.delete(id)
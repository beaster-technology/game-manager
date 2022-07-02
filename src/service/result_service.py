from uuid import UUID

from model.game import Game
from model.result import Result

from model.exceptions.invalid_uuid import InvalidUUID
from model.exceptions.resource_not_found import ResourceNotFound

from repository.results_dao import ResultsDAO

from serializer.result_serializer import ResultSerializer

class ResultService:
    
    @staticmethod
    def get(id: str):
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID
        
        result: Result = ResultsDAO.retrieve(id)
        if result == '': raise ResourceNotFound

        return ResultSerializer.serialize(result)

    @staticmethod
    def insert(game: Game):
        ResultsDAO.insert(game)

    @staticmethod
    def delete(id: str):
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID
        
        ResultsDAO.delete(id)
from uuid import UUID
from model.result import Result

from serializer.result_serializer import ResultSerializer

from repository.results_dao import ResultsDAO

from model.exceptions.invalid_uuid import InvalidUUID
from model.exceptions.resource_not_found import ResourceNotFound

class ResultService:
    def get_result(id: str):
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID
        
        result: Result = ResultsDAO.retrieve(id)
        if result == '': raise ResourceNotFound

        return ResultSerializer.serialize(result)

    def delete_result(id: str):
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID
        
        ResultsDAO.delete(id)
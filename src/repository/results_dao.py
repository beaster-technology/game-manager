from copy import deepcopy
from model.result import Result
from model.player import Player
from model.bet import Bet

MOCKED_EPOCH = 1656681396.448879
MOCKED_RESULT = Result('61be0f5f-a5c1-4e0a-92ef-686eac1e3699', [
    Player('Tanan', Bet(50, MOCKED_EPOCH)),
    Player('Besca', Bet(35, MOCKED_EPOCH))
], 'Brazil')

class ResultsDAO: # This guy needs to connect to firebase firestore
    def __init__(self) -> None:
        # Here you can initialize the connection
        pass

    @staticmethod
    def retrieve(id: str):
        # Retrieve targeted result
        target_result: Result = deepcopy(MOCKED_RESULT)
        target_result.id = id
        
        return target_result

    @staticmethod
    def insert(result: Result):
        # Delete game result with provided ID
        pass

    @staticmethod
    def delete(id: str):
        # Delete game result with provided ID
        pass

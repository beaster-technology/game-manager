from copy import deepcopy

from src.model.game import Game
from src.model.result import Result
from src.model.player import Player
from src.model.bet import Bet

MOCKED_EPOCH: float = 1656681396.448879
MOCKED_RESULT: list[Game] = Result('61be0f5f-a5c1-4e0a-92ef-686eac1e3699', [
    Player('Tanan', Bet(50, 'Brazil')),
    Player('Besca', Bet(35, 'Brazil'))
], 'Brazil')

class ResultsDAO: # This guy needs to connect to firebase firestore
    def __init__(self) -> None:
        # Here you can initialize the connection
        pass

    @staticmethod
    def retrieve(id: str) -> Result:
        # Retrieve targeted result
        target_result: Result = deepcopy(MOCKED_RESULT)
        target_result.id = id
        
        return target_result

    @staticmethod
    def insert(result: Result) -> None:
        # Delete game result with provided ID
        pass

    @staticmethod
    def delete(id: str) -> None:
        # Delete game result with provided ID
        pass

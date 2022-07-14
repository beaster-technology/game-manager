from copy import deepcopy

from src.model.game import Game
from src.model.result import Result
from src.model.player import Player
from src.model.bet import Bet
from google.cloud import firestore

MOCKED_EPOCH: float = 1656681396.448879
MOCKED_RESULT: list[Game] = Result('61be0f5f-a5c1-4e0a-92ef-686eac1e3699', [
    Player('Tanan', Bet(50, 'Brazil')),
    Player('Besca', Bet(35, 'Brazil'))
], 'Brazil')

class ResultsDAO: # This guy needs to connect to firebase firestore
    def __init__(self) -> None:
        # Set variable type from collection return type
        self.results_collection = firestore \
            .Client(project = 'beaster-f041b') \
            .collection(u'results')

    def retrieve(self, id: str) -> Result:
        print(self.results_collection.document(id))

    def insert(self, result: Result) -> None:
        
        pass

    def delete(id: str) -> None:
        pass

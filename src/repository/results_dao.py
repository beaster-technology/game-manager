import os
from pydoc import doc
from xml.dom.minidom import Document
from src.model.game import Game
from src.model.result import Result
from src.model.player import Player
from src.model.bet import Bet
from google.cloud import firestore

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='/mnt/c/Users/henri/Meu Drive/Drive Pessoal/Trabalhos/2022.1/POO/Python/game-manager/credentials/beaster-f041b-1f5e0e12c487.json'

MOCKED_EPOCH: float = 1656681396.448879
MOCKED_RESULT: list[Game] = Result('61be0f5f-a5c1-4e0a-92ef-686eac1e3699', [
    Player('Tanan', Bet(50, 'Brazil')),
    Player('Besca', Bet(35, 'Brazil'))
], 'Brazil')

class ResultsDAO: # This guy needs to connect to firebase firestore
    db = firestore.Client(project='beaster-f041b').collection('results')

    @staticmethod
    def retrieve(id: str) -> Result:
        document = ResultsDAO.db.document(id).get()
        if not document: return None

        print(document.to_dict())
      
    @staticmethod
    def insert(result: Result) -> None:
        
        pass

    @staticmethod
    def delete(id: str) -> None:
        pass

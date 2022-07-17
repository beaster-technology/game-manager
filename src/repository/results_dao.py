import os
from pydoc import doc
from xml.dom.minidom import Document
from src.model.game import Game
from src.model.result import Result
from src.model.player import Player
from src.model.bet import Bet
from google.cloud import firestore

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='/mnt/d/Google Drive/Drive Pessoal/Trabalhos/2022.1/POO/Python/game-manager/credentials/beaster-f041b-1f87f429ab75.json'

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

        winners = []
        for winner in document.to_dict().get('winners').items():
            winner_name: str = winner[0]
            winner_info: dict = winner[1]

            winners.append(
                Player(
                    winner_name, 
                    Bet(winner_info.get('value'), winner_info.get('target'), winner_info.get('created_at'))
                )
            )

        return Result(
            id, 
            winners, 
            document.to_dict().get('champion')
        )
      
    @staticmethod
    def insert(result: Result) -> None:
        
        pass

    @staticmethod
    def delete(id: str) -> None:
        pass
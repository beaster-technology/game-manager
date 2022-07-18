import os
from pydoc import doc
from xml.dom.minidom import Document
from src.model.game import Game
from src.model.result import Result
from src.model.player import Player
from src.model.bet import Bet
from google.cloud import firestore

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='/mnt/d/Google Drive/Drive Pessoal/Trabalhos/2022.1/POO/Python/game-manager/credentials/beaster-f041b-1f87f429ab75.json'

class ResultsDAO:
    db = firestore.Client(project='beaster-f041b').collection('results')

    @staticmethod
    def retrieve(id: str) -> Result:
        document = ResultsDAO.db.document(id).get().to_dict()
        print(document)
        if not document: return None

        winners = []
        for winner in document['winners']:
            winner_name: str = winner['name']
            winner_info: dict = winner['bet']

            winners.append(
                Player(
                    winner_name, 
                    Bet(winner_info.get('value'), winner_info.get('target'), winner_info.get('created_at'))
                )
            )

        return Result(
            id, 
            winners, 
            document['champion']
        )
      
    @staticmethod
    def insert(result: Result) -> None:
        document_reference = ResultsDAO.db.document(result.id)

        winner_list = []
        for winner in result.winners:
            winner_list.append(
                { 
                  'name': winner.name, 
                  'bet': {
                    'value': winner.bet.value,
                    'target': winner.bet.target,
                    'created_at': winner.bet.created_at
                    }
                }
            )

        document_reference.set({
            'id': result.id,
            'winners': winner_list,
            'champion': result.champion
        })

    @staticmethod
    def delete(id: str) -> None:
        ResultsDAO.db.document(id).delete()
from locale import strcoll
import os
from platform import platform
from this import d

from jinja2 import TemplateRuntimeError
from src.model.game import Game
from src.model.competitor import Competitor
from src.model.player import Player
from src.model.bet import Bet
from google.cloud import firestore

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/mnt/d/Google Drive/Drive Pessoal/Trabalhos/2022.1/POO/Python/game-manager/credentials/beaster-f041b-1f87f429ab75.json'

MOCKED_EPOCH: float = 1656681396.448879
MOCKED_GAME_LIST: list[Game] = [
    Game(
        teams=(Competitor('Colombia', 2), Competitor('England', 3)),
        players=[
            Player('Tanga', Bet(12.1, 'Colombia', MOCKED_EPOCH)),        # Born along its game
            Player('Beni', Bet(0.2, 'Colombia', MOCKED_EPOCH + 180)),   # Born 3 minutes after its game was created
            Player('Lusca', Bet(10.3, 'England', MOCKED_EPOCH + 120)),   # Born 2 minutes after its game was created
            Player('Tchan', Bet(23.8, 'England', MOCKED_EPOCH + 600))    # Born 10 minutes after its game was created
        ],
        open_at=MOCKED_EPOCH,
    ),
    Game(
        teams=(Competitor('Japan'), Competitor('Mexico')),
        players=[
            Player('Lusni', Bet(28.4, 'Mexico', MOCKED_EPOCH + 3600 + 600)),   # Born 10 minutes after its game was created
            Player('Tchanga', Bet(42.0, 'Japan', MOCKED_EPOCH + 3600)),        # Born along its game
            Player('Besca', Bet(50.0, 'Japan', MOCKED_EPOCH + 3600 + 120)),    # Born 2 minutes after its game was created
            Player('Tanan', Bet(75.3, 'Mexico', MOCKED_EPOCH + 3600 + 180))    # Born 3 minutes after its game was created
        ],
        unit='Bandecos',
        open_at=MOCKED_EPOCH + 3600, # Born 1 hour after previous game
    ),
]

def create_game_from_document_ref(document_ref: firestore.DocumentReference) -> Game:
    id = document_ref.id
    document: dict = document_ref.get().to_dict()
    if not document: return None

    teams = []
    for team in document['teams']:
        team_name: str = team['name']
        team_goals: int = team['goals'] if 'goals' in team else None

        teams.append(Competitor(team_name, team_goals))
    
    players = []
    for player in document['players']:
        player_name: str = player['name']
        player_info: dict = player['bet']

        players.append(
            Player(
                player_name, 
                Bet(player_info.get('value'), player_info.get('target'), player_info.get('created_at'))
            )
        )

    return Game(
      tuple(teams),
      players,
      document['unit'],
      id,
      document['created_at'],
      document['is_open']
    )

def format_game_to_store(game: Game) -> dict:
    player_list = []
    for player in game.players:
        player_list.append(
            { 
              'name': player.name, 
              'bet': {
                'value': player.bet.value,
                'target': player.bet.target,
                'created_at': player.bet.created_at
                }
            }
        )

    team_list = [
        {'name': game.teams[0].name}, 
        {'name': game.teams[1].name}
    ]

    for i in range(2): 
      if game.teams[i].goals != None: 
        team_list[i]['goals'] = game.teams[i].goals

    return {
        'created_at': game.open_at,
        'is_open': game.is_open,
        'players': player_list,
        'teams': team_list,
        'unit': game.unit
    }

class GamesDAO:
    db = firestore.Client(project='beaster-f041b').collection('games')

    @staticmethod
    def list(open_only: bool = True) -> list[Game]:
        document_list = GamesDAO.db.list_documents()

        game_list = []
        for doc in document_list:
          game_list.append(create_game_from_document_ref(doc))

        return game_list
        
    @staticmethod
    def retrieve(id: str) -> Game:
        document_reference = GamesDAO.db.document(id).get()

        return create_game_from_document_ref(document_reference)

    @staticmethod
    def insert(game: Game) -> None:
        document_reference = GamesDAO.db.document(game.id).get()

        document_reference.set(format_game_to_store(game))

    @staticmethod
    def update(game: Game, id: str) -> None:
        document_reference = GamesDAO.db.document(id)

        document_reference.update(format_game_to_store(game))

    @staticmethod
    def delete(id: str) -> None:
        GamesDAO.db.document(id).delete()

    @staticmethod
    def close(id: str) -> None:
        document_reference = GamesDAO.db.document(id)

        document_reference.update({'is_open': False})

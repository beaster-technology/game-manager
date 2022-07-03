from copy import deepcopy

from model.game import Game
from model.competitor import Competitor
from model.player import Player
from model.bet import Bet

MOCKED_EPOCH = 1656681396.448879
MOCKED_GAME_LIST = [
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

class GamesDAO: # This guy needs to connect to firebase firestore
    def __init__(self) -> None:
        # Here you can initialize the connection
        pass

    @staticmethod
    def list(open_only: bool = True) -> list[Game]:
        # Retrieve all games
        return MOCKED_GAME_LIST

    @staticmethod
    def retrieve(id: str) -> Game:
        # Retrieve game with id
        target_game: Game = deepcopy(MOCKED_GAME_LIST[0])
        target_game.id = id

        return target_game

    @staticmethod
    def insert(game: Game) -> None:
        # Insert provided game in firestore
        pass

    @staticmethod
    def update(game: Game) -> None:
        # Update provided game in firestore
        pass

    @staticmethod
    def delete(id: str) -> None:
        # Delete game result with provided ID
        pass

    @staticmethod
    def close(id: str) -> None:
        # Close game with provided ID - set is_open to False
        pass

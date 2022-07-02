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
            Player('Tanga', Bet(10, MOCKED_EPOCH)),         # Born along its game
            Player('Beni', Bet(10, MOCKED_EPOCH + 180)),    # Born 3 minutes after its game was created
            Player('Lusca', Bet(10, MOCKED_EPOCH + 120)),   # Born 2 minutes after its game was created
            Player('Tchan', Bet(10, MOCKED_EPOCH + 600))    # Born 10 minutes after its game was created
        ],
        open_at=MOCKED_EPOCH,
    ),
    Game(
        teams=(Competitor('Japan'), Competitor('Mexico')),
        players=[
            Player('Lusni', Bet(10, MOCKED_EPOCH + 3600 + 600)),    # Born 10 minutes after its game was created
            Player('Tchanga', Bet(10, MOCKED_EPOCH + 3600)),        # Born along its game
            Player('Besca', Bet(10, MOCKED_EPOCH + 3600 + 120)),    # Born 2 minutes after its game was created
            Player('Tanan', Bet(10, MOCKED_EPOCH + 3600 + 180))     # Born 3 minutes after its game was created
        ],
        unit='Bandecos',
        open_at=MOCKED_EPOCH + 3600, # Born 1 hour after previous game
    ),
]

class GamesDAO: # This guy needs to connect to firebase firestore
    def __init__(self) -> None:
        # Here you can initialize the connection
        pass

    def list(open_only: bool = True):
        # Retrieve all games
        return MOCKED_GAME_LIST

    def retrieve(id: str):
        # Retrieve game with id
        target_game: Game = deepcopy(MOCKED_GAME_LIST[0])
        target_game.id = id

        return target_game

    def insert(game: Game):
        # Insert provided game in firestore
        pass

    def update(game: Game):
        # Update provided game in firestore
        pass

    def delete(id: str):
        # Delete game result with provided ID
        pass

    def close(id: str):
        # Close game with provided ID - set is_open to False
        pass

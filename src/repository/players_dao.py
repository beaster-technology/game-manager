from copy import deepcopy

from model.game import Game
from model.player import Player
from model.bet import Bet

MOCKED_EPOCH = 1656681396.448879
MOCKED_PLAYER_LIST = [
    Player('Tanga', Bet(10, MOCKED_EPOCH)),         # Born along its game
    Player('Beni', Bet(10, MOCKED_EPOCH + 180)),    # Born 3 minutes after its game was created
    Player('Lusca', Bet(10, MOCKED_EPOCH + 120)),   # Born 2 minutes after its game was created
    Player('Tchan', Bet(10, MOCKED_EPOCH + 600))    # Born 10 minutes after its game was created
]

class PlayersDAO: # This guy needs to connect to firebase firestore
    def __init__(self) -> None:
        # Here you can initialize the connection
        pass

    def retrieve(id: str):
        # Retrieve players with id
        return MOCKED_PLAYER_LIST

    def update(game: Game):
        # Update provided game in firestore
        pass

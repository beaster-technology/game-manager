from model.game import Game
from model.player import Player
from model.bet import Bet
from model.winner import Winner

from serializer.game_serializer import GameSerializer
from serializer.player_serializer import PlayerSerializer

MOCKED_EPOCH = 1656681396.448879
MOCKED_GAME_LIST = [
    Game(
        teams=('Brasil', 'França'),
        players=[
            Player('Tanga', Bet(10, MOCKED_EPOCH)),         # Born along its game
            Player('Beni', Bet(10, MOCKED_EPOCH + 180)),    # Born 3 minutes after its game was created
            Player('Lusca', Bet(10, MOCKED_EPOCH + 120)),   # Born 2 minutes after its game was created
            Player('Tchan', Bet(10, MOCKED_EPOCH + 600))    # Born 10 minutes after its game was created
        ],
        open_at=MOCKED_EPOCH,
    ),
    Game(
        teams=('Argentina', 'Itália'),
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
MOCKED_WINNER_LIST = [ # Created at the moment their game closed
    Winner('Tanan', Bet(50, MOCKED_EPOCH), '61be0f5f-a5c1-4e0a-92ef-686eac1e3699'),
    Winner('Besca', Bet(35, MOCKED_EPOCH), '61be0f5f-a5c1-4e0a-92ef-686eac1e3699')
]

class GameService:

    def list_games(open_only: bool=True):
        # Get list from repository
        return GameSerializer.serialize_list(MOCKED_GAME_LIST)

    def get_game(id: str):
        # TODO: Validate UUID formatting - InvalidUUID

        # TODO: Search in repository and raise unhandled exceptions - Exception
        mocked_game = MOCKED_GAME_LIST[0]
        mocked_game.id = id

        # Check zero value from repo and check for it at the controller

        return GameSerializer.serialize(mocked_game)

    def get_players(id: str):
        # TODO: Validate UUID formatting - InvalidUUID
        
        # TODO: Search in repository and raise unhandled exceptions - Exception

        # Check game existance from repo and check for it here - NotFoundException

        return PlayerSerializer.serialize_list(MOCKED_GAME_LIST[0].players)

    def get_winners(id: str):
        # TODO: Validate UUID formatting - InvalidUUID
        
        # TODO: Search in repository and raise unhandled exceptions - Exception

        # Check game existance from repo and check for it here - NotFoundException

        return PlayerSerializer.serialize_list(MOCKED_WINNER_LIST)

    def create_game(request):

        # Validate body

        # TODO: Create game in repository and raise unhandled exceptions - Exception


        return GameSerializer.serialize(MOCKED_GAME_LIST[0])

    def close_game(id):
        # TODO: Validate UUID formatting - InvalidUUID

        # TODO: Search in repository and raise unhandled exceptions - Exception

        # Make sure game exists - NotFoundException

        # TODO: Check if game is already closed - AlreadyClosedGame

        # Close game

        pass

    def update_game(id, request):
        # TODO: Validate UUID formatting - InvalidUUID

        # Make sure game exists - NotFoundException

        # TODO: Update in repository and raise unhandled exceptions - Exception

        # Update the game

        pass

    def update_players(id, request):
        # TODO: Validate UUID formatting - InvalidUUID

        # Make sure game exists - NotFoundException

        # TODO: Update game in repository and raise unhandled exceptions - Exception

        pass

    def delete_game(id):
        # TODO: Validate UUID formatting - InvalidUUID

        # TODO: Search in repository and raise unhandled exceptions - Exception

        # Make sure game exists - NotFoundException

        # Delete targeted game

        pass

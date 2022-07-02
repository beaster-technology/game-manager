from collections import namedtuple
from json import loads
from uuid import UUID
from model.game import Game
from model.competitor import Competitor
from model.player import Player
from model.bet import Bet

from serializer.game_serializer import GameSerializer
from serializer.player_serializer import PlayerSerializer

from repository.games_dao import GamesDAO
from repository.players_dao import PlayersDAO

from model.exceptions.invalid_uuid import InvalidUUID
from model.exceptions.resource_not_found import ResourceNotFound
from model.exceptions.invalid_request_payload import InvalidRequestPayload

class GameService:

    def list_games(open_only: bool=True):
        games: list[Game] = GamesDAO.list(open_only)
        return GameSerializer.serialize_list(games)

    def get_game(id: str):
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID

        game = GamesDAO.retrieve(id)
        if not game: raise ResourceNotFound

        return GameSerializer.serialize(game)

    def get_players(id: str):
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID
        
        players = PlayersDAO.retrieve(id)
        if players == '': raise ResourceNotFound

        return PlayerSerializer.serialize_list(players)

    def create_game(request):

        # Validate body

        # Generate game creation class
        game = Game((Competitor('Brasil'), Competitor('Espanha')), [])

        GamesDAO.insert(game)

        return GameSerializer.serialize(game)

    def close_game(id):
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID

        GamesDAO.close(id)

    def update_game(id, request):
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID

        # Validate game update payload

        # Build game object
        game_update = Game(('Brazil', 'Spain'), [])

        GamesDAO.update(game_update)

    def update_players(id, request):
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID

        # Validate players update payload

        # Build players objects list
        game_update = Player('Besca', Bet(10))

        PlayersDAO.update(game_update)

    def delete_game(id):
        try: _ = UUID(id, version=4)
        except ValueError: raise InvalidUUID

        GamesDAO.delete(id)
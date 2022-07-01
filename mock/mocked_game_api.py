from flask import Flask, request, Response
from copy import deepcopy
from json import dumps
from sys import path

path.append('../src')
from game import Game
from player import Player
from bet import Bet

from serializer.game_serializer import GameSerializer
from serializer.player_serializer import PlayerSerializer

app = Flask(__name__)

MOCKED_EPOCH = 1656681396.448879
MOCKED_GAME_LIST = [
    Game(
        teams = ('Brasil', 'França'),
        players = [
            Player('Tanga', Bet(10, MOCKED_EPOCH)),         # Born along its game
            Player('Beni', Bet(10, MOCKED_EPOCH + 180)),    # Born 3 minutes after its game was created
            Player('Lusca', Bet(10, MOCKED_EPOCH + 120)),   # Born 2 minutes after its game was created
            Player('Tchan', Bet(10, MOCKED_EPOCH + 600))    # Born 10 minutes after its game was created
        ],
        open_at = MOCKED_EPOCH,
    ),
    Game(
        teams = ('Argentina', 'Itália'),
        players = [
            Player('Lusni', Bet(10, MOCKED_EPOCH + 3600 + 600)),    # Born 10 minutes after its game was created
            Player('Tchanga', Bet(10, MOCKED_EPOCH + 3600)),        # Born along its game
            Player('Besca', Bet(10, MOCKED_EPOCH + 3600 + 120)),    # Born 2 minutes after its game was created
            Player('Tanan', Bet(10, MOCKED_EPOCH + 3600 + 180))     # Born 3 minutes after its game was created
        ],
        unit = 'Bandecos',
        open_at = MOCKED_EPOCH + 3600, # Born 1 hour after previous game
    ),
]

@app.route('/')
def root() -> str: return 'Mocked Beaster! :)'

@app.route('/game', methods=['GET'])
def list_games() -> list[Game]:
    serialized_games_list = GameSerializer.serialize_list(MOCKED_GAME_LIST)
    return Response(serialized_games_list, status=200, mimetype='application/json')

@app.route('/game/<id>', methods=['GET'])
def get_game(id) -> Game:
    mocked_game = deepcopy(MOCKED_GAME_LIST[0])
    mocked_game.id = id

    serialized_game = GameSerializer.serialize(mocked_game)
    return Response(serialized_game, status=200, mimetype='application/json')

@app.route('/game/<id>/player', methods=['GET'])
def get_players(id) -> list[Player]:
    serialized_players = PlayerSerializer.serialize_list(MOCKED_GAME_LIST[0].players)
    return Response(serialized_players, status=200, mimetype='application/json')

@app.route('/game', methods=['POST'])
def create_game() -> None:
    serialized_game = GameSerializer.serialize(MOCKED_GAME_LIST[0])
    return Response(serialized_game, status=201, mimetype='application/json')

@app.route('/game/<id>/close', methods=['POST'])
def close_game(id) -> None:
    return Response(status=204, mimetype='application/json')

@app.route('/game/<id>', methods=['PUT'])
def update_game(id) -> None:
    return Response(status=204, mimetype='application/json')

@app.route('/game/<id>/players', methods=['PUT'])
def update_players(id) -> None:
    return Response(status=204, mimetype='application/json')

@app.route('/game/<id>', methods=['DELETE'])
def delete_game(id) -> None:
    return Response(status=204, mimetype='application/json')

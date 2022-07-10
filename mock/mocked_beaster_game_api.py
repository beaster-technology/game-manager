from flask import Flask, request, Response
from copy import deepcopy
from json import dumps
from sys import path

path.append('../src')
from src.model.game import Game
from src.model.competitor import Competitor
from src.model.player import Player
from src.model.bet import Bet
from src.model.result import Result

from src.serializer.game_serializer import GameSerializer
from src.serializer.result_serializer import ResultSerializer

app = Flask(__name__)

MOCKED_EPOCH: int = 1656681396.448879

MOCKED_GAME_LIST: list[Game] = [
    Game(
        teams=(Competitor('Brazil'), Competitor('France')),
        players=[
            Player('Tanga', Bet(10, 'Brazil', MOCKED_EPOCH)),         # Born along its game
            Player('Beni', Bet(25, 'Brazil', MOCKED_EPOCH + 180)),    # Born 3 minutes after its game was created
            Player('Lusca', Bet(10.5, 'France', MOCKED_EPOCH + 120)),   # Born 2 minutes after its game was created
            Player('Tchan', Bet(30.0, 'Brazil', MOCKED_EPOCH + 600))    # Born 10 minutes after its game was created
        ],
        open_at=MOCKED_EPOCH,
    ),
    Game(
        teams=(Competitor('Italy', 3), Competitor('Germany', 1)),
        players=[
            Player('Lusni', Bet(10, 'Italy', MOCKED_EPOCH + 3600 + 600)),    # Born 10 minutes after its game was created
            Player('Tchanga', Bet(10.8, 'Italy', MOCKED_EPOCH + 3600)),        # Born along its game
            Player('Besca', Bet(12.5, 'Germany', MOCKED_EPOCH + 3600 + 120)),    # Born 2 minutes after its game was created
            Player('Tanan', Bet(24.1, 'Germany', MOCKED_EPOCH + 3600 + 180))     # Born 3 minutes after its game was created
        ],
        unit='Bandecos',
        open_at=MOCKED_EPOCH + 3600, # Born 1 hour after previous game
    ),
]

MOCKED_RESULT: Result = Result('61be0f5f-a5c1-4e0a-92ef-686eac1e3699', [
    Player('Tanan', Bet(50, MOCKED_EPOCH)),
    Player('Besca', Bet(35, MOCKED_EPOCH))
], 'Brazil')

@app.route('/')
def root() -> str: return 'Mocked Beaster! :)'

@app.route('/game', methods=['GET'])
def list_games() -> Response:
    serialized_game_list: str = GameSerializer.serialize_list(MOCKED_GAME_LIST)
    return Response(serialized_game_list, status=200, mimetype='application/json')

@app.route('/game/<id>', methods=['GET'])
def get_game(id) -> Response:
    mocked_game: Game = deepcopy(MOCKED_GAME_LIST[0])
    mocked_game.id = id

    serialized_game: str = GameSerializer.serialize(mocked_game)
    return Response(serialized_game, status=200, mimetype='application/json')

@app.route('/game/<id>/result', methods=['GET'])
def get_result(id) -> Response:
    serialized_result: str = ResultSerializer.serialize(MOCKED_RESULT)
    return Response(serialized_result, status=200, mimetype='application/json')

@app.route('/game', methods=['POST'])
def create_game() -> Response:
    serialized_game: str = GameSerializer.serialize(MOCKED_GAME_LIST[0])
    return Response(serialized_game, status=201, mimetype='application/json')

@app.route('/game/<id>/close', methods=['POST'])
def close_game(id) -> Response:
    return Response(status=204, mimetype='application/json')

@app.route('/game/<id>', methods=['PUT'])
def update_game(id) -> Response:
    return Response(status=204, mimetype='application/json')

@app.route('/game/<id>', methods=['DELETE'])
def delete_game(id) -> Response:
    return Response(status=204, mimetype='application/json')

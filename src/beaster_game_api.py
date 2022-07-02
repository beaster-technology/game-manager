from flask import Flask, request, Response

beaster_game_api = Flask(__name__)

from service.game_service import GameService
from service.result_service import ResultService

from model.exceptions.invalid_uuid import InvalidUUID
from model.exceptions.resource_not_found import ResourceNotFound
from model.exceptions.invalid_request_payload import InvalidRequestPayload

@beaster_game_api.route('/game', methods=['GET'])
def list_games():
    try:
        response = GameService.list_games()
        return Response(response, status=200, mimetype='application/json')
    except Exception as error_message:
        return Response(f'Unable to retrieve game list: {error_message}', status=500)

@beaster_game_api.route('/game/<id>', methods=['GET'])
def get_game(id):
    try: response = GameService.get_game(id)
    except InvalidUUID:
        return Response(f'Invalid UUID passed as parameter.', status=400)
    except ResourceNotFound:
        return Response(f'Game with id {id} not found.', status=404)
    except Exception as error_message:
        return Response(f'Unable to retrieve game list: {error_message}.', status=500)

    return Response(response, status=200, mimetype='application/json')

@beaster_game_api.route('/game/<id>/player', methods=['GET'])
def get_players(id):
    try: response = GameService.get_players(id)
    except InvalidUUID:
        return Response(f'Invalid UUID passed as parameter.', status=400)
    except ResourceNotFound:
        return Response(f'Game with id {id} not found.', status=404)
    except Exception as error_message:
        return Response(f'Unable to retrieve players: {error_message}.', status=500)

    return Response(response, status=200, mimetype='application/json')

@beaster_game_api.route('/game/<id>/result', methods=['GET'])
def get_result(id):
    try: response = ResultService.get_result(id)
    except InvalidUUID:
        return Response(f'Invalid UUID passed as parameter.', status=400)
    except ResourceNotFound:
        return Response(f'Game with id {id} not found.', status=404)
    except Exception as error_message:
        return Response(f'Unable to retrieve players: {error_message}.', status=500)

    return Response(response, status=200, mimetype='application/json')

@beaster_game_api.route('/game', methods=['POST'])
def create_game():
    try: response = GameService.create_game(request.values)
    except InvalidRequestPayload as error_message:
        return Response(f'Invalid creation request payload.', status=400)
    except Exception as error_message:
        return Response(f'Unable to create game: {error_message}.', status=500)

    return Response(response, status=201, mimetype='application/json')

@beaster_game_api.route('/game/<id>/close', methods=['POST'])
def close_game(id):
    try: GameService.close_game(id)
    except InvalidUUID:
        return Response(f'Invalid UUID passed as parameter.', status=400)
    except ResourceNotFound:
        return Response(f'Game with id {id} not found.', status=404)
    except AlreadyClosedGame:
        return Response(f'Game with id {id} is already closed.', status=400)
    except Exception as error_message:
        return Response(f'Unable to close game: {error_message}.', status=500)

    return Response(status=204)

@beaster_game_api.route('/game/<id>', methods=['PUT'])
def update_game(id):
    try: GameService.update_game(id, request.values)
    except InvalidUUID:
        return Response(f'Invalid UUID passed as parameter.', status=400)
    except InvalidRequestPayload:
        return Response(f'Invalid game update request payload.', status=400)
    except ResourceNotFound:
        return Response(f'Game with id {id} not found.', status=404)
    except Exception as error_message:
        return Response(f'Unable to update game: {error_message}.', status=500)

    return Response(status=204)

@beaster_game_api.route('/game/<id>/player', methods=['PUT'])
def update_players(id) -> None:
    try: GameService.update_players(id, request.values)
    except InvalidUUID:
        return Response(f'Invalid UUID passed as parameter.', status=400)
    except InvalidRequestPayload:
        return Response(f'Invalid players update request payload.', status=400)
    except ResourceNotFound:
        return Response(f'Game with id {id} not found.', status=404)
    except Exception as error_message:
        return Response(f'Unable to update players: {error_message}.', status=500)

    return Response(status=204)

@beaster_game_api.route('/game/<id>', methods=['DELETE'])
def delete_game(id) -> None:
    try: GameService.delete_game(id)
    except InvalidUUID:
        return Response(f'Invalid UUID passed as parameter.', status=400)
    except Exception as error_message:
        return Response(f'Unable to delete game: {error_message}.', status=500)

    return Response(status=204)

@beaster_game_api.route('/game/<id>/result', methods=['DELETE'])
def delete_result(id) -> None:
    try: ResultService.delete_result(id)
    except InvalidUUID:
        return Response(f'Invalid UUID passed as parameter.', status=400)
    except Exception as error_message:
        return Response(f'Unable to delete result: {error_message}.', status=500)

    return Response(status=204)

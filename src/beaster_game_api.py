from flask import Flask, request, Response

beaster_game_api = Flask(__name__)

from service.game_service import GameService
from service.result_service import ResultService

from model.exceptions.invalid_uuid import InvalidUUID
from model.exceptions.resource_not_found import ResourceNotFound
from model.exceptions.invalid_request_payload import InvalidRequestPayload

@beaster_game_api.route('/game', methods=['GET'])
def list_games() -> Response:
    try:
        response: str = GameService.list()
        return Response(response, status=200, mimetype='application/json')
    except Exception as error_message:
        return Response(f'Unable to retrieve game list: {error_message}', status=500)

@beaster_game_api.route('/game/<id>', methods=['GET'])
def get_game(id) -> Response:
    try: response: str = GameService.get(id)
    except InvalidUUID:
        return Response(f'Invalid UUID passed as parameter.', status=400)
    except ResourceNotFound:
        return Response(f'Game with id {id} not found.', status=404)
    except Exception as error_message:
        return Response(f'Unable to retrieve game list: {error_message}.', status=500)

    return Response(response, status=200, mimetype='application/json')

@beaster_game_api.route('/game/<id>/result', methods=['GET'])
def get_result(id) -> Response:
    try: response: str = ResultService.get(id)
    except InvalidUUID:
        return Response(f'Invalid UUID passed as parameter.', status=400)
    except ResourceNotFound:
        return Response(f'Game with id {id} not found.', status=404)
    except Exception as error_message:
        return Response(f'Unable to retrieve results: {error_message}.', status=500)

    return Response(response, status=200, mimetype='application/json')

@beaster_game_api.route('/game', methods=['POST'])
def create_game() -> Response:
    try: response: str = GameService.create(request.json)
    except InvalidRequestPayload as error_message:
        return Response(f'Invalid creation request payload: {error_message}', status=400)
    except Exception as error_message:
        return Response(f'Unable to create game: {error_message}.', status=500)

    return Response(response, status=201, mimetype='application/json')

@beaster_game_api.route('/game/<id>/close', methods=['POST'])
def close_game(id) -> Response:
    try: GameService.close(id)
    except InvalidUUID:
        return Response(f'Invalid UUID passed as parameter.', status=400)
    except ResourceNotFound:
        return Response(f'Game with id {id} not found.', status=404)
    except Exception as error_message:
        return Response(f'Unable to close game: {error_message}.', status=500)

    return Response(status=204)

@beaster_game_api.route('/game/<id>', methods=['PUT'])
def update_game(id) -> Response:
    try: GameService.update(id, request.json)
    except InvalidUUID:
        return Response(f'Invalid UUID passed as parameter.', status=400)
    except InvalidRequestPayload:
        return Response(f'Invalid game update request payload.', status=400)
    except ResourceNotFound:
        return Response(f'Game with id {id} not found.', status=404)
    except Exception as error_message:
        return Response(f'Unable to update game: {error_message}.', status=500)

    return Response(status=204)

@beaster_game_api.route('/game/<id>', methods=['DELETE'])
def delete_game(id) -> Response:
    try: GameService.delete(id)
    except InvalidUUID:
        return Response(f'Invalid UUID passed as parameter.', status=400)
    except Exception as error_message:
        return Response(f'Unable to delete game: {error_message}.', status=500)

    return Response(status=204)

@beaster_game_api.route('/game/<id>/result', methods=['DELETE'])
def delete_result(id) -> Response:
    try: ResultService.delete(id)
    except InvalidUUID:
        return Response(f'Invalid UUID passed as parameter.', status=400)
    except Exception as error_message:
        return Response(f'Unable to delete result: {error_message}.', status=500)

    return Response(status=204)

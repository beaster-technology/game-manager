from uuid import UUID
from model.game import Game

from model.exceptions.invalid_request_payload import InvalidRequestPayload
from model.exceptions.invalid_uuid import InvalidUUID

class GameValidator:

    @staticmethod
    def validate(game: Game):

        if not game.id or not game.teams or not game.players or not game.unit:
            raise InvalidRequestPayload("null fields")

        try: _ = UUID(game.id, version=4)
        except ValueError: raise InvalidUUID

        if len(game.teams) != 2: raise InvalidRequestPayload("more thant two teams playing")
            
        if any([ team.name == '' for team in game.teams ]):
            raise InvalidRequestPayload("one or both teams are unnamed")

        if any([ player.name == '' for player in game.players ]):
            raise InvalidRequestPayload("one or more players are unnamed")

        team_names: list[str] = [ competitor.name for competitor in game.teams ]
        bet_targets: list[str] = [ player.bet.target for player in game.players ]
        if any([ not bet_target in team_names for bet_target in bet_targets ]):
            raise InvalidRequestPayload("there are bets not targeting the competitors")

        if any([ player.bet.value <= 0 for player in game.players ]):
            raise InvalidRequestPayload("there are null or negative bets")

        if game.unit == '': raise InvalidRequestPayload("unit can't be empty")

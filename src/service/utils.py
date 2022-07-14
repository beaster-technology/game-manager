from typing import Union

from src.model.game import Game
from src.model.competitor import Competitor
from src.model.player import Player
from src.model.bet import Bet

def to_game(request_body: dict[str, Union[str, float, int, bool]]) -> Game:
    return Game(
        teams=[
            Competitor(
                team['name'],
                team['goals'] if 'goals' in team else None
            ) for team in request_body['teams']
        ],
        players=[
            Player(
                player['name'],
                Bet(
                    player['bet']['value'],
                    player['bet']['target']
                )
            ) for player in request_body['players']
        ],
        unit=request_body['unit']
    )

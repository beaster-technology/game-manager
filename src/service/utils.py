from model.game import Game
from model.competitor import Competitor
from model.player import Player
from model.bet import Bet

def to_game(request_body):
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

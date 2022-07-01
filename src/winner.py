from player import Player
from bet import Bet

class Winner(Player):
    def __init__(self, name: str, earned_bet: Bet) -> None:
        super().__init__(name, earned_bet)
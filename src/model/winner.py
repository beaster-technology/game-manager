from model.player import Player
from model.bet import Bet

class Winner(Player):
    def __init__(self, name: str, earned_bet: Bet, won_game_id: str) -> None:
        super().__init__(name, earned_bet)
        self.game_id = won_game_id
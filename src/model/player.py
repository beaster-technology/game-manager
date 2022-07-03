from model.bet import Bet

class Player:
    def __init__(self, name: str, bet: Bet) -> None:
        self.name: str = name
        self.bet: Bet = bet
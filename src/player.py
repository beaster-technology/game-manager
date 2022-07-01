from bet import Bet

class Player:
    def __init__(self, name: str, bet: Bet) -> None:
        self.name = name
        self.bet = bet
from model.player import Player

class Result:
    def __init__(self, id: str, winners: list[Player], champion: str) -> None:
        self.id: str = id
        self.winners: list[Player] = winners
        self.champion: str = champion
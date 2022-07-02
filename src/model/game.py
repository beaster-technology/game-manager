from time import time
from uuid import uuid4

from model.player import Player
from model.competitor import Competitor

class Game:
    def __init__(
        self,
        teams: tuple[Competitor, Competitor],
        players: list[Player],
        unit: str = 'Beastcoins',
        id: str = None,
        open_at: float = None,
        is_open: bool = True
    ) -> None:
        self.id = id if id else str(uuid4())
        self.open_at = open_at if open_at else time()
        self.teams = teams
        self.players = players
        self.unit = unit
        self.is_open = is_open

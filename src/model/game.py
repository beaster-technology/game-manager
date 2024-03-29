from time import time
from uuid import uuid4

from src.model.player import Player
from src.model.competitor import Competitor

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
        self.id: str = id if id else str(uuid4())
        self.open_at: float = open_at if open_at else time()
        self.teams: tuple[Competitor, Competitor] = teams
        self.players: list[Player] = players
        self.unit: str = unit
        self.is_open: bool = is_open

    def game_is_tie(self) -> bool:
      return self.teams[0].goals == self.teams[1].goals
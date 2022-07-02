from time import time
from uuid import uuid4

from model.player import Player

class Game:
    def __init__(
        self,
        teams: tuple[str, str],
        players: list[Player],
        unit: str = 'Beastcoins',
        id: str = str(uuid4()),
        open_at: float = time(),
        is_open: bool = True
    ) -> None:
        self.id = id
        self.teams = teams
        self.players = players
        self.unit = unit
        self.open_at = open_at
        self.is_open = is_open

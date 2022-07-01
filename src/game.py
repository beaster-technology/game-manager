from time import time
from uuid import uuid4
from json import dumps

from player import Player

class Game:
    def __init__(
        self,
        teams: tuple[str],
        players: list[Player],
        unit: str = 'Beastcoin',
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

    def toJSON(self): return dumps(self, default = lambda attribute: attribute.__dict__)
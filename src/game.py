from time import time
from uuid import uuid4
from json import dumps

from player import Player

class Game:
    def __init__(
        self,
        id: str = str(uuid4()),
        players: list[Player] = [],
        open_at: float = time(),
        is_open: bool = True
    ) -> None:
        self.id = id
        self.players = players
        self.open_at = open_at
        self.is_open = is_open

    def toJSON(self): return dumps(self, default = lambda attribute: attribute.__dict__)
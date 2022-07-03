from time import time

class Bet:
    def __init__(self, value: float, target: str, created_at: float = time()) -> None:
        self.value: float = value
        self.target: str = target
        self.created_at: float = created_at
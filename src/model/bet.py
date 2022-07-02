from time import time

class Bet:
    def __init__(self, value: float, target: str, created_at: float = time()) -> None:
        self.value = value
        self.target = target
        self.created_at = created_at
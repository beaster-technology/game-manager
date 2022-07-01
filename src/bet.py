from time import time

class Bet:
    def __init__(self, value: int, created_at: float = time()) -> None:
        self.value = value
        self.created_at = created_at
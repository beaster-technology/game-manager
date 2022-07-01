from time import time

class Bet:
    def __init__(self, units: int, betted_on: float = time()) -> None:
        self.value = units
        self.created_at = betted_on
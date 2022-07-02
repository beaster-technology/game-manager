from typing import Optional

class Competitor:
    def __init__(self, name: str, goals: int = None) -> None:
        self.name: str = name
        self.goals: Optional[int] = goals
class InvalidCloseGame(Exception):
    def __init__(self, message: str = 'could not close game with unregistered goals.') -> None:
        self.message: str = message
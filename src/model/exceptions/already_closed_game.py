class AlreadyClosedGame(Exception):
    def __init__(self, message: str = 'failure trying to close already closed session.') -> None:
        self.message: str = message
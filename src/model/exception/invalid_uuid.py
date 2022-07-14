class InvalidUUID(Exception):
    def __init__(self, message: str = 'invalid UUID received.') -> None:
        self.message: str = message
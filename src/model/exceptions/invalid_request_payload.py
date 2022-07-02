class InvalidRequestPayload(Exception):
    def __init__(self, message: str = 'invalid update request payload received.') -> None:
        self.message: str = message
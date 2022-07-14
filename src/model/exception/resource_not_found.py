class ResourceNotFound(Exception):
    def __init__(self, message: str = 'could not found requested resource.') -> None:
        self.message: str = message
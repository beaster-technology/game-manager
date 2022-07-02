from model.game import Game

class GamesDAO: # This guy needs to connect to firebase firestore
    def __init__(self) -> None:
        # Here you can initialize the connection
        pass

    def retrieve(id: str):
        # Retrieve game with id
        pass

    def list(open_only: bool = True):
        # Retrieve all games
        pass

    def insert(game: Game):
        # Insert provided game in firestore
        pass

    def update(game: Game):
        # Update provided game in firestore
        pass

    def delete(id: str):
        # Delete game result with provided ID
        pass

    def close(id: str):
        # Close game with provided ID - set is_open to False
        pass

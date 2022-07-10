from src.model.game import Game
from src.model.result import Result
from src.model.competitor import Competitor
from src.model.player import Player
from src.model.bet import Bet

MOCKED_EPOCH: float = 1656681396.448879

MOCKED_GAME: Game = Game(
    teams=(Competitor('Colombia', 7), Competitor('England', 3)),
    players=[
        Player('Tanga', Bet(7, 'Colombia', MOCKED_EPOCH)),        # Born along its game
        Player('Beni', Bet(3, 'Colombia', MOCKED_EPOCH + 180)),   # Born 3 minutes after its game was created
        Player('Lusca', Bet(67.45, 'England', MOCKED_EPOCH + 120)),   # Born 2 minutes after its game was created
        Player('Tchan', Bet(22.55, 'England', MOCKED_EPOCH + 600))    # Born 10 minutes after its game was created
    ],
    open_at=MOCKED_EPOCH,
)

MOCKED_WINNER: str = 'Colombia'

MOCKED_RESULT = Result('61be0f5f-a5c1-4e0a-92ef-686eac1e3699', [
    Player('Tanan', Bet(50, 'Brazil')),
    Player('Besca', Bet(35, 'Brazil'))
], 'Brazil')

MOCKED_GAME_LIST = [
    Game(
        teams=(Competitor('Colombia', 2), Competitor('England', 3)),
        players=[
            Player('Tanga', Bet(12.1, 'Colombia', MOCKED_EPOCH)),        # Born along its game
            Player('Beni', Bet(0.2, 'Colombia', MOCKED_EPOCH + 180)),   # Born 3 minutes after its game was created
            Player('Lusca', Bet(10.3, 'England', MOCKED_EPOCH + 120)),   # Born 2 minutes after its game was created
            Player('Tchan', Bet(23.8, 'England', MOCKED_EPOCH + 600))    # Born 10 minutes after its game was created
        ],
        open_at=MOCKED_EPOCH,
    ),
    Game(
        teams=(Competitor('Japan'), Competitor('Mexico')),
        players=[
            Player('Lusni', Bet(28.4, 'Mexico', MOCKED_EPOCH + 3600 + 600)),   # Born 10 minutes after its game was created
            Player('Tchanga', Bet(42.0, 'Japan', MOCKED_EPOCH + 3600)),        # Born along its game
            Player('Besca', Bet(50.0, 'Japan', MOCKED_EPOCH + 3600 + 120)),    # Born 2 minutes after its game was created
            Player('Tanan', Bet(75.3, 'Mexico', MOCKED_EPOCH + 3600 + 180))    # Born 3 minutes after its game was created
        ],
        unit='Bandecos',
        open_at=MOCKED_EPOCH + 3600, # Born 1 hour after previous game
    ),
]
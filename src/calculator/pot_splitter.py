from src.model.player import Player
from src.model.bet import Bet

class PotSplitter:
    def calculate_pot_distribution(players: list[Player], champion: str) -> list[Player]:
        absolute_pot: float = sum(player.bet.value for player in players)

        winners: list[Player] = list(filter(lambda player: player.bet.target == champion, players))
        winners_pot: float = sum(player.bet.value for player in winners)

        distribution: list[Player] = [
            Player(
                winner.name,
                Bet(
                    absolute_pot * (winner.bet.value / winners_pot),
                    winner.bet.target,
                    winner.bet.created_at
                )
            )
            for winner in winners
        ]

        return distribution

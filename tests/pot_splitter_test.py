import unittest as ut

from src.calculator.pot_splitter import PotSplitter
from fixtures import *

class PotSplitterTest(ut.TestCase):

    def testFullyPotDistribution(self):
        absolute_pot: float = sum(player.bet.value for player in MOCKED_GAME.players)

        distribution: list[Player] = PotSplitter.calculate_pot_distribution(
            MOCKED_GAME.players, MOCKED_WINNER
        )

        self.assertEqual(absolute_pot, sum(winner.bet.value for winner in distribution))
        
    def testProportionalPotDistribution(self):
        absolute_pot: float = sum(player.bet.value for player in MOCKED_GAME.players)

        winners: list[Player] = list(filter(
            lambda player: player.bet.target == MOCKED_WINNER,
            MOCKED_GAME.players
        ))
        winners_pot: float = sum(player.bet.value for player in winners)

        distribution: list[Player] = PotSplitter.calculate_pot_distribution(
            MOCKED_GAME.players, MOCKED_WINNER
        )

        for i in range(len(winners)):
            self.assertEqual(
                absolute_pot * (MOCKED_GAME.players[i].bet.value / winners_pot),
                distribution[i].bet.value
            )

    def testWinnersOnlyPotDistribution(self):
        loser_players: list[str] = list(filter(
            lambda player: player.bet.target != MOCKED_WINNER,
            MOCKED_GAME.players
        ))

        losers: list[str] = [ player.name for player in loser_players ]

        winner_players: list[Player] = PotSplitter.calculate_pot_distribution(
            MOCKED_GAME.players, MOCKED_WINNER
        )
        winners: list[str] = [ player.name for player in winner_players ]

        self.assertTrue(all(not loser in winners for loser in losers))

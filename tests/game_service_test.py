import unittest as ut
from src.service.game_service import GameService

from src.model.exception.invalid_uuid import InvalidUUID
from tests.fixtures import MOCKED_GAME

class GameServiceTest(ut.TestCase):
    
    def testInvalidUUIDErrorOnRetrieval(self):
        with self.assertRaises(InvalidUUID) as context:
            GameService.get('invalid UUID here')

    def testInvalidUUIDErrorOnClosure(self):
        with self.assertRaises(InvalidUUID) as context:
            GameService.close('invalid UUID here')

    def testInvalidUUIDErrorOnUpdate(self):
        with self.assertRaises(InvalidUUID) as context:
            GameService.update('invalid UUID here', MOCKED_GAME)

    def testInvalidUUIDErrorOnDeletion(self):
        with self.assertRaises(InvalidUUID) as context:
            GameService.delete('invalid UUID here')

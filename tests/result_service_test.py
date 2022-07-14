import unittest as ut
from src.service.result_service import ResultService

from src.model.exception.invalid_uuid import InvalidUUID


class ResultServiceTest(ut.TestCase):
    def testInvalidUUIDErrorOnRetrieval(self):
        with self.assertRaises(InvalidUUID) as context:
            ResultService.get('invalid UUID here')

    def testInvalidUUIDErrorOnDeletion(self):
        with self.assertRaises(InvalidUUID) as context:
            ResultService.delete('invalid UUID here')

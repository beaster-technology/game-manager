from copy import deepcopy
from json import dumps

from model.result import Result

class ResultSerializer:

    @staticmethod
    def serialize(result: Result):
        serialized_result: str = deepcopy(result)
        for winner in serialized_result.winners: winner.bet = vars(winner.bet)
        serialized_result.winners = [vars(winner) for winner in serialized_result.winners]
        return dumps(vars(serialized_result))

    @staticmethod
    def serialize_list(results: list[Result]):
        serialized_results_list: list[Result] = deepcopy(results)
        for result in serialized_results_list:
            for winner in result.winners: winner.bet = vars(winner.bet)
            result.winners = [vars(winner) for winner in result.winners]
        serialized_results_list = [vars(result) for result in serialized_results_list]

        return dumps(serialized_results_list)

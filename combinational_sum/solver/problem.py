from typing import List


class CombinationalSumProblem:
    def __init__(self, target: float, available_values: List[float]):
        self.target = target
        self.available_values = available_values

    @staticmethod
    def from_strings(target_string: str, values_str: str):
        values = []
        for item in values_str.replace(" ", "").split(","):
            values.append(float(item))
        return CombinationalSumProblem(float(target_string), values)

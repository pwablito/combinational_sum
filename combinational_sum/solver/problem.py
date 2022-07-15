from typing import Dict


class CombinationalSumProblem:
    def __init__(self, target: float, options: Dict[str, float]):
        self.target = target
        self.options = options

    @staticmethod
    def from_strings(target_string: str, values_str: str):
        values = []
        for item in values_str.replace(" ", "").split(","):
            values.append(float(item))
        return CombinationalSumProblem(float(target_string), values)

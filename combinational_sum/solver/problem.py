from typing import Dict


class CombinationalSumProblem:
    def __init__(self, target: float, options: Dict[str, float]):
        self.target = target
        self.options = options

    @staticmethod
    def from_strings(target_string: str, values_str: str):
        values = {}
        counter = 1
        for item in values_str.replace(" ", "").split("\n"):
            values[f"{counter} ({item})"] = float(item.replace("$", ""))
            counter += 1
        return CombinationalSumProblem(float(target_string), values)

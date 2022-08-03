from combinational_sum.solver.problem import CombinationalSumProblem
from combinational_sum.solver.solution import CombinationalSumSolution

from typing import List, Dict
import math
import statistics


class CombinationalSumSolver:
    def __init__(self, problem: CombinationalSumProblem):
        self.problem = problem

    def solve(self) -> CombinationalSumSolution:
        all_solutions: List[Dict[str, int]] = []
        self.gather_solutions({}, all_solutions)
        optimal = self.find_optimal(all_solutions)
        return CombinationalSumSolution(optimal)

    def gather_solutions(self, state: Dict[str, int], all_solutions: List[Dict[str, int]]) -> None:
        if self.state_sum(state) == self.problem.target and state not in all_solutions:
            all_solutions.append(state)
        elif self.state_sum(state) < self.problem.target:
            for key, value in self.problem.options.items():
                if value != 0.0:
                    new_state = state.copy()
                    if key not in new_state:
                        new_state[key] = 0
                    new_state[key] += 1
                    self.gather_solutions(new_state, all_solutions)

    def state_sum(self, state: Dict[str, int]):
        total = 0
        for key, value in state.items():
            total += (self.problem.options[key] * value)
        return total

    def find_optimal(self, possible_solutions: List[Dict[str, int]]) -> Dict[str, int]:
        # TODO account for cases where score is perfect but solution is missing items
        best_solution = None
        best_score = math.inf
        for solution in possible_solutions:
            solution_score = self.get_score(solution)
            if best_score > solution_score:
                best_score = solution_score
                best_solution = solution
        return best_solution

    def get_score(self, solution: Dict[str, int]) -> float:
        counts = {key: 0 for key in self.problem.options.keys()}
        for name, count in solution.items():
            counts[name] += count
        median = statistics.median(counts.values())
        score = 0
        for count in counts.values():
            score += abs(count - median)
        return score

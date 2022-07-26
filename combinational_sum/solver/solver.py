from combinational_sum.solver.problem import CombinationalSumProblem
from combinational_sum.solver.solution import CombinationalSumSolution

from typing import List, Dict
import math


class CombinationalSumSolver:
    def __init__(self, problem: CombinationalSumProblem):
        self.problem = problem

    def solve(self) -> CombinationalSumSolution:
        all_solutions: List[Dict[str, int]] = []
        self.gather_solutions({}, all_solutions)
        return self.find_optimal(all_solutions)

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
        best_solution = None
        best_score = math.inf
        for solution in possible_solutions:
            solution_score = self.get_score(solution)
            if best_score > solution_score:
                best_score = solution_score
                best_solution = solution
        return best_solution

    def get_score(self, solution: Dict[str, int]):
        counts = {key: 0 for key in self.problem.options.keys()}
        for name, count in solution:
            counts[name] += count
        median = math.median(counts.values())
        score = 0
        for item in counts:
            score += math.abs(item - median)

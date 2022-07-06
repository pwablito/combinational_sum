from combinational_sum.solver.problem import CombinationalSumProblem
from combinational_sum.solver.solution import CombinationalSumSolution

from typing import List


class CombinationalSumSolver:
    def __init__(self, problem: CombinationalSumProblem):
        self.problem = problem

    def solve(self) -> CombinationalSumSolution:
        all_solutions: List[List[float]] = []
        self.gather_solutions([], all_solutions)
        optimal_solution: List[float] = self.find_optimal(all_solutions)
        # TODO convert optimal_solution to CombinationalSumSolution

    def gather_solutions(self, state: List[float], all_solutions: List[float]) -> None:
        if sum(state.values) == self.problem.target:
            all_solutions.append(state)
        elif sum(state.values) < self.problem.target:
            for item in self.problem.available_values.filter(lambda x: x != 0.0):
                new_state = state
                new_state.append(item)
                self.gather_solutions(new_state, all_solutions)

    def find_optimal(self, possible_solutions: List[List[float]]) -> List[float]:
        raise NotImplementedError

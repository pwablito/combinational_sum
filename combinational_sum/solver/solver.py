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

    def gather_solutions(self, state: List[float], all_solutions: List[List[float]]) -> None:
        if sum(state) == self.problem.target:
            all_solutions.append(state)
        elif sum(state) < self.problem.target:
            for item in filter(lambda x: x != 0.0, self.problem.available_values):
                new_state = state
                new_state.append(item)
                self.gather_solutions(new_state, all_solutions)

    def find_optimal(self, possible_solutions: List[List[float]]) -> List[float]:
        # TODO find the option that is the most even between the possibilities
        raise NotImplementedError

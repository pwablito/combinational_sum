from combinational_sum.solver.problem import CombinationalSumProblem
from combinational_sum.solver.solution import CombinationalSumSolution


class CombinationalSumSolver:
    def __init__(self, problem: CombinationalSumProblem):
        self.problem = problem

    def solve(self) -> CombinationalSumSolution:
        raise NotImplementedError

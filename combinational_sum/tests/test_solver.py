from combinational_sum.solver.problem import CombinationalSumProblem
from combinational_sum.solver.solver import CombinationalSumSolver


def test_gather_solutions():
    problem = CombinationalSumProblem(
        10.0,
        [5.0, 4.0, 1.0]
    )
    solver = CombinationalSumSolver(problem)
    all_solutions = []
    solver.gather_solutions([], all_solutions)
    assert len(all_solutions)
    assert [5.0, 4.0, 1.0] in all_solutions


def test_find_optimal():
    raise NotImplementedError

from combinational_sum.solver.problem import CombinationalSumProblem
from combinational_sum.solver.solver import CombinationalSumSolver


def test_gather_solutions():
    problem = CombinationalSumProblem(
        10.0,
        {
            "item1": 5.0,
            "item2": 4.0,
            "item3": 1.0,
        }
    )
    solver = CombinationalSumSolver(problem)
    all_solutions = []
    solver.gather_solutions({}, all_solutions)
    assert len(all_solutions)
    assert {
        "item1": 1,
        "item2": 1,
        "item3": 1,
    } in all_solutions


def test_find_optimal():
    raise NotImplementedError

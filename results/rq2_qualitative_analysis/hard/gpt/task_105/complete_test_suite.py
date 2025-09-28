from llm_output import solve_problem


def check(candidate):
    assert solve_problem("1\n2\n1 2") == "6"


check(solve_problem)
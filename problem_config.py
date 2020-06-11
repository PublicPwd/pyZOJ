from programming_problem_config import ProgrammingProblemConfig


class ProblemConfig:
    ProgrammingProblemConfig = ProgrammingProblemConfig
    SolutionVisible = None

    def __init__(self, programming_problem_config, solution_visible):
        self.ProgrammingProblemConfig = programming_problem_config
        self.SolutionVisible = solution_visible

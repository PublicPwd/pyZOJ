import json
import time

import problem
import problem_info
from problem_type import ProblemType

for i in range(0, 1):
    items = problem_info.get_list(i, 100, ProblemType.Programming)
    for item in items:
        p = problem.get(item.ProblemSetID, item.ID)
        print(p.Title)
        time.sleep(2)

import json

import requests

from author_organization import AuthorOrganization
from example_test_data import ExampleTestData
from problem_config import ProblemConfig
from programming_problem_config import ProgrammingProblemConfig


class Problem:
    ID = None
    Label = None
    Score = None
    ProblemConfig = ProblemConfig
    Deadline = None
    Title = None
    Content = None
    Type = None
    Author = None
    AuthorOrganization = AuthorOrganization
    compiler = None
    ProblemStatus = None
    LastSubmissionID = None
    Solution = None
    ProblemSetID = None
    ProblemID = None
    Description = None

    def __init__(self, id, label, score, problem_config, deadline, title,
                 content, type, author, author_organization, compiler,
                 problem_status, last_submission_id, solution, problem_set_id,
                 problem_id, description):
        self.ID = id
        self.Label = label
        self.Score = score
        self.ProblemConfig = problem_config
        self.Deadline = deadline
        self.Title = title
        self.Content = content
        self.Type = type
        self.Author = author
        self.AuthorOrganization = author_organization
        self.compiler = compiler
        self.ProblemStatus = problem_status
        self.LastSubmissionID = last_submission_id
        self.Solution = solution
        self.ProblemSetID = problem_set_id
        self.ProblemID = problem_id
        self.Description = description


def get(problem_set_id, id):
    """
    获取问题详情
    :param problem_set_id: 问题集 ID
    :param id: 问题 ID
    """
    headers = {"Accept": "application/json;charset=UTF-8"}
    url = "https://pintia.cn/api/problem-sets/{0}/problems/{1}".format(
        problem_set_id, id)
    res = requests.get(url, headers=headers)
    item = json.loads(res.text)["problemSetProblem"]

    example_test_datas_items = item["problemConfig"][
        "programmingProblemConfig"]["exampleTestDatas"]
    example_test_datas = []
    for i in example_test_datas_items:
        e = ExampleTestData(i["name"], i["input"], i["output"])
        example_test_datas.append(e)

    i = item["problemConfig"]["programmingProblemConfig"]
    programming_problem_config = ProgrammingProblemConfig(
        i["timeLimit"], i["memoryLimit"], i["codeSizeLimit"], i["cases"],
        example_test_datas, i["testdataDescriptionCode"], i["customizeLimits"],
        i["stackSizeLimit"])

    i = item["problemConfig"]
    problem_config = ProblemConfig(programming_problem_config,
                                   i["solutionVisible"])

    i = item["authorOrganization"]
    author_organization = AuthorOrganization(i["id"], i["name"], i["comment"],
                                             i["code"], i["country"],
                                             i["membersCount"], i["type"],
                                             i["balance"], i["subdomain"],
                                             i["logo"])

    probelm = Problem(item["id"], item["label"], item["score"], problem_config,
                      item["deadline"], item["title"], item["content"],
                      item["type"], item["author"], author_organization,
                      item["compiler"], item["problemStatus"],
                      item["lastSubmissionId"], item["solution"],
                      item["problemSetId"], item["problemId"],
                      item["description"])
    return probelm

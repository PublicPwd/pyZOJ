import json

import requests


class ProblemInfo:
    ID = None
    Label = None
    Score = None
    Deadline = None
    AcceptCount = None
    SubmitCount = None
    Title = None
    Type = None
    Compiler = None
    ProblemStatus = None
    ProblemSetID = None

    def __init__(self, id, label, score, deadline, accept_count, submit_count,
                 title, type, compiler, problem_status, problem_set_id):
        self.ID = id
        self.Label = label
        self.Score = score
        self.Deadline = deadline
        self.AcceptCount = accept_count
        self.SubmitCount = submit_count
        self.Title = title
        self.Type = type
        self.Compiler = compiler
        self.ProblemStatus = problem_status
        self.ProblemSetID = problem_set_id


def get_list(page, limit, problem_type):
    """
    获取问题列表
    :param page: 页数（从 0 开始）
    :param limit: 每页个数
    :param problem_type: 问题类型
    """
    headers = {"Accept": "application/json;charset=UTF-8"}
    url = "https://pintia.cn/api/problem-sets/91827364500/problem-list"
    params = {"page": page, "limit": limit, "problem_type": problem_type}
    res = requests.get(url, headers=headers, params=params)
    items = json.loads(res.text)["problemSetProblems"]
    list = []
    for item in items:
        info = ProblemInfo(item["id"], item["label"], item["score"],
                           item["deadline"], item["acceptCount"],
                           item["submitCount"], item["title"], item["type"],
                           item["compiler"], item["problemStatus"],
                           item["problemSetId"])
        list.append(info)
    return list

class ProgrammingProblemConfig:
    TimeLimit = None
    MemoryLimit = None
    CodeSizeLimit = None
    Cases = None
    ExampleTestDatas = []
    TestDataDescriptionCode = None
    CustomizeLimits = None
    StackSizeLimit = None

    def __init__(self, time_limit, memory_limit, code_size_limit, cases,
                 example_test_datas, test_data_description_code,
                 customize_limits, stack_size_limit):
        self.TimeLimit = time_limit
        self.MemoryLimit = memory_limit
        self.CodeSizeLimit = code_size_limit
        self.Cases = cases
        self.ExampleTestDatas = example_test_datas
        self.CustomizeLimits = customize_limits
        self.StackSizeLimit = stack_size_limit

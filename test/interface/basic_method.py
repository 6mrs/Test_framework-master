class TestCaseKeyWord(object):
    """
    定义测试用例关键字类
    """

    CASE_ID = '0'
    NAME = '1'
    EXECUTE = '2'
    METHOD = '3'
    URL = '4'
    HEADERS = '5'
    DATA = '6'
    EXPECTED = '7'
    ACTUAL = '8'


# 获取用例id
def get_case_id():
    return TestCaseKeyWord.CASE_ID


# 获取用例名称
def get_case_name():
    return TestCaseKeyWord.NAME


# 用例是否执行
def get_case_is_execute():
    return TestCaseKeyWord.EXECUTE


# 用例方法
def get_case_method():
    return TestCaseKeyWord.METHOD


# 接口url
def get_case_interface_url():
    return TestCaseKeyWord.URL


# 请求头
def get_case_header():
    return TestCaseKeyWord.HEADERS


# 请求参数
def get_case_payload():
    return TestCaseKeyWord.DATA


# 预期结果
def get_case_expected_result():
    return TestCaseKeyWord.EXPECTED


# 实际结果
def get_case_actual_result():
    return TestCaseKeyWord.ACTUAL


if __name__ == '__main__':
    print(get_case_id())
    print(get_case_is_execute())

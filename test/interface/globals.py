from test.interface.manageexcel import ReadExcel

CASE_NUMBER = 0  # 用例编号
CASE_NAME = 1  # 用例名称
CASE_METHOD = 2  # 请求类型
CASE_URL = 3  # 请求地址
CASE_DATA = 4  # 用例数据
CASE_STATUS = 5  # 用例状态
CASE_KEY = 6  # 验证关键字

file_path = "/Users/youjia/Desktop/Test_framework-master/data/api_data.xlsx"
# host = "http://localhost:5000"
row_num = ReadExcel(file_path).getRows


class CASE:
    number = ReadExcel(file_path).getName(CASE_NUMBER)
    name = ReadExcel(file_path).getName(CASE_NAME)
    method = ReadExcel(file_path).getName(CASE_METHOD)
    url = ReadExcel(file_path).getName(CASE_URL)
    data = ReadExcel(file_path).getName(CASE_DATA)
    status = ReadExcel(file_path).getName(CASE_STATUS)
    key = ReadExcel(file_path).getName(CASE_KEY)

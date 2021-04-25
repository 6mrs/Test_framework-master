import json
import unittest

from test.common.get_token import get_token
from test.interface.get_keyword import getData
from test.interface.method import ApiRequest
from test.interface.read_excel import Operate_Excel


class excelTest(unittest.TestCase):

    def test_login(self):

        read_xls = Operate_Excel(sheet_id=0)
        get_data = getData()
        for i in range(1, 7):
            print("测试名称： ", get_data.get_name(i))
            print("是否运行key： ", get_data.get_is_run(i))
            print("请求头： ", get_data.get_is_header(i))
            print("接口url： ", get_data.get_url(i))
            print("接口请求方法： ", get_data.get_method(i))
            print("接口请求数据： ", get_data.get_data(i))

            name = get_data.get_name(i)
            header = get_data.get_is_header(i)
            url = get_data.get_url(i)
            method = get_data.get_method(i)
            data = get_data.get_data(i)

            ir2 = ApiRequest()

            result = ir2.run_method(url=url, method=method, header=header, data=data.encode('utf-8'))
            print("运行返回数据为：", result)
            if (json.loads(result)["code"] == 0):
                print(read_xls.write_to_excel(i, 8, '成功'))
            else:
                print(read_xls.write_to_excel(i, 8, '失败'))

    def test_userinfo(self):

        read_xls = Operate_Excel()
        get_data = getData()
        header = {"Content-Type": "application/Json", "app-token": get_token()}
        for i in range(13, 14):
            print("测试名称： ", get_data.get_name(i))
            print("是否运行key： ", get_data.get_is_run(i))
            print("请求头： ", header)
            print("接口url： ", get_data.get_url(i))
            print("接口请求方法： ", get_data.get_method(i))
            print("接口请求数据： ", get_data.get_data(i))

            name = get_data.get_name(i)
            url = get_data.get_url(i)
            method = get_data.get_method(i)
            data = get_data.get_data(i)
            ir2 = ApiRequest()
            result = ir2.run_method(url=url, method=method, header=header, data=data.encode('utf-8'))
            print("运行返回数据为：", result)
            if (json.loads(result)["code"] == 0):
                print(read_xls.write_to_excel(i, 8, '成功'))
            else:
                print(read_xls.write_to_excel(i, 8, '失败'))


if __name__ == '__main__':
    unittest.main()

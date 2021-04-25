import unittest
import requests
import json

from test.common.get_admintoken import get_admintoken
from test.common.get_token import get_token
from utils.log import logger


class TestInterface(unittest.TestCase):
    def setUp(self):  # 初始化
        self.t = globals()
        self.base1_url = 'http://test.dr.loc/api/order/userOrder/pageOrderByType'

    def test_page(self):  # admin分页查询app用户信息

        data = {
            "current": 0,
            "entity": {
                "endTime": "2021-01-04T06:27:25.359Z",
                "orderType": "string",
                "payType": "string",
                "shopOrderId": 0,
                "signPhone": 0,
                "startTime": "2021-01-04T06:27:25.359Z",
                "status": 2
            },
            "orders": [
                {
                    "asc": "true",
                    "column": "string"
                }
            ],
            "size": 0
        }

        head = {"Content-Type": "application/Json", "app-token": get_admintoken()}
        r = requests.post(self.base1_url, json=data, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base1_url)
        print("返回数据为......:", result)
        # jsr = json.loads(result)
        # userid = jsr['data']['id']
        # self.t['userid'] = userid
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_getMsg(self):  # admin查看用户信息

        data = {
            "ids":
                2762335240897771521
        }

        head = {"Content-Type": "application/Json"}
        r = requests.post(self.base1_url, json=data, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base1_url)
        print("返回数据为......:", result)
        # jsr = json.loads(result)
        # userid = jsr['data']['id']
        # self.t['userid'] = userid
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_updateMsy(self):  # admin修改用户信息

        data = {
            "avator": "",
            "deptId": "",
            "id": 2766714085496637441,
            "inviterId": 0,
            "label": "",
            "linkAddr": "",
            "name": "测试修改",
            "openid": "",
            "phone": "121221123113131312",
            "pwd": "",
            "role": "",
            "sex": 1,
            "sign": "",
            "status": 1,
            "top": 0
        }

        head = {"Content-Type": "application/Json"}
        r = requests.post(self.base2_url, json=data, headers=head)
        result = json.loads(r.text)  # 使用json格式返回
        print("headers信息...:", head)
        print("请求地址.......:", self.base2_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_remove(self):  # admin删除用户信息

        data = {
            "ids": [2762335240897771522]
        }
        head = {"Content-Type": "application/Json"}
        r = requests.post(self.base3_url, json=data, headers=head)
        result = json.loads(r.text)  # 使用json格式返回
        print("headers信息...:", head)
        print("请求地址.......:", self.base3_url)
        print("请求地址.......:", self.base3_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)


if __name__ == '__main__':
    unittest.main()

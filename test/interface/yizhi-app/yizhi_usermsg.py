import json
import unittest

import requests

from test.common.get_token import get_token
from utils.log import logger


class TestFans(unittest.TestCase):
    def setUp(self):
        self.url1 = 'http://dev.dr.loc/api/app-user/app/userPrivMsg/add'
        self.url2 = 'http://test.dr.loc/api/app-user/app/userPrivMsg/get'
        self.url3 = 'http://test.dr.loc/api/app-user/app/userPrivMsg/page'
        self.url4 = 'http://test.dr.loc/api/app-user/app/userPrivMsg/remove'
        self.url5 = 'http://test.dr.loc/api/app-user/app/userPrivMsg/count'

    def test_addMsg(self):  # app发私信
        data = {
            "msg": {
                "data": "hello哈哈哈哈哈哈哈、",
                "type": "1"
            },
            "recUserId": 2768483002515404801  # id：2762327263629356033
        }
        header = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.url1, json=data, headers=header)
        result = json.loads(r.text)
        print("headers信息...:", header)
        print("请求地址.......:", self.url1)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_getMsg(self):  # app查看和默认的私信内容列表
        data = {
            "current": 0,
            "entity": {
                "recUserId": [
                    2768788935397508097
                ]
            },
            "orders": [
                {
                    "asc": "true",
                    "column": ""
                }
            ],
            "size": 0
        }
        header = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.url2, json=data, headers=header)
        result = json.loads(r.text)
        print("headers信息...:", header)
        print("请求地址.......:", self.url2)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_getPage(self):  # app分页查询私信列表
        data = {
            "current": 0,
            "entity": {},
            "orders": [
                {
                    "asc": "true",
                    "column": ""
                }
            ],
            "size": 0
        }
        header = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.url3, json=data, headers=header)
        result = json.loads(r.text)
        print("headers信息...:", header)
        print("请求地址.......:", self.url3)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_remove(self):  # app删除私信
        data = {
            "id": [2769957469547724801]
            # "recUserId": [2762327263629356033]
        }
        header = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.url4, json=data, headers=header)
        result = json.loads(r.text)
        print("headers信息...:", header)
        print("请求地址.......:", self.url4)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_count(self):  # app查看未读消息数量

        header = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.url5,  headers=header)
        result = json.loads(r.text)
        print("headers信息...:", header)
        print("请求地址.......:", self.url5)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)


if __name__ == '__main__':
    unittest.main()

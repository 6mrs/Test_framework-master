import json
import unittest

import requests

from test.common.get_token import get_token
from utils.log import logger


class TestFans(unittest.TestCase):
    def setUp(self):
        self.url1 = 'http://test.dr.loc/api/app-user/app/userFans/add'
        self.url2 = 'http://test.dr.loc/api/app-user/app/userFans/byList'
        self.url3 = 'http://test.dr.loc/api/app-user/app/userFans/byPage'
        self.url4 = 'http://test.dr.loc/api/app-user/app/userFans/page'
        self.url5 = 'http://test.dr.loc/api/app-user/app/userFans/list'

    def test_addFans(self):  # app关注某人
        data = {
            "ids": [2768788935397508097]
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

    def test_byList(self):  # app非分页查询被关注列表
        header = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.url2, headers=header)
        result = json.loads(r.text)
        print("headers信息...:", header)
        print("请求地址.......:", self.url2)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_byPage(self):  # app分页查询被关注列表
        data = {
            "current": 0,
            "entity": {},
            "orders": [
                {
                    "asc": "true",
                    "column": "0"
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

    def test_Page(self):  # app分页查询关注列表
        data = {
            "current": 0,
            "entity": {},
            "orders": [
                {
                    "asc": 'true',
                    "column": ""
                }
            ],
            "size": 0
        }
        header = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.url4, json=data, headers=header)
        result = json.loads(r.text)
        print("headers信息...:", header)
        print("请求地址.......:", self.url4)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        logger.debug(r.text)

    def test_List(self):  # app非分页查询关注列表

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

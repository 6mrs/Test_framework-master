import unittest
import requests
import json

from test.common.get_admintoken import get_admintoken
from test.common.get_token import get_token
from utils.log import logger


class TestInterface(unittest.TestCase):
    def setUp(self):  # 初始化
        self.t = globals()
        self.base_url = 'http://dev.dr.loc/api/app-goods/goods/goodsInfo/adminVerifyPass'
        self.base2_url = 'http://dev.dr.loc/api/app-goods/goods/goodsInfo/adminGet'
        self.base3_url = 'http://dev.dr.loc/api/app-goods/goods/goodsInfo/adminPage'

    def test_admin(self):  # 同意商品，按照商品id进行审核
        data = {
            "feedback": "同意同意",
            "goodsIds": [2771441186970552321]
        }
        head = {"Content-Type": "application/Json", "app-token": get_admintoken()}
        r = requests.post(self.base_url, json=data, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_getmsg(self):  # 查询商品详细情况
        data = {
            "ids": [
                2771441186970552321
            ]
        }
        head = {"Content-Type": "application/Json", "app-token": get_admintoken()}
        r = requests.post(self.base2_url, json=data, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base2_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_getpage(self):  # 分页查询商品信息
        data = {
            "current": 0,
            "entity": {
                "categoryId": 0,
                "createTimeEnd": "2020-12-08T10:19:55.067Z",
                "createTimeStart": "2020-12-08T10:19:55.067Z",
                "goodsName": "string",
                "shopPhone": "string",
                "status": 0
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
        r = requests.post(self.base3_url, json=data, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base3_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)


if __name__ == '__main__':
    unittest.main()

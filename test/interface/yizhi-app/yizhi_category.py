import unittest
import requests
import json

from test.common.get_token import get_token
from utils.log import logger


class TestInterface(unittest.TestCase):
    def setUp(self):  # 初始化
        self.t = globals()
        self.base_url = 'http://dev.dr.loc/api/app-goods/goods/appGoodsCategory/add'
        self.base2_url = 'http://dev.dr.loc/api/app-goods/goods/appGoodsCategory/all'
        self.base3_url = 'http://dev.dr.loc/api/app-goods/goods/appGoodsCategory/get'
        self.base4_url = 'http://dev.dr.loc/api/app-goods/goods/appGoodsCategory/remove'

    def test_add(self):  # 新增分类信息
        data = {
            "name": "花棚",
            "parentId": 1334682399234039809,
            "status": 1
        }
        head = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.base_url, json=data, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_get(self):  # 获取所有分类信息
        head = {"Content-Type": "application/Json"}
        r = requests.post(self.base2_url, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base2_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_page(self):  # 查询商品分类信息详情
        data = {
            "ids": [
                1334440270087716866
            ]
        }
        head = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.base3_url, json=data, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base3_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_remove(self):  # admin删除分类
        data = {
            "ids": [
                1334669039927009281
            ]
        }
        head = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.base4_url, json=data, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base4_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)


if __name__ == '__main__':
    unittest.main()

import unittest
import requests
import json

from test.common.get_token import get_token
from utils.log import logger


class TestInterface(unittest.TestCase):
    def setUp(self):  # 初始化
        self.base3_url = 'http://test.dr.loc/api/app-user/app/userAddr/add'
        self.base6_url = 'http://test.dr.loc/api/app-user/app/userAddr/get'
        self.base7_url = 'http://test.dr.loc/api/app-user/app/userAddr/update'
        self.base8_url = 'http://test.dr.loc/api/app-user/app/userAddr/remove'
        self.base9_url = 'http://test.dr.loc/api/app-user/app/userAddr/page'
        self.t = globals()

    def test_1_pageAddress(self):  # 分页查询地址
        data = {
            "current": 0,
            "entity": {},
            "orders": [
                {
                    "asc": 'true',
                    "column": ""
                }
            ],
            "size": 10
        }

        head = {"Content-Type": "application/Json", 'app-token': get_token()}
        r = requests.post(self.base9_url, json=data, headers=head)
        result = json.loads(r.text)  # 使用json格式返回
        print("headers信息...:", head)
        print("请求地址.......:", self.base9_url)
        print("返回数据为......:", r.json()["data"]["records"])   # 列表多个数据，需加索引号方可取值
        self.t["idd"] = r.json()["data"]["records"][0]["id"]
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_addUserAddress(self):  # 添加收货地址
        data = {
            "areaAddr": "北京朝阳区",
            "areaVO": {
                "city": '',
                "county": '',
                "province": '',
                "town": ''
            },
            "detailAddr": "常营天街",
            "isDefault": 0,
            "remark": "",
            "signName": "秋分姐姐",
            "signPhone": "13140190582"
        }

        head = {"Content-Type": "application/Json", 'app-token': get_token()}
        r = requests.post(self.base3_url, json=data, headers=head)
        result = r.text  # 使用json格式返回

        print("请求地址：.......", self.base3_url)
        print("请求数据为：...", data)
        print("返回数据为：.....", result)
        self.assertIn('msg', r.text)  # 断言
        # self.assertEqual(result['code'], '0')
        # self.t['token'] = head['app-token']
        logger.debug(r.text)

    def test_3_getAddress(self):  # 查询收货地址详情
        data = {
            "ids": []
        }

        head = {"Content-Type": "application/Json", 'app-token': get_token()}
        r = requests.post(self.base6_url, headers=head)
        result = json.loads(r.text)  # 使用json格式返回
        print("headers信息：...", head)
        print("请求地址：.......", self.base6_url)
        print("返回数据为：.....", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], '0')
        logger.debug(r.text)

    def test_4_updateAddress(self):  # 修改收货地址
        data = {
            "areaAddr": "北京朝阳四环街道",
            "areaVO": {
                "city": 0,
                "county": 0,
                "province": 0,
                "town": 0
            },
            "detailAddr": "哇哈哈哈哈哈哈哈哈街区",
            "id": self.t['idd'],
            "isDefault": 0,
            "remark": "",
            "signName": "哇哈哈",
            "signPhone": "131243"
        }
        head = {"Content-Type": "application/Json", 'app-token': get_token()}
        r = requests.post(self.base7_url, json=data, headers=head)
        result = json.loads(r.text)  # 使用json格式返回
        print("headers信息：...", head)
        print("请求地址：.......", self.base7_url)
        print("返回数据为：.....", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_5_removeAddress(self):  # 删除收货地址
        data = {
            "ids": [self.t['idd']]
        }
        head = {"Content-Type": "application/Json"}
        r = requests.post(self.base8_url, json=data, headers=head)
        result = json.loads(r.text)  # 使用json格式返回
        print("headers信息：...", head)
        print("请求地址：.......", self.base8_url)
        print("返回数据为：.....", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)


if __name__ == '__main__':
    unittest.main()

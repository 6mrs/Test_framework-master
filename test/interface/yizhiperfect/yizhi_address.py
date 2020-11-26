import unittest
import requests
import json
from utils.log import logger


class TestInterface(unittest.TestCase):
    def setUp(self):  # 初始化
        self.base_url = 'http://192.168.11.102:8080/app/userInfo/login'
        self.base3_url = 'http://192.168.11.102:8080/app/userAddr/add'
        self.base6_url = 'http://192.168.11.102:8080/app/userAddr/get'
        self.base7_url = 'http://192.168.11.102:8080/app/userAddr/update'
        self.base8_url = 'http://192.168.11.102:8080/app/userAddr/remove'
        self.t = globals()

    def test_1_login(self):  # 登录获取token
        data = {"phone": "13140190582", "sms": "102938"}  # 定义传参数据
        head = {"Content-Type": "application/Json"}  # 定义头部
        r = requests.post(self.base_url, json=data, headers=head)  # 传入参数
        result = r.text
        self.assertIn('msg', r.text)  # 检验返回值
        logger.debug(r.text)
        print(r.json()['data'])
        self.t['token'] = r.json()['data']
        return r.json()['data']  # data为token

    def test_2_addUserAddress(self):  # 添加收货地址
        data = {
            "areaAddr": "北京朝阳区",
            "areaVO": {
                "city": 1,
                "county": 2,
                "province": 2,
                "town": 2
            },
            "detailAddr": "常营天街",
            "isDefault": 0,
            "remark": "",
            "signName": "秋分姐姐",
            "signPhone": "13140190582"
        }

        head = {"Content-Type": "application/Json", 'app-token': self.t['token']}
        r = requests.post(self.base3_url, json=data, headers=head)
        result = r.text  # 使用json格式返回
        print("headers信息：...", head)
        print("请求地址：.......", self.base3_url)
        print("返回数据为：.....", result)
        self.assertIn('msg', r.text)  # 断言
        # self.assertEqual(result['code'], '0')
        # self.t['token'] = head['app-token']
        logger.debug(r.text)

    def test_3_getAddress(self):  # 查询收货地址详情
        data = {
            "ids": [2766684318613377025]
        }

        head = {"Content-Type": "application/Json", 'app-token': self.t['token']}
        r = requests.post(self.base6_url, json=data, headers=head)
        result = r.text  # 使用json格式返回
        print("headers信息：...", head)
        print("请求地址：.......", self.base6_url)
        print("返回数据为：.....", result)
        self.t['idd'] = r.json()['data'][0]['id']
        self.assertIn('msg', r.text)  # 断言
        # self.assertEqual(result['code'], '0')
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
            "detailAddr": "哇哈哈街区",
            "id": self.t['idd'],
            "isDefault": 0,
            "remark": "",
            "signName": "哇哈哈",
            "signPhone": "131243"
        }
        head = {"Content-Type": "application/Json", 'app-token': self.t['token']}
        r = requests.post(self.base7_url, json=data, headers=head)
        result = r.text  # 使用json格式返回
        print("headers信息：...", head)
        print("请求地址：.......", self.base7_url)
        print("返回数据为：.....", result)
        self.assertIn('msg', r.text)  # 断言
        # self.assertEqual(result['code'], '0')
        logger.debug(r.text)

    def test_5_removeAddress(self):  # 删除收货地址
        data = {
            "ids": [self.t['idd']]
        }
        head = {"Content-Type": "application/Json"}
        r = requests.post(self.base8_url, json=data, headers=head)
        result = r.text  # 使用json格式返回
        print("headers信息：...", head)
        print("请求地址：.......", self.base8_url)
        print("返回数据为：.....", result)
        self.assertIn('msg', r.text)  # 断言
        # self.assertEqual(result['code'], '0')
        logger.debug(r.text)


if __name__ == '__main__':
    unittest.main()

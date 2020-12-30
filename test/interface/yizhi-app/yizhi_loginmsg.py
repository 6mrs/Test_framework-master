import unittest
import requests
import json

from test.common.get_token import get_token
from utils.log import logger


class TestInterface(unittest.TestCase):
    def setUp(self):  # 初始化
        self.t = globals()
        self.base_url = 'http://dev.dr.loc/api/app-user/app/userInfo/login'
        self.base2_url = 'http://dev.dr.loc/api/app-user/app/userInfo/get'
        self.base4_url = 'http://dev.dr.loc/api/app-user/app/userInfo/sms'
        self.base5_url = 'http://dev.dr.loc/api/app-user/app/userInfo/update'

    # def test_1_login(self):  # 登录获取token
    #     data = {"phone": "13140190582", "sms": "102938"}  # 定义传参数据
    #     head = {"Content-Type": "application/Json"}  # 定义头部
    #     r = requests.post(self.base_url, data=json.dumps(data), headers=head)  # 传入参数
    #     result = r.text
    #     print(result)
    #     jsr = json.loads(result)
    #     token = jsr['data']
    #     self.t['fx'] = token
    #     print(self.t['fx'])
    #     self.assertIn('msg', r.text)  # 检验返回值
    #     logger.debug(r.text)

    def test_2_getMsg(self):  # 查看用户信息
        head = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.base2_url, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base2_url)
        print("返回数据为......:", result)
        # jsr = json.loads(result)
        # userid = jsr['data']['id']
        # self.t['userid'] = userid
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    # def test_getSms(self):  # 获取验证码
    #     data = {
    #         "phone": ""
    #     }  # 定义传参数据
    #
    #     head = {"Content-Type": "application/Json"}
    #     r = requests.post(self.base4_url, json=data, headers=head)
    #     result = json.loads(r.text)  # 使用json格式返回
    #     print(result)
    #     self.assertIn('msg', r.text)  # 断言
    #     # self.assertEqual(result['code'], '0')
    #     logger.debug(r.text)

    def test_3_updateMsy(self):  # 修改用户信息
        data = {
            "avator": "",
            "deptId": "",
            "linkAddr": "",
            "name": "",
            "phone": "",
            "pwd": "123456",
            "sex": 1,
            "sign": "小魔仙"
        }  # 定义传参数据

        head = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.base5_url, json=data, headers=head)
        result = json.loads(r.text)  # 使用json格式返回
        print("headers信息...:", head)
        print("请求地址.......:", self.base5_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)


if __name__ == '__main__':
    unittest.main()

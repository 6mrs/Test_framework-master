import unittest
import requests
import json
from utils.log import logger


class TestInterface(unittest.TestCase):
    def setUp(self):  # 初始化
        self.t = globals()
        self.base_url = 'http://192.168.11.102:8080/app/userInfo/login'
        self.base2_url = 'http://192.168.11.102:8080/app/userInfo/get'
        self.base4_url = 'http://192.168.11.102:8080/app/userInfo/sms'
        self.base5_url = 'http://192.168.11.102:8080/app/userInfo/update'

    def test_login(self):  # 登录获取token
        data = {"phone": "13140190582", "sms": "102938"}  # 定义传参数据
        head = {"Content-Type": "application/Json"}  # 定义头部
        r = requests.post(self.base_url, data=json.dumps(data), headers=head)  # 传入参数
        result = r.text
        print(result)
        jsr = json.loads(result)
        token = jsr['data']
        self.t['fx'] = token
        print(self.t['fx'])
        self.assertIn('msg', r.text)  # 检验返回值
        logger.debug(r.text)

    def test_getMsg(self):  # 查看用户信息
        print(self.t)
        head = {"Content-Type": "application/Json", "app-token": self.t['fx']}
        r = requests.post(self.base2_url, headers=head)
        result = json.loads(r.text)
        print(result)
        # jsr = json.loads(result)
        # userid = jsr['data']['id']
        # self.t['userids'] = userid
        # self.assertIn('msg', r.text)  # 断言
        # # self.assertEqual(result['code'], '0')
        # logger.debug(r.text)

    def test_getSms(self):  # 获取验证码
        data = {
            "phone": ""
        }  # 定义传参数据

        head = {"Content-Type": "application/Json"}
        r = requests.post(self.base4_url, json=data, headers=head)
        result = json.loads(r.text)  # 使用json格式返回
        print(result)
        self.assertIn('msg', r.text)  # 断言
        # self.assertEqual(result['code'], '0')
        logger.debug(r.text)

    def test_updateMsy(self):  # 修改用户信息
        data = {
            "avator": "",
            "deptId": "",
            "linkAddr": "",
            "name": "",
            "phone": "",
            "pwd": "",
            "sex": 2,
            "sign": ""
        }  # 定义传参数据

        head = {"Content-Type": "application/Json", "app-token": self.test_login()}
        r = requests.post(self.base5_url, json=data, headers=head)
        result = json.loads(r.text)  # 使用json格式返回
        print(result)
        self.assertIn('msg', r.text)  # 断言
        # self.assertEqual(result['code'], '0')
        logger.debug(r.text)


if __name__ == '__main__':
    unittest.main()

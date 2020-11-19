import unittest
import requests
import json


class TestList(unittest.TestCase):
    def setUp(self):  # 初始化
        self.base_url = 'http://10.0.1.184/boot/app/address/findUserAddress'

    def test_le(self):
        head = {"Content-Type": "application/Json", 'appToken': self.test_user()}  # 定义头部

        r = requests.post(self.base_url, headers=head)  # 传入参数
        result = json.loads(r.text)  # 使用json格式返回

        self.assertIn('retmsg', r.text)  # 检验返回值
        print(result)


if __name__ == '__main__':
    unittest.main()

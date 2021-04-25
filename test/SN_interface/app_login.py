import json
import unittest

import requests


def test_loginToGetToken():
    url = "http://dev.sn.loc/api/app/userInfo/login"
    # 登录的参数数据
    data = {"code": "",
            "deviceId": "",
            "inviterId": 0,
            "name": "",
            "phone": "13140190582",
            "sms": "102938"}  # 定义传参数据18224560720
    head = {"Content-Type": "application/Json"}  # 定义头部im
    # 初始化url请求对象
    response = requests.post(url=url, json=data, headers=head)

    # result = json.loads(response.text)  # 使用json格式返回
    print(response)


if __name__ == "__main__":
    unittest.main()

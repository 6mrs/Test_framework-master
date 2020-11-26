#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

import json

from ruamel import yaml


def test_loginToGetToken():
    url = "http://10.0.1.184/boot/admin/login"
    # 登录的参数数据
    data = {"phone": "13140190582", "shortMsgCode": "102938", "type": "1"}  # 定义传参数据
    head = {"Content-Type": "application/Json"}  # 定义头部im
    # 初始化url请求对象
    response = requests.post(url=url, params=data, headers=head)
    result = json.loads(response.text)  # 使用json格式返回

    # print(response.text)
    print(response.status_code)
    print(response.json()["data"]["appToken"])
    # return response.json()["token"]

    # 把token值写入配置文件中
    yamlpath = r'/Users/youjia/Desktop/Test_framework-master/config/token.yaml'  # 保存文件路径
    # 提取token字段
    tokenValue = {
        'appToken': response.json()["data"]["appToken"]
    }
    with open(yamlpath, "w", encoding="utf-8") as f:  # w进行写入，截断文件
        yaml.dump(tokenValue, f, Dumper=yaml.RoundTripDumper)


if __name__ == "__main__":
    test_loginToGetToken()

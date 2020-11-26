import unittest

import fp as fp
import requests
import json
from utils.HTMLTestRunner import HTMLTestRunner
from utils.config import REPORT_PATH
from utils.log import logger


class TestInterface(unittest.TestCase):
    def setUp(self):  # 初始化
        self.base_url = 'http://10.0.1.184/boot/admin/login'
        self.base2_url = 'http://10.0.1.184/boot/app/address/findUserAddress'
        self.base3_url = 'http://10.0.1.184/boot/app/order/findOrderList'
        self.base4_url = 'http://10.0.1.184/boot/app/address/addUserAddress'
        self.base5_url = 'http://10.0.1.184/boot/app/address/updateUserAddress'
        self.base6_url = 'http://10.0.1.184/boot/app/address/removeUserAddress'

    def test_login(self):  # 登录获取token
        data = {"phone": "13140190582", "shortMsgCode": "102938", "type": "1"}  # 定义传参数据
        head = {"Content-Type": "application/Json"}  # 定义头部
        r = requests.post(self.base_url, params=data, headers=head)  # 传入参数
        result = json.loads(r.text)  # 使用json格式返回
        self.assertIn('retmsg', r.text)  # 检验返回值
        logger.debug(r.text)
        return r.json()['data']['appToken']

    def test_findUserAddress(self):  # 查看收货地址
        head = {"Content-Type": "application/Json", 'appToken': self.test_login()}
        r = requests.post(self.base2_url, headers=head)
        result = json.loads(r.text)  # 使用json格式返回
        print(result)
        self.assertIn('retmsg', r.text)  # 断言
        self.assertEqual(result['retcode'], '200')
        logger.debug(r.text)

    def test_findOrderList(self):  # 订单查询  订单状态 全部：100 1：待支付，2:待发货，3:待收货，4：待评价 5：已完成 0：已取消
        data = {'time': '1', 'type': '2', 'page': '0', 'size': '10'}  # 定义传参数据
        head = {"Content-Type": "application/Json", 'appToken': self.test_login()}
        r = requests.post(self.base3_url, params=data, headers=head)
        result = json.loads(r.text)  # 使用json格式返回
        print(result)
        self.assertIn('retmsg', r.text)  # 断言
        self.assertEqual(result['retcode'], '200')
        logger.debug(r.text)

    def test_addUserAddress(self):  # 添加收货地址
        data = {'userid': '6928', 'username': 'queens',
                'userphone': '13143980894',
                'areaidpath': '1_72_2799_0',
                'areapathname': '北京朝阳区三环以内',
                'useraddress': 'wwawa',
                'zipcode': '100000',
                'isdefault': '1'}  # 定义传参数据

        head = {"Content-Type": "application/Json", 'appToken': self.test_login()}
        r = requests.post(self.base4_url, params=data, headers=head)
        result = json.loads(r.text)  # 使用json格式返回
        print(result)
        self.assertIn('retmsg', r.text)  # 断言
        self.assertEqual(result['retcode'], '200')
        logger.debug(r.text)

    def test_updateUserAddress(self):  # 修改收货地址
        data = {'userid': '6928', 'username': '清清浅浅',
                'userphone': '13143980894',
                'areaidpath': '1_72_2799_0',
                'areapathname': '北京朝阳区三环以内',
                'useraddress': 'wwawa',
                'zipcode': '100000',
                'isdefault': '1'}  # 定义传参数据

        head = {"Content-Type": "application/Json", 'appToken': self.test_login()}
        r = requests.post(self.base5_url, params=data, headers=head)
        result = json.loads(r.text)  # 使用json格式返回
        print(result)
        self.assertIn('retmsg', r.text)  # 断言
        self.assertEqual(result['retcode'], '200')
        logger.debug(r.text)

    def test_removeUserAddress(self):  # 删除收货地址
        data = {'userAddressId': '24050'}

        head = {"Content-Type": "application/Json", 'appToken': self.test_login()}
        r = requests.post(self.base6_url, params=data, headers=head)
        result = json.loads(r.text)  # 使用json格式返回
        print(result)
        self.assertIn('retmsg', r.text)  # 断言
        self.assertEqual(result['retcode'], '200')
        logger.debug(r.text)


if __name__ == '__main__':
    unittest.main()

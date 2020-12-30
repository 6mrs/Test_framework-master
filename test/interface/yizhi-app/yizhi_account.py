import unittest
import requests
import json

from test.common.get_token import get_token
from utils.log import logger


class TestInterface(unittest.TestCase):
    def setUp(self):  # 初始化
        self.t = globals()
        self.base_url = 'http://dev.dr.loc/api/user-account/account/userAccount/updateUserMoneyAccount'
        self.base2_url = 'http://dev.dr.loc/api/user-account/account/userAccount/updateSystemAccount'
        self.base3_url = 'http://dev.dr.loc/api/user-account/earnest/userEarnest/update'
        self.base4_url = 'http://dev.dr.loc/api/user-account/account/userAccount/pageUserMoneyLog'

    def test_update(self):  # 更新用户资金信息
        data = {
            "ioAmt": 10000000,
            "ioType": 1,  # 记录类型: 1:充值, 2:消费,3:提取,4:退款,5:冲正,6:收入
            "orderId": 2772163323007071233,
            "remark": "",
            "status": 1,
            "userId": 2768483002515404801
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

    def test_get(self):  # 更新平台系统账户信息
        data = {
            "buyerId": 2768483002515404801,
            "ioAmt": 30,
            "ioType": 12,  # 资金进出类型 11:买家支付,12:付款给卖家,13:未支付给卖家前退款给买家
            "sellerId": 2762327263629356033,
            "shopOrderId": 2761976043156836353
        }
        head = {"Content-Type": "application/Json"}
        r = requests.post(self.base2_url, json=data, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base2_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_earnest_update(self):  # 充值，冲正和扣款更新用户保证金账户信息

        data = {
            "earnestType": "buy",  # 保证类型 sell卖家保证金/buy买家保证金
            "ioAmt": 50000,
            "ioType": 1,  # 记录类型: 1:充值, 2:扣款，5:冲正
            "userId": 2772540048977598465
        }
        head = {"Content-Type": "application/Json", "app-user": get_token()}
        r = requests.post(self.base3_url, json=data, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base3_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_moneylog(self):  # 分页查询用户资金明细

        data = {
            "current": 0,
            "entity": {},
            "orders": [
                {
                    "asc": "true",
                    "column": ""
                }
            ],
            "size": 0
        }
        head = {"Content-Type": "application/Json", "app-user": get_token()}
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

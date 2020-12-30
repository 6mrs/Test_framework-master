import unittest
import requests
import json

from test.common.get_token import get_token
from utils.log import logger


class TestInterface(unittest.TestCase):
    def setUp(self):  # 初始化
        self.t = globals()
        self.base_url = 'http://test.dr.loc/api/app-order/aftersales/orderAftersales/initRefundInfo'
        self.base2_url = 'http://dev.dr.loc/api/app-order/aftersales/orderAftersales/add'
        self.base3_url = 'http://dev.dr.loc/api/app-order/aftersales/orderAftersales/pageOrderAftersalesApp'
        self.base4_url = 'http://dev.dr.loc/api/app-order/aftersales/orderAftersales/remove'
        self.base5_url = 'http://dev.dr.loc/api/app-order/aftersales/orderAftersales/sellerAgreesReturnGoods'
        self.base6_url = 'http://dev.dr.loc/api/app-order/aftersales/orderAftersales/update'

    def test_init(self):  # APP端点击申请退款按钮，初始化退款信息
        data = {
            "orderId": 2773603817686199297
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

    def test_add(self):  # APP端创建退货申请单
        data = {
            "goodsOrderId": 0,
            "refundAmt": 0,
            "refundNum": 0,
            "remark": "string",
            "returnCategoryCode": "string",
            "returnReason": "string",
            "shopId": 0,
            "userPhone": "string"
        }
        head = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.base2_url, json=data, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base2_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_order(self):  # app前端分页查询用户退货申请单
        data = {
            "current": 0,
            "entity": {},
            "orders": [
                {
                    "asc": "true",
                    "column": "string"
                }
            ],
            "size": 0
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

    def test_page(self):  # 用户撤销退货申请单
        data = {
            "ids": [
                0
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

    def test_seller(self):  # 卖家同意退货
        data = {
            "orderAftersalesId": 0,
            "refundAmt": 0,
            "sendOutGoods": 0,
            "status": 0
        }

        head = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.base5_url, json=data, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base5_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_update(self):  # 买家修改退货申请单
        data = {
            "goodsOrderId": 0,
            "id": 0,
            "refundAmt": 0,
            "refundNum": 0,
            "remark": "string",
            "returnCategoryCode": "string",
            "returnReason": "string",
            "shopId": 0,
            "userPhone": "string"
        }
        head = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.base6_url, json=data, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base6_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

if __name__ == '__main__':
    unittest.main()

import unittest
import requests
import json

from test.common.get_token import get_token
from utils.log import logger


class TestInterface(unittest.TestCase):
    def setUp(self):  # 初始化
        self.t = globals()
        self.base_url = 'http://release.dr.loc/api/app-order/order/userOrder/addFromGoodDetail'
        self.base2_url = 'http://release.dr.loc/api/app-order/order/userOrder/page'
        self.base3_url = 'http://release.dr.loc/api/app-order/order/userOrder/addFromShoppingCart'
        self.base4_url = 'http://dev.dr.loc/api/app-order/order/userOrder/get'
        self.base5_url = 'http://dev.dr.loc/api/app-order/order/userOrder/pageShopOrder'
        self.base6_url = 'http://dev.dr.loc/api/app-order/order/userOrder/cancelOrder'
        self.base7_url = 'http://dev.dr.loc/api/app-order/order/userOrder/confirmReceipt'

    def test_add(self):  # 商品详情页提交订单，创建订单
        data = {
            "goodsId": "2785108415015829505",
            "goodsNum": 2,
            "specsId": "2785108424893416449",
            "userAddrId": 2781568947706145793,
            "userPhone": "13140190582"
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

    def test_get(self):  # APP端分页查询我的订单列表
        data = {
            "current": 0,
            "entity": {
                "status": 100
            },
            "orders": [
                {
                    "asc": "true",
                    "column": "string"
                }
            ],
            "size": 0
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

    def test_order(self):  # app购物车选择商品后，提交订单
        data = {
            "cartIds": [
                2784861228128357377
            ],
            "userAddrId": 2781568947706145793,
            "userPhone": "13140190582"
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

    def test_page(self):  # APP端用户查询我的订单详情
        data = {
            "shopOrderId": 2772163322080129025,
            "status": 0,  # 0:全部 1：待支付 2:待发货 3:待收货，4：待评价
            "userOrderId": 2772163323007071233
        }
        head = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.base4_url, json=data, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base4_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言 APP端分页查询商品订单列表
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)

    def test_orderpage(self):  # APP端分页查询商品订单列表
        data = {
            "entity": {
                "status": 100
            },
            "current": 1
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

    def test_cancelorder(self):  # APP端待支付页面用户取消订单
        data = {
            "orderId": 2768909019680299009
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

    def test_confirm(self):  # APP端用户确认收货
        data = {
            "shopOrderId": 0
        }
        head = {"Content-Type": "application/Json", "app-token": get_token()}
        r = requests.post(self.base7_url, json=data, headers=head)
        result = json.loads(r.text)
        print("headers信息...:", head)
        print("请求地址.......:", self.base7_url)
        print("返回数据为......:", result)
        self.assertIn('msg', r.text)  # 断言
        self.assertEqual(result['code'], 0)
        logger.debug(r.text)


if __name__ == '__main__':
    unittest.main()

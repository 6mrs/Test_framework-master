import unittest
import requests
import json

from test.common.get_token import get_token
from utils.log import logger


class TestInterface(unittest.TestCase):
    def setUp(self):  # 初始化
        self.t = globals()
        self.base_url = 'http://test.dr.loc/api/app-order/order/userOrder/sendOutGoods'
        self.base2_url = 'http://dev.dr.loc/api/app-goods/goods/auction/pageAuction'
        self.base3_url = 'http://dev.dr.loc/api/app-goods/goods/auction/price'

    def test_add(self):  # APP商家去发货
        data = {
            "comCode": 11111,
            "expressNum": "12321312321",
            "orderId": 2779001780188436481
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

    def test_page(self):  # app拍卖商品列表
        data = {
            "current": 1,
            "entity": {
                "categoryIds": [
                    1338331876033527810
                ],
                "sort": 1,
                "status": 12  # 12：正在拍卖
            },
            "size": 30
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

    def test_price(self):  # app拍品出价·
        data = {
            "id": 2774300638384865281,
            "price": 2200,
            "priceType": 1,
            "specsId": 2774300639118869505
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


if __name__ == '__main__':
    unittest.main()

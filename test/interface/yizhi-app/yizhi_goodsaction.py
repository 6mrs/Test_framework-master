import unittest
import requests
import json

from test.common.get_token import get_token
from utils.log import logger


class TestInterface(unittest.TestCase):
    def setUp(self):  # 初始化
        self.t = globals()
        self.base_url = 'http://dev.dr.loc/api/app-goods/goods/auction/add'
        self.base2_url = 'http://dev.dr.loc/api/app-goods/goods/auction/pageAuction'
        self.base3_url = 'http://dev.dr.loc/api/app-goods/goods/auction/price'
        # self.base4_url = 'http://test.dr.loc/api/app-goods/goods/goodsInfo/updateVerify'
        # self.base5_url = 'http://dev.dr.loc/api/app-goods/goods/appGoodsCategory/page'

    def test_add(self):  # 新增拍品信息  状态 1:上架 0:下架 2:删除 3:系统下架 4:售罄
        data = {
            "ableAftersale": 0,
            "categoryId": 1338331876033527810,
            "deliveryType": 0,
            "details": "string",
            "endDate": "2020-12-18T18:46:01.452Z",
            "freight": 0,
            "goodsName": "拍品5",
            "imgs": "https://youjiayuexiang-test.oss-cn-beijing.aliyuncs.com/ossclient/upload/2020/07/4cc7ea98d218c16530a1159509f4fa9a.jpg",
            "increasePrice": 20,
            "sort": 0,
            "startDate": "2020-12-17T15:13:01.000Z",
            "startPrice": 100
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

    # def test_update(self):  # 修改商品信息-修改商品状态为待审核
    #     data = {
    #         "categoryId": 0,
    #         "deliveryType": 1,
    #         "details": "哈哈哈哈哈哈",
    #         "freight": 0,
    #         "goodsName": "超级牛肉",
    #         "goodsSpecsAdminUpdateVOList": [
    #             {
    #                 "excPoints": 0,
    #                 "goodsId": 0,
    #                 "goodsStock": 0,
    #                 "goodsWeight": 0,
    #                 "icon": "string",
    #                 "id": 2771088853707041793,
    #                 "marketPrice": 0,
    #                 "sellingPrice": 0,
    #                 "specsName": ""
    #             }
    #         ],
    #         "goodsType": "FIX",
    #         "id": 2771088853572822017,
    #         "imgs": "",
    #         "sort": 0
    #     }
    #     head = {"Content-Type": "application/Json"}
    #     r = requests.post(self.base4_url, json=data, headers=head)
    #     result = json.loads(r.text)
    #     print("headers信息...:", head)
    #     print("请求地址.......:", self.base4_url)
    #     print("返回数据为......:", result)
    #     self.assertIn('msg', r.text)  # 断言
    #     self.assertEqual(result['code'], 0)
    #     logger.debug(r.text)
    #
    # def test_page(self):  # 修改商品信息-修改商品状态为待审核
    #     data = {
    #         "categoryId": 0,
    #         "deliveryType": 1,
    #         "details": "哈哈哈哈哈哈",
    #         "freight": 0,
    #         "goodsName": "超级牛肉",
    #         "goodsSpecsAdminUpdateVOList": [
    #             {
    #                 "excPoints": 0,
    #                 "goodsId": 0,
    #                 "goodsStock": 0,
    #                 "goodsWeight": 0,
    #                 "icon": "string",
    #                 "id": 2771088853707041793,
    #                 "marketPrice": 0,
    #                 "sellingPrice": 0,
    #                 "specsName": ""
    #             }
    #         ],
    #         "goodsType": "FIX",
    #         "id": 2771088853572822017,
    #         "imgs": "",
    #         "sort": 0
    #     }
    #     head = {"Content-Type": "application/Json"}
    #     r = requests.post(self.base4_url, json=data, headers=head)
    #     result = json.loads(r.text)
    #     print("headers信息...:", head)
    #     print("请求地址.......:", self.base4_url)
    #     print("返回数据为......:", result)
    #     self.assertIn('msg', r.text)  # 断言
    #     self.assertEqual(result['code'], 0)
    #     logger.debug(r.text)
    #


if __name__ == '__main__':
    unittest.main()

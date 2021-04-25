import unittest
import requests
import json

from test.common.get_token import get_token
from utils.log import logger


class TestInterface(unittest.TestCase):
    def setUp(self):  # 初始化
        self.t = globals()
        self.base_url = 'http://release.dr.loc/api/app-goods/goods/auction/add'
        self.base2_url = 'http://dev.dr.loc/api/app-goods/goods/auction/pageAuction'
        self.base3_url = 'http://dev.dr.loc/api/app-goods/goods/auction/price'
        # self.base4_url = 'http://test.dr.loc/api/app-goods/goods/goodsInfo/updateVerify'
        # self.base5_url = 'http://dev.dr.loc/api/app-goods/goods/appGoodsCategory/page'

    def test_add(self):  # 新增拍品信息  状态 1:上架 0:下架 2:删除 3:系统下架 4:售罄
        data = {
            "categoryId": "1346325648180768770",
            "categoryName": " 植物分类(番杏)",
            "deliveryType": 2,
            "details": "哈哈哈就开始哭就说你是那你上哪嘴巴在哪芭娜娜那那那那那那那那那那那那扭扭捏捏那你呢那你呢你那那你呢\n\n\n\n经久不衰并不代表睡觉觉手机手机手机\n\n嫁鸡随鸡思考思考",
            "freight": 0,
            "goodsName": "我发布的测试拍品，就是我自己赢得拍品。DoYouKnow，测试暗价比较，名家比较爱哦的",
            "goodsSpecsAdminAddVOList": [],
            "goodsType": "FIX",
            "imgs": "https://test-dr.oss-cn-shanghai.aliyuncs.com/goods/2781482836501241857/16112830210110.png",
            "sort": 0,
            "increasePrice": 1000,
            "startDate": "2021-01-22 10:58:00",
            "endDate": "2021-01-22 12:36:00",
            "startPrice": 100,
            "linePrice": 0,
            "uuid": "adajdksjfk"
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

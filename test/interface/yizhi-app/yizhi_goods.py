import unittest
import requests
import json

from test.common.get_token import get_token
from utils.log import logger


class TestInterface(unittest.TestCase):
    def setUp(self):  # 初始化
        self.t = globals()
        self.base_url = 'http://release.dr.loc/api/app-goods/goods/goodsInfo/add'
        self.base2_url = 'http://release.dr.loc/api/app-goods/goods/goodsInfo/get'
        self.base3_url = 'http://release.dr.loc/api/app-goods/goods/goodsInfo/page'
        # self.base4_url = 'http://test.dr.loc/api/app-goods/goods/goodsInfo/updateVerify'
        # self.base5_url = 'http://release.dr.loc/api/app-goods/goods/appGoodsCategory/page'

    def test_add(self):  # 新增商品信息
        data = {
            "categoryId": "1346325552638717953",
            "categoryName": "潮流花盆(花盆02)",
            "deliveryType": 1,
            "details": "哈哈",
            "freight": 0,
            "goodsName": "商品烧烤",
            "goodsSpecsAdminAddVOList": [{
                "excPoints": 0,
                "goodsStock": 99,
                "goodsWeight": 0,
                "icon": "https://youjiayuexiang-test.oss-cn-beijing.aliyuncs.com/ossclient/upload/2020/12/10a2c59d94e9f2e5589b65d7c1219100.png",
                "marketPrice": 12,
                "sellingPrice": 10,
                "specsName": "原味"
            },
                {
                    "excPoints": 0,
                    "goodsStock": 99,
                    "goodsWeight": 0,
                    "icon": "https://youjiayuexiang-test.oss-cn-beijing.aliyuncs.com/ossclient/upload/2020/12/10a2c59d94e9f2e5589b65d7c1219100.png",
                    "marketPrice": 12,
                    "sellingPrice": 11,
                    "specsName": "测试味"
                },
                {
                    "excPoints": 0,
                    "goodsStock": 99,
                    "goodsWeight": 0,
                    "icon": "https://youjiayuexiang-test.oss-cn-beijing.aliyuncs.com/ossclient/upload/2020/12/10a2c59d94e9f2e5589b65d7c1219100.png",
                    "marketPrice": 12,
                    "sellingPrice": 10,
                    "specsName": "开发味"
                }],
            "goodsType": "FIX",
            "imgs": "https://youjiayuexiang-test.oss-cn-beijing.aliyuncs.com/ossclient/upload/2020/12/10a2c59d94e9f2e5589b65d7c1219100.png",
            "sort": 0,
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

    def test_get(self):  # 查询商品信息
        data = {
            "ids": [
                2771778208608770049
            ]
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

    def test_page(self):  # app分页查询所有在售商品信息
        data = {
            "current": 1,
            "entity": {
                "categoryId": 1336869398598602754,
                "goodsType": "FIX",
                "sortType": 1,
            }
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

import unittest

import requests

from utils.log import logger


class TestFans(unittest.TestCase):
    def setUp(self):
        self.url1 = 'http://192.168.11.102:8080/app/userFans/add'
        self.url2 = 'http://192.168.11.102:8080/app/userFans/byList'
        self.url3 = 'http://192.168.11.102:8080/app/userFans/byPage'

    def test_addFans(self):  # app关注某人
        data = {
            "ids": 2764905559492803585
        }
        header = {"Content-Type": "application/Json", "app-token": "2762335240897771521"}
        r = requests.post(self.url1, json=data, headers=header)
        result = r.text
        print(result)
        self.assertIn('msg', r.text)  # 断言
        logger.debug(r.text)

    def test_byList(self):  # app非分页查询列表
        header = {"Content-Type": "application/Json", "app-token": "2762335240897771521"}
        r = requests.post(self.url2, headers=header)
        result = r.text
        print(result)
        self.assertIn('msg', r.text)  # 断言
        logger.debug(r.text)

    def test_byPage(self):  # app分页查询列表
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
        header = {"Content-Type": "application/Json", "app-token": "2762335240897771521"}
        r = requests.post(self.url3, json=data, headers=header)
        result = r.text
        print(result)
        self.assertIn('msg', r.text)  # 断言
        logger.debug(r.text)


if __name__ == '__main__':
    unittest.main()

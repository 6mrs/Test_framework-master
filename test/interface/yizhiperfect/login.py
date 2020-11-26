import unittest
import requests
import json


class CreateActivity(unittest.TestCase):
    """创建活动-测试用例"""

    def setUp(self):
        self.base6_url = 'http://192.168.11.102:8080/app/userAddr/get'

    def push_file_download(self, xxx):
        """生成一条活动数据"""

        payload = {
            "ids": [2766684318613377025]
        }

        head = {"Content-Type": "application/Json", 'app-token': ''}

        response = requests.post(self.base6_url, data=json.dumps(payload), headers=head)

        data = json.loads(response.content)

        try:

            if data["data"] != {}:
                r_data = {
                    "id": data["data"]["id"]
                }
                return r_data
            else:
                print("返回结果为空或返回数据异常，请检查接口")
            return None

        except Exception as e:
            print("headers信息：", head)
            print("请求地址：", response.url)
            print("参数信息：", payload)
            raise e

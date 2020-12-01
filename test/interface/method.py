import requests
import json


class ApiRequest(object):
    """
    请求方法
    """

    # 请求方法get
    def get_method(self, url, data=None, header=None):

        if header is not None:
            res = requests.get(url, params=data, headers=header)
        else:
            res = requests.get(url, params=data)
        return res.json()

    # 请求方法post
    def post_method(self, url, data=None, header=None):
        global res
        if header is not None:
            res = requests.post(url, data=data, json=data, headers=header)
        else:
            res = requests.post(url, data=data, json=data,)
        if str(res) == "<Response [200]>":
            return res.json()
        else:
            return res.text

    # 请求方法put
    def put_method(self, url, data=None, header=None):
        if header is not None:
            res = requests.put(url, json=data, headers=header)
        else:
            res = requests.delete(url, json=data)
        return res.json()

    # 请求方法delete
    def delete_method(self, url, data=None, header=None):
        if header is not None:
            res = requests.delete(url, json=data, headers=header)
        else:
            res = requests.delete(url, json=data)
        return res.json()

    # 主方法
    def run_method(self, method, url, data=None, header=None):
        if method == 'get' or method == 'GET':
            res = self.get_method(url, data, header)
        elif method == 'post' or method == 'POST':
            res = self.post_method(url, data, header)
        elif method == 'put' or method == 'PUT':
            res = self.post_method(url, data, header)
        elif method == 'delete' or method == 'DELETE':
            res = self.post_method(url, data, header)
        else:
            res = "你的请求方式不正确！"
        # return res
        return json.dumps(res, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ':'))

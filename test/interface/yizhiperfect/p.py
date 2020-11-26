import json

import requests


class TestWework:
    def setup_class(self):
        r = requests.post(
            'http://192.168.11.102:8080/app/userInfo/login',
            params={"phone": "13140190582", "sms": "102938"}
        )
        self.token = r.json()['data']

    def test_tags_list(self):
        r = requests.post(
            'http://192.168.11.102:8080/app/userInfo/get',
            headers={'app-token': self.token}
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.status_code == 0
        assert r.json()['errcode'] == 0

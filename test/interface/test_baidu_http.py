import unittest
import warnings

from utils.config import Config, REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.assertion import assertHTTPCode


class TestBaiDuHTTP(unittest.TestCase):
    URL = 'https://www.baidu.com'

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='GET')

    def test_baidu_http(self):
        res = self.client.send()
        logger.debug(res.text)
        self.assertIn('百度一下，你就知道', res.text)


if __name__ == '__main__':
    report = REPORT_PATH + '/report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架', description='接口html报告')
        runner.run(TestBaiDuHTTP('test_baidu_http'))

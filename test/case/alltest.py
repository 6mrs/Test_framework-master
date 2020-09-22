import unittest
import os

from utils import HTMLTestRunner
from utils.config import REPORT_PATH


def allTest():
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),  # 文件地址
        pattern="dev_*.py",  # 文件类型
        top_level_dir=None)
    return suite


def run():
    unittest.TextTestRunner(verbosity=2).run(allTest())


def get_nowtime(): '''时间'''


pass

if __name__ == "__main__":
    report = REPORT_PATH + '/testReport.html'
    HTMLTestRunner.HTMLTestRunner(
        stream=open(report, 'wb'),
        title="自动化测试报告",
        description="自动化测试执行的详细信息"
    ).run(allTest())

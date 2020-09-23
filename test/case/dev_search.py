import os

from selenium import webdriver
import unittest
import time

from utils import HTMLTestRunner
from utils.config import DATA_PATH
from utils.file_reader import ExcelReader
from utils.log import logger


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 打开url
        self.driver.get("http://www.ibdata.cn/#/login")

    excel = DATA_PATH + '/baidu.xlsx'

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
        self.driver.find_element_by_name("handle").clear()  # clear方法清空列表
        self.driver.find_element_by_name("handle").send_keys(d['username'])
        time.sleep(2)
        # 密码的定位
        # 因为所有元素的条件相同所以我在此选择xpath进行定位
        self.driver.find_elements_by_xpath("//input[@name='handle']")[-1].send_keys(d['password'])
        self.driver.find_element_by_class_name("sign-button").click()

        time.sleep(5)
        links = self.driver.find_elements_by_xpath(
            '/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/button')
        for link in links:
            logger.info(link.text)


def tearDown(self):
    self.driver.quit()


if __name__ == "__main__":
    unittest.main()

import time
import unittest

import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH
from utils.log import logger


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '/chromedriver')
        self.driver.get(self.URL)

    def test_search_0(self):
        self.driver.find_element_by_css_selector('#signupForm > input.form-control.uname').send_keys('admin')  # 用户名正确
        self.driver.find_element_by_css_selector('#signupForm > input.form-control.pword').send_keys('123')  # 密码正确
        self.driver.find_element_by_css_selector('#signupForm > div.row.m-t > div:nth-child(1) > input').send_keys(
            '1234')  # 验证码错误
        self.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

        links = self.driver.find_elements_by_xpath('//*[@id="btnSubmit"]"]')
        for link in links:
            logger.info(link.text)
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

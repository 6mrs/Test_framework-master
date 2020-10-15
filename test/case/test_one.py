# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from utils.config import REPORT_PATH
from utils.HTMLTestRunner import HTMLTestRunner

class UntitledTestCase1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case1(self):
        driver = self.driver
        driver.get("http://10.0.1.184/youjia-admin/login")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123")
        driver.find_element_by_name("validateCode").clear()
        driver.find_element_by_name("validateCode").send_keys("0")
        driver.find_element_by_id("btnSubmit").click()
        time.sleep(5)

        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("18675425672766555677")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123")
        driver.find_element_by_name("validateCode").clear()
        driver.find_element_by_name("validateCode").send_keys("16")
        driver.find_element_by_id("btnSubmit").click()
        time.sleep(5)


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == '__main__':
    report = REPORT_PATH + '/test.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='测试框架', description='修改html报告')
        runner.run(UntitledTestCase1('test_untitled_test_case1'))

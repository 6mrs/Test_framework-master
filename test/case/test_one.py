# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from test.case.alltest import allTest
from utils import HTMLTestRunner
from utils.config import REPORT_PATH


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
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("")
        driver.find_element_by_id("btnSubmit").click()
        driver.find_element_by_name("username").click()
        time.sleep(5)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("youjia")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123")
        driver.find_element_by_name("validateCode").clear()
        driver.find_element_by_name("validateCode").send_keys("16")
        driver.find_element_by_id("signupForm").submit()
        driver.find_element_by_name("username").click()
        time.sleep(5)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("youjia")
        driver.find_element_by_name("validateCode").clear()
        driver.find_element_by_name("validateCode").send_keys("1")
        driver.find_element_by_id("btnSubmit").click()

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


if __name__ == "__main__":
    report = REPORT_PATH + '/test.html'
    HTMLTestRunner.HTMLTestRunner(
        stream=open(report, 'wb'),
        title="自动化测试报告",
        description="自动化测试执行的详细信息"
    ).run(webdriver())

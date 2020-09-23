# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from utils.log import logger


class UntitledTestCase2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case2(self):
        driver = self.driver
        driver.get("http://10.0.1.184/youjia-admin/index")
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_name("goodsName").click()
        driver.find_element_by_name("goodsName").clear()
        driver.find_element_by_name("goodsName").send_keys(u"苹果")
        driver.find_element_by_link_text(u"搜索").click()
        driver.find_element_by_name("goodsName").click()
        driver.find_element_by_name("goodsName").clear()
        driver.find_element_by_name("goodsName").send_keys("123")
        driver.find_element_by_link_text(u"搜索").click()
        driver.find_element_by_name("goodsName").click()
        driver.find_element_by_name("goodsName").clear()
        driver.find_element_by_name("goodsName").send_keys(u"苹  果")
        driver.find_element_by_link_text(u"搜索").click()
        links = self.driver.find_elements_by_xpath(
            '/html/body/div/div/div[1]/form/div/ul/li[10]/a[1]')
        for link in links:
            logger.info(link.text)

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
    unittest.main()

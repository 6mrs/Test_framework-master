# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase4(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case4(self):
        driver = self.driver
        driver.get("http://10.0.1.183/youjia-admin/index")
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=3 | ]]
        driver.find_element_by_link_text(u"添加").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_name("cardName").click()
        driver.find_element_by_name("cardName").clear()
        driver.find_element_by_name("cardName").send_keys("youjia")
        driver.find_element_by_name("cardSign").click()
        driver.find_element_by_name("cardSign").clear()
        driver.find_element_by_name("cardSign").send_keys("1234")
        driver.find_element_by_id("expiryDate").click()
        driver.find_element_by_xpath("//tr[5]/td[4]").click()
        driver.find_element_by_id("parValue").click()
        driver.find_element_by_id("parValue").clear()
        driver.find_element_by_id("parValue").send_keys("100")
        driver.find_element_by_id("quantity").click()
        driver.find_element_by_id("quantity").clear()
        driver.find_element_by_id("quantity").send_keys("6")
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_link_text(u"关闭").click()

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

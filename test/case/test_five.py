# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_untitled_test_case1(self):
        driver = self.driver
        driver.get("http://10.0.1.183/youjia-admin/login")
        # 将用户名密码写入浏览器cookie中
        driver.add_cookie({'name': 'JSESSIONID', 'value': 'b3813600-d685-4fc9-8279-a488507ebc4d'})
        driver.add_cookie({'name': 'Hm_lvt_9bd56a6d0766b887592ee921aa94763f',
                           'value': '1600653214,1600916935,1602579523'})
        driver.add_cookie({'name': 'Hm_lpvt_9bd56a6d0766b887592ee921aa94763f', 'value': '1603069273'})
        # 再次访问网站，将会自动登录
        driver.get("http://10.0.1.183/youjia-admin/login")
        driver.refresh()  # 刷新下我们直接就登录进去了
        # time.sleep(3)
        # self.driver.implicitly_wait(10)
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        # self.driver.find_element_by_xpath('//*[@id="side-menu"]/li[5]/a/span[1]').click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="side-menu"]/li[5]/ul/li[3]/a').click()
        # time.sleep(5)
        # self.driver.get('http://10.0.1.183/youjia-admin/app/goods')
        # # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        self.driver.find_element_by_name('goodsName').send_keys('京东')
        self.driver.find_element_by_xpath('//*[@id="formId"]/div/ul/li[10]/a[1]').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

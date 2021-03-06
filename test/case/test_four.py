# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.driver.get('http://10.0.1.183/youjia-admin/login')
        driver = self.driver



    def test_untitled_test_case(self):
        self.driver.find_element_by_name("username").clear()  # 用户名正确，密码正确
        self.driver.find_element_by_name("username").send_keys("admin")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("youjia")
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(3)
        a = self.driver.current_url  # current_url 方法可以得到当前页面的URL
        b = "http://10.0.1.183/youjia-admin/index"
        self.assertEqual(a, b, '登录失败')
        cookie = self.driver.get_cookies()
        print(cookie)
        driver = self.driver
        # driver.add_cookie({'name': 'JSESSIONID', 'value': '087556d1-10a0-47bf-9711-0348d1028b62'})
        # driver.add_cookie({'name': 'Hm_lvt_9bd56a6d0766b887592ee921aa94763f',
        #                    'value': '1600653214,1600916935,1602579523'})
        # driver.add_cookie({'name': 'Hm_lpvt_9bd56a6d0766b887592ee921aa94763f', 'value': '1602809960'})
        time.sleep(3)
        driver.implicitly_wait(10)  # 隐式等待时间
        driver.switch_to.window(self.driver.window_handles[-1])  # 切换到该窗口
        driver.find_element_by_xpath('//*[@id="side-menu"]/li[5]/a/span[1]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="side-menu"]/li[5]/ul/li[3]/a').click()
        # driver.forward()
        # driver.find_element_by_xpath('//*[@id="toolbar"]/a[1]').click()
        # time.sleep(3)
        #
        # driver.switch_to.window(self.driver.window_handles[-1])
        driver.implicitly_wait(10)
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="content-main"]/iframe[2]'))  # 定位商品管理框架
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="formId"]/div/ul/li[1]/input').send_keys('100010851550')
        driver.find_element_by_xpath('//*[@id="formId"]/div/ul/li[10]/a[1]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="toolbar"]/a[1]').click()
        driver.switch_to_default_content()  # 释放iframe
        driver.implicitly_wait(10)
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="content-main"]/iframe[3]'))  #定位到添加商品框架
        time.sleep(3)
        driver.find_element_by_name('goodsName').send_keys('苹果')
        
        time.sleep(3)




    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

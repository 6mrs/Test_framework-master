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
        self.verificationErrors = []
        self.accept_next_alert = True
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
        time.sleep(3)
        driver.implicitly_wait(10)  # 隐式等待时间
        driver.switch_to.window(self.driver.window_handles[-1])  # 切换到该窗口
        driver.find_element_by_xpath('//*[@id="side-menu"]/li[5]/a/span[1]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="side-menu"]/li[5]/ul/li[3]/a').click()
        driver.implicitly_wait(10)
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="content-main"]/iframe[2]'))  # 定位商品管理框架
        time.sleep(3)
        driver.find_element_by_name("goodsName").send_keys("苹果")
        driver.find_element_by_link_text(u"搜索").click()
        time.sleep(3)
        q = driver.find_element_by_xpath('//*[@id="bootstrap-table"]/tbody/tr/td').text
        w = '没有找到匹配的记录'
        self.assertNotEqual(q, w, '查询失败')
        self.driver.get_screenshot_as_file("/Users/youjia/Desktop/测试图/shangpin1.jpg")

        driver.find_element_by_xpath("//form[@id='formId']/div/ul/li[10]/a[2]/i").click()
        driver.find_element_by_name("goodsName").send_keys("null")
        driver.find_element_by_xpath("//form[@id='formId']/div/ul/li[10]/a/i").click()
        q = driver.find_element_by_xpath('//*[@id="bootstrap-table"]/tbody/tr/td').text
        w = '没有找到匹配的记录'
        self.assertNotEqual(q, w, '查询失败')
        print('查询')
        time.sleep(3)
        driver.find_element_by_name("goodsName").clear()
        driver.find_element_by_name("goodsName").send_keys(u"苹 果")
        driver.find_element_by_link_text(u"搜索").click()
        time.sleep(3)
        driver.find_element_by_name("goodsName").clear()
        driver.find_element_by_name("goodsName").send_keys("asjhdbsjhcbhgvdcghfsdhgcjhbdschjvhgsvcfhgdcjbjshvchsd")
        driver.find_element_by_link_text(u"搜索").click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

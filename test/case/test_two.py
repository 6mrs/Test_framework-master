# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest



class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.driver.get('http://10.0.1.183/youjia-admin/login/')
        driver = self.driver

    # 定义方法
    def login(self, username, password):
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_id('btnSubmit').click()

    def test_untitled_test_case1(self):
        self.driver.find_element_by_name("username").send_keys("admin")  # 用户名正确，密码错误
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("123")
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(3)
        error_message = self.driver.find_element_by_xpath('/html/body/div[2]').text
        self.assertIn('用户不存在/密码错误', error_message)  # 用assertIn(a,b)方法来断言 a in b
        self.driver.get_screenshot_as_file("/Users/youjia/Desktop/测试图/login1.jpg")
        # a = self.driver.current_url  # current_url 方法可以得到当前页面的URL
        # b = "http://10.0.1.183/youjia-admin/index"
        # self.assertEqual(a, b, '登录失败')

    def test_untitled_test_case2(self):
        self.driver.find_element_by_name("username").clear()  # 用户名正确，密码正确
        self.driver.find_element_by_name("username").send_keys("admin")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("youjia")
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(3)
        a = self.driver.current_url  # current_url 方法可以得到当前页面的URL
        b = "http://10.0.1.183/youjia-admin/index"
        self.assertEqual(a, b, '登录失败')

    def test_untitled_test_case3(self):
        self.driver.find_element_by_name("username").clear()  # 用户名错误，密码正确
        self.driver.find_element_by_name("username").send_keys("one")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("youjia")
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(3)
        error_message = self.driver.find_element_by_xpath('/html/body/div[2]').text
        self.assertIn('用户不存在/密码错误', error_message)
        self.driver.get_screenshot_as_file("/Users/youjia/Desktop/测试图/login2.jpg")
        # a = self.driver.current_url  # current_url 方法可以得到当前页面的URL
        # b = "http://10.0.1.183/youjia-admin/index"
        # self.assertEqual(a, b, '登录失败')


    def tearDown(self):
        time.sleep(2)
        print('自动测试完毕！')
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

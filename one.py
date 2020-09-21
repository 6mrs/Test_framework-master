import unittest
from datetime import time

import self as self
from selenium.webdriver.chrome import webdriver

from utils.config import DRIVER_PATH


class testpro(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '/chromedriver')
        self.driver.implicitly_wait(8)
        self.driver.get('https://www.baidu.com')

    def tearDown(self):
        self.driver.quit()

    def test_baidu_search(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(2)


try:
    assert 'selenium' in self.driver.title
    print('Test Pass.')
except Exception as e:
    print('Test Fail.', format(e))

if __name__ == '__main__':
    unittest.main()

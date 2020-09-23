# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from utils import HTMLTestRunner
from utils.config import REPORT_PATH
from utils.log import logger


class UntitledTestCase3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case3(self):
        driver = self.driver
        driver.get("https://new.yjmsy.com/h5/")
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='search']").click()
        driver.find_element_by_xpath("//input[@type='search']").clear()
        driver.find_element_by_xpath("//input[@type='search']").send_keys(u"苹果")
        driver.find_element_by_xpath(
            "//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADsElEQVRYR+1XS2icVRg9Z17WKNYRg60P3LnUhaIgbiJaranWmv9eJ1FrsopRFKlILSpEW6iV6kJBjAjRaNLk/jOJ2hottAYRVwURIbXV+gARBdNgwhAd5nHkhomkbWby5wHd5K4G5nuc731+4jw/nmf/WANQNwN9fX0XNTQ0NEvaBuBGAFcDWAdgAsBJkl+USqXBTCbz/XJLuSCA0dHRC2ZmZh6StAfAxsWMS/qoUqnszGQyPywme/b/5wAYGBi4IplMvgPgPgCSNE7yfZJHC4XCr8lkcrpUKl2eSCRuIZkB0AzgEgDTJJ8IguDDpYA4A4BzbgPJQ9V0/07y2SAIDtQzmMvlrpW0T9KDXo5kVxAEb0cF8T8A59zFJAd9RJK+icViJgiCn6MaCsNwF4CXASQA3G+M+TiK7iyAsbGxxMTERBeAN0j+VCwWm1pbW3+LYmC+TBiGuwG8AOB4uVwOojTnLADnXCPJU/63pDZr7adLdT4nH4bhMIBtknY1Njbub2pqKtWzRedcHEAXyTcBHDLG3Ltc514vDMPNAHzTTlcqlWZr7cm6AHp6epLpdHqU5K2S7Eqin5eFwwA2AbjDGHN0sQysJ3kawOnx8fGN3d3dlZVkwOtms9k9kp4H8FI+n3+lo6Pj31o2mc1mb5J0TNLX1trbVuq8CsBKes+XtFgsPt7W1uY354LPA7hL0ucAho0xLasBwDl3O8khSd/G4/HtLS0tf0QBsOIGnHNSDWrA75MoAOZKcMxae/NqZCAMQ7+iewEcXLQEIyMjl5ZKJd+EE6vVhPMW0m5Je621/9QsgXMuBeBLktev4hiOAtgsactiYz27iGKx2FOSXpd00Frrr+Cyn3PubpLvArgKQIsxxm/Gmu+cVQwgY4z5bLkInHNZkn6afFnTAD6Q9Jy19s+FbK72MXqxehHHJbUCuJOkP1AFAE9PTk4e6OzsLM4HcsY5BjBE8h4/PgACa+0vUTPhnNtBci+AlKSt1tpPvO7g4OB18Xjc35lNko7EYrEngyA4MWe3LiGR9Iy1dqgeiCqJ2Qdge1XuMWNMz9k6zrlHSL4K4DIAfjpe89NRi5L5JtpSpWTfAehJJBJfTU1NnWpvby8MDw9vKJfLN5C0AB4AsB7A3yR9dDUpWX9/fzqVSu0H8CiAE+VyeWtNUprP5x8m6RnOlRHKMEJyZxAEP0aQRS6Xa6pUKm8B2LFUWn6NrzGAvyR5Wj4myVlrj0dxPF+mt7d3XSqVunDty2gtA/8B7tbLlbiWJAgAAAAASUVORK5CYII=')]").click()
        driver.find_element_by_xpath("//input[@type='search']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//input[@type='search']").clear()
        driver.find_element_by_xpath("//input[@type='search']").send_keys(u"方便面")
        driver.find_element_by_xpath(
            "//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADsElEQVRYR+1XS2icVRg9Z17WKNYRg60P3LnUhaIgbiJaranWmv9eJ1FrsopRFKlILSpEW6iV6kJBjAjRaNLk/jOJ2hottAYRVwURIbXV+gARBdNgwhAd5nHkhomkbWby5wHd5K4G5nuc731+4jw/nmf/WANQNwN9fX0XNTQ0NEvaBuBGAFcDWAdgAsBJkl+USqXBTCbz/XJLuSCA0dHRC2ZmZh6StAfAxsWMS/qoUqnszGQyPywme/b/5wAYGBi4IplMvgPgPgCSNE7yfZJHC4XCr8lkcrpUKl2eSCRuIZkB0AzgEgDTJJ8IguDDpYA4A4BzbgPJQ9V0/07y2SAIDtQzmMvlrpW0T9KDXo5kVxAEb0cF8T8A59zFJAd9RJK+icViJgiCn6MaCsNwF4CXASQA3G+M+TiK7iyAsbGxxMTERBeAN0j+VCwWm1pbW3+LYmC+TBiGuwG8AOB4uVwOojTnLADnXCPJU/63pDZr7adLdT4nH4bhMIBtknY1Njbub2pqKtWzRedcHEAXyTcBHDLG3Ltc514vDMPNAHzTTlcqlWZr7cm6AHp6epLpdHqU5K2S7Eqin5eFwwA2AbjDGHN0sQysJ3kawOnx8fGN3d3dlZVkwOtms9k9kp4H8FI+n3+lo6Pj31o2mc1mb5J0TNLX1trbVuq8CsBKes+XtFgsPt7W1uY354LPA7hL0ucAho0xLasBwDl3O8khSd/G4/HtLS0tf0QBsOIGnHNSDWrA75MoAOZKcMxae/NqZCAMQ7+iewEcXLQEIyMjl5ZKJd+EE6vVhPMW0m5Je621/9QsgXMuBeBLktev4hiOAtgsactiYz27iGKx2FOSXpd00Frrr+Cyn3PubpLvArgKQIsxxm/Gmu+cVQwgY4z5bLkInHNZkn6afFnTAD6Q9Jy19s+FbK72MXqxehHHJbUCuJOkP1AFAE9PTk4e6OzsLM4HcsY5BjBE8h4/PgACa+0vUTPhnNtBci+AlKSt1tpPvO7g4OB18Xjc35lNko7EYrEngyA4MWe3LiGR9Iy1dqgeiCqJ2Qdge1XuMWNMz9k6zrlHSL4K4DIAfjpe89NRi5L5JtpSpWTfAehJJBJfTU1NnWpvby8MDw9vKJfLN5C0AB4AsB7A3yR9dDUpWX9/fzqVSu0H8CiAE+VyeWtNUprP5x8m6RnOlRHKMEJyZxAEP0aQRS6Xa6pUKm8B2LFUWn6NrzGAvyR5Wj4myVlrj0dxPF+mt7d3XSqVunDty2gtA/8B7tbLlbiWJAgAAAAASUVORK5CYII=')]").click()
        driver.find_element_by_xpath(
            "//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADsElEQVRYR+1XS2icVRg9Z17WKNYRg60P3LnUhaIgbiJaranWmv9eJ1FrsopRFKlILSpEW6iV6kJBjAjRaNLk/jOJ2hottAYRVwURIbXV+gARBdNgwhAd5nHkhomkbWby5wHd5K4G5nuc731+4jw/nmf/WANQNwN9fX0XNTQ0NEvaBuBGAFcDWAdgAsBJkl+USqXBTCbz/XJLuSCA0dHRC2ZmZh6StAfAxsWMS/qoUqnszGQyPywme/b/5wAYGBi4IplMvgPgPgCSNE7yfZJHC4XCr8lkcrpUKl2eSCRuIZkB0AzgEgDTJJ8IguDDpYA4A4BzbgPJQ9V0/07y2SAIDtQzmMvlrpW0T9KDXo5kVxAEb0cF8T8A59zFJAd9RJK+icViJgiCn6MaCsNwF4CXASQA3G+M+TiK7iyAsbGxxMTERBeAN0j+VCwWm1pbW3+LYmC+TBiGuwG8AOB4uVwOojTnLADnXCPJU/63pDZr7adLdT4nH4bhMIBtknY1Njbub2pqKtWzRedcHEAXyTcBHDLG3Ltc514vDMPNAHzTTlcqlWZr7cm6AHp6epLpdHqU5K2S7Eqin5eFwwA2AbjDGHN0sQysJ3kawOnx8fGN3d3dlZVkwOtms9k9kp4H8FI+n3+lo6Pj31o2mc1mb5J0TNLX1trbVuq8CsBKes+XtFgsPt7W1uY354LPA7hL0ucAho0xLasBwDl3O8khSd/G4/HtLS0tf0QBsOIGnHNSDWrA75MoAOZKcMxae/NqZCAMQ7+iewEcXLQEIyMjl5ZKJd+EE6vVhPMW0m5Je621/9QsgXMuBeBLktev4hiOAtgsactiYz27iGKx2FOSXpd00Frrr+Cyn3PubpLvArgKQIsxxm/Gmu+cVQwgY4z5bLkInHNZkn6afFnTAD6Q9Jy19s+FbK72MXqxehHHJbUCuJOkP1AFAE9PTk4e6OzsLM4HcsY5BjBE8h4/PgACa+0vUTPhnNtBci+AlKSt1tpPvO7g4OB18Xjc35lNko7EYrEngyA4MWe3LiGR9Iy1dqgeiCqJ2Qdge1XuMWNMz9k6zrlHSL4K4DIAfjpe89NRi5L5JtpSpWTfAehJJBJfTU1NnWpvby8MDw9vKJfLN5C0AB4AsB7A3yR9dDUpWX9/fzqVSu0H8CiAE+VyeWtNUprP5x8m6RnOlRHKMEJyZxAEP0aQRS6Xa6pUKm8B2LFUWn6NrzGAvyR5Wj4myVlrj0dxPF+mt7d3XSqVunDty2gtA/8B7tbLlbiWJAgAAAAASUVORK5CYII=')]").click()
        driver.find_element_by_xpath(
            "//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADsElEQVRYR+1XS2icVRg9Z17WKNYRg60P3LnUhaIgbiJaranWmv9eJ1FrsopRFKlILSpEW6iV6kJBjAjRaNLk/jOJ2hottAYRVwURIbXV+gARBdNgwhAd5nHkhomkbWby5wHd5K4G5nuc731+4jw/nmf/WANQNwN9fX0XNTQ0NEvaBuBGAFcDWAdgAsBJkl+USqXBTCbz/XJLuSCA0dHRC2ZmZh6StAfAxsWMS/qoUqnszGQyPywme/b/5wAYGBi4IplMvgPgPgCSNE7yfZJHC4XCr8lkcrpUKl2eSCRuIZkB0AzgEgDTJJ8IguDDpYA4A4BzbgPJQ9V0/07y2SAIDtQzmMvlrpW0T9KDXo5kVxAEb0cF8T8A59zFJAd9RJK+icViJgiCn6MaCsNwF4CXASQA3G+M+TiK7iyAsbGxxMTERBeAN0j+VCwWm1pbW3+LYmC+TBiGuwG8AOB4uVwOojTnLADnXCPJU/63pDZr7adLdT4nH4bhMIBtknY1Njbub2pqKtWzRedcHEAXyTcBHDLG3Ltc514vDMPNAHzTTlcqlWZr7cm6AHp6epLpdHqU5K2S7Eqin5eFwwA2AbjDGHN0sQysJ3kawOnx8fGN3d3dlZVkwOtms9k9kp4H8FI+n3+lo6Pj31o2mc1mb5J0TNLX1trbVuq8CsBKes+XtFgsPt7W1uY354LPA7hL0ucAho0xLasBwDl3O8khSd/G4/HtLS0tf0QBsOIGnHNSDWrA75MoAOZKcMxae/NqZCAMQ7+iewEcXLQEIyMjl5ZKJd+EE6vVhPMW0m5Je621/9QsgXMuBeBLktev4hiOAtgsactiYz27iGKx2FOSXpd00Frrr+Cyn3PubpLvArgKQIsxxm/Gmu+cVQwgY4z5bLkInHNZkn6afFnTAD6Q9Jy19s+FbK72MXqxehHHJbUCuJOkP1AFAE9PTk4e6OzsLM4HcsY5BjBE8h4/PgACa+0vUTPhnNtBci+AlKSt1tpPvO7g4OB18Xjc35lNko7EYrEngyA4MWe3LiGR9Iy1dqgeiCqJ2Qdge1XuMWNMz9k6zrlHSL4K4DIAfjpe89NRi5L5JtpSpWTfAehJJBJfTU1NnWpvby8MDw9vKJfLN5C0AB4AsB7A3yR9dDUpWX9/fzqVSu0H8CiAE+VyeWtNUprP5x8m6RnOlRHKMEJyZxAEP0aQRS6Xa6pUKm8B2LFUWn6NrzGAvyR5Wj4myVlrj0dxPF+mt7d3XSqVunDty2gtA/8B7tbLlbiWJAgAAAAASUVORK5CYII=')]").click()
        driver.find_element_by_xpath(
            "//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADsElEQVRYR+1XS2icVRg9Z17WKNYRg60P3LnUhaIgbiJaranWmv9eJ1FrsopRFKlILSpEW6iV6kJBjAjRaNLk/jOJ2hottAYRVwURIbXV+gARBdNgwhAd5nHkhomkbWby5wHd5K4G5nuc731+4jw/nmf/WANQNwN9fX0XNTQ0NEvaBuBGAFcDWAdgAsBJkl+USqXBTCbz/XJLuSCA0dHRC2ZmZh6StAfAxsWMS/qoUqnszGQyPywme/b/5wAYGBi4IplMvgPgPgCSNE7yfZJHC4XCr8lkcrpUKl2eSCRuIZkB0AzgEgDTJJ8IguDDpYA4A4BzbgPJQ9V0/07y2SAIDtQzmMvlrpW0T9KDXo5kVxAEb0cF8T8A59zFJAd9RJK+icViJgiCn6MaCsNwF4CXASQA3G+M+TiK7iyAsbGxxMTERBeAN0j+VCwWm1pbW3+LYmC+TBiGuwG8AOB4uVwOojTnLADnXCPJU/63pDZr7adLdT4nH4bhMIBtknY1Njbub2pqKtWzRedcHEAXyTcBHDLG3Ltc514vDMPNAHzTTlcqlWZr7cm6AHp6epLpdHqU5K2S7Eqin5eFwwA2AbjDGHN0sQysJ3kawOnx8fGN3d3dlZVkwOtms9k9kp4H8FI+n3+lo6Pj31o2mc1mb5J0TNLX1trbVuq8CsBKes+XtFgsPt7W1uY354LPA7hL0ucAho0xLasBwDl3O8khSd/G4/HtLS0tf0QBsOIGnHNSDWrA75MoAOZKcMxae/NqZCAMQ7+iewEcXLQEIyMjl5ZKJd+EE6vVhPMW0m5Je621/9QsgXMuBeBLktev4hiOAtgsactiYz27iGKx2FOSXpd00Frrr+Cyn3PubpLvArgKQIsxxm/Gmu+cVQwgY4z5bLkInHNZkn6afFnTAD6Q9Jy19s+FbK72MXqxehHHJbUCuJOkP1AFAE9PTk4e6OzsLM4HcsY5BjBE8h4/PgACa+0vUTPhnNtBci+AlKSt1tpPvO7g4OB18Xjc35lNko7EYrEngyA4MWe3LiGR9Iy1dqgeiCqJ2Qdge1XuMWNMz9k6zrlHSL4K4DIAfjpe89NRi5L5JtpSpWTfAehJJBJfTU1NnWpvby8MDw9vKJfLN5C0AB4AsB7A3yR9dDUpWX9/fzqVSu0H8CiAE+VyeWtNUprP5x8m6RnOlRHKMEJyZxAEP0aQRS6Xa6pUKm8B2LFUWn6NrzGAvyR5Wj4myVlrj0dxPF+mt7d3XSqVunDty2gtA/8B7tbLlbiWJAgAAAAASUVORK5CYII=')]").click()
        driver.find_element_by_xpath(
            "//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADsElEQVRYR+1XS2icVRg9Z17WKNYRg60P3LnUhaIgbiJaranWmv9eJ1FrsopRFKlILSpEW6iV6kJBjAjRaNLk/jOJ2hottAYRVwURIbXV+gARBdNgwhAd5nHkhomkbWby5wHd5K4G5nuc731+4jw/nmf/WANQNwN9fX0XNTQ0NEvaBuBGAFcDWAdgAsBJkl+USqXBTCbz/XJLuSCA0dHRC2ZmZh6StAfAxsWMS/qoUqnszGQyPywme/b/5wAYGBi4IplMvgPgPgCSNE7yfZJHC4XCr8lkcrpUKl2eSCRuIZkB0AzgEgDTJJ8IguDDpYA4A4BzbgPJQ9V0/07y2SAIDtQzmMvlrpW0T9KDXo5kVxAEb0cF8T8A59zFJAd9RJK+icViJgiCn6MaCsNwF4CXASQA3G+M+TiK7iyAsbGxxMTERBeAN0j+VCwWm1pbW3+LYmC+TBiGuwG8AOB4uVwOojTnLADnXCPJU/63pDZr7adLdT4nH4bhMIBtknY1Njbub2pqKtWzRedcHEAXyTcBHDLG3Ltc514vDMPNAHzTTlcqlWZr7cm6AHp6epLpdHqU5K2S7Eqin5eFwwA2AbjDGHN0sQysJ3kawOnx8fGN3d3dlZVkwOtms9k9kp4H8FI+n3+lo6Pj31o2mc1mb5J0TNLX1trbVuq8CsBKes+XtFgsPt7W1uY354LPA7hL0ucAho0xLasBwDl3O8khSd/G4/HtLS0tf0QBsOIGnHNSDWrA75MoAOZKcMxae/NqZCAMQ7+iewEcXLQEIyMjl5ZKJd+EE6vVhPMW0m5Je621/9QsgXMuBeBLktev4hiOAtgsactiYz27iGKx2FOSXpd00Frrr+Cyn3PubpLvArgKQIsxxm/Gmu+cVQwgY4z5bLkInHNZkn6afFnTAD6Q9Jy19s+FbK72MXqxehHHJbUCuJOkP1AFAE9PTk4e6OzsLM4HcsY5BjBE8h4/PgACa+0vUTPhnNtBci+AlKSt1tpPvO7g4OB18Xjc35lNko7EYrEngyA4MWe3LiGR9Iy1dqgeiCqJ2Qdge1XuMWNMz9k6zrlHSL4K4DIAfjpe89NRi5L5JtpSpWTfAehJJBJfTU1NnWpvby8MDw9vKJfLN5C0AB4AsB7A3yR9dDUpWX9/fzqVSu0H8CiAE+VyeWtNUprP5x8m6RnOlRHKMEJyZxAEP0aQRS6Xa6pUKm8B2LFUWn6NrzGAvyR5Wj4myVlrj0dxPF+mt7d3XSqVunDty2gtA/8B7tbLlbiWJAgAAAAASUVORK5CYII=')]").click()
        driver.find_element_by_xpath("//input[@type='search']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//input[@type='search']").clear()
        driver.find_element_by_xpath("//input[@type='search']").send_keys(u"方便面")
        driver.find_element_by_xpath("//input[@type='search']").send_keys(Keys.ENTER)
        # 生成日志
        links = driver.find_elements_by_xpath("//input[@type='search']")
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
    report = REPORT_PATH + '/one.html'
    HTMLTestRunner.HTMLTestRunner(
        stream=open(report, 'wb'),
        title="自动化测试报告",
        description="自动化测试执行的详细信息"
    ).run(UntitledTestCase3('test_untitled_test_case3'))

# -*- coding: utf-8 -*-

from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        ele_click = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        ele_right_click = self.driver.find_element_by_xpath("/html/body/form/input[4]")
        ele_double_click = self.driver.find_element_by_xpath("/html/body/form/input[2]")
        action = ActionChains(self.driver)
        action.click(ele_click)
        action.context_click(ele_right_click)
        action.double_click(ele_double_click)
        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element_by_link_text("设置")
        # ele = self.driver.find_element_by_xpath("//*[@id='s-usersetting-top']")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        ele_drag = self.driver.find_element_by_id("dragger")
        ele_drop = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        # action.drag_and_drop(ele_drag, ele_drop).perform()
        # action.click_and_hold(ele_drag).release(ele_drop).perform()
        action.click_and_hold(ele_drop).move_to_element(ele_drop).release().perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("hello").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

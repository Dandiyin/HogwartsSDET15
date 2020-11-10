# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver

from web.selenium_window_frame.base import Base


class TestWindows(Base):

    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        # 打印当前窗口
        print(self.driver.current_window_handle)
        # 打印所有窗口
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        # 切换窗口到列表返回的最后一个
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("12345678")
        sleep(3)
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys('12345678')
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)

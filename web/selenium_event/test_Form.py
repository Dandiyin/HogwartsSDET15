# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver


class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("872332156@qq.com")
        self.driver.find_element_by_id("user_password").send_keys("ssmtx5211314ddd")
        self.driver.find_element_by_id("user_remember_me").click()
        self.driver.find_element_by_name("commit").click()
        sleep(3)

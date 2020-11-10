#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestTestdemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("http://ruhua.txbapp.com/")
        sleep(3)

    def test_user(self):
        self.driver.find_element_by_link_text("用户平台").click()

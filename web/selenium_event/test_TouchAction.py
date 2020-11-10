# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class Test_TouchAction():
    def setup(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(chrome_options=opt)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_case(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        action_search = TouchActions(self.driver)
        action_search.tap(self.driver.find_element_by_id("su")).perform()
        el = self.driver.find_element_by_id("su")
        action = TouchActions(self.driver)
        # 向上滑动10000个像素
        action.scroll_from_element(el, 0, 10000).perform()
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        sleep(3)

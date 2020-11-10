# -*- coding: utf-8 -*-
from time import sleep

from web.selenium_js.base import Base


class TestJS(Base):

    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        sleep(3)
        # for code in [
        #     'return document.title','return JSON.stringify(performance.timing)'
        # ]:
        # print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))
        print(self.driver.execute_script("return JSON.stringify(performance.timing)"))

# -*- coding: utf-8 -*-
from time import sleep

from web.selenium_js.base import Base


class TestJSDataTime(Base):

    def test_js_datatime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a=document.getElementById('train_date')")
        self.driver.execute_script("a.removeAttribute('readonly')")
        self.driver.execute_script("a.value='2020-12-01'")
        sleep(2)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))

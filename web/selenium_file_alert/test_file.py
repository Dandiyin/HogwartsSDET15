# -*- coding: utf-8 -*-
from time import sleep

from web.selenium_window_frame.base import Base


class TestFile(Base):

    def test_file_upload(self):
        self.driver.get("https://images.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys(
            "/Users/dandanyin/Downloads/4636e68593db881dc54297026d507eb5.jpg")
        sleep(3)

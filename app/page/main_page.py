# -*- coding: utf-8 -*-
import os

import yaml
from appium.webdriver.common.mobileby import MobileBy

from app.page.addresslist_page import AddressListPage
from app.page.base_page import BasePage

"""首页"""


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    '''
    进入到消息页
    '''

    def goto_message(self):
        pass

    '''
    进入到通讯录页面
    '''

    def goto_address(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # cur_path = os.path.dirname(os.path.realpath(__file__))
        # yaml_path = os.path.join(cur_path, "main.yml")
        self.parse_yaml("../app/page/main.yml", "goto_address")
        return AddressListPage(self.driver)

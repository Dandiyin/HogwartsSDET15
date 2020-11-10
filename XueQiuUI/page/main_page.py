# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from app.paga.addresslist_page import AddressListPage
from app.paga.base_page import Base_Page

"""首页"""


class MainPage(Base_Page):
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
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self.driver)

# -*- coding: utf-8 -*-
import os

from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage

'''
编辑成员页
'''


class ContactEditPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    def click_delete(self):
        self.find_by_scroll("删除成员").click()
        # self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        self.parse_yaml("../app/page/contact_edit.yml", "click_delete")
        from app.page.addresslist_page import AddressListPage
        return AddressListPage(self.driver)

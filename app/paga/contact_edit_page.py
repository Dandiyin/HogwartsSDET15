# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from app.paga.base_page import Base_Page

'''
编辑成员页
'''


class ContactEditPage(Base_Page):

    # def __init__(self, driver):
    #     self.driver = driver

    def click_delete(self):
        self.find_by_scroll("删除成员").click()
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        from app.paga.addresslist_page import AddressListPage
        return AddressListPage(self.driver)

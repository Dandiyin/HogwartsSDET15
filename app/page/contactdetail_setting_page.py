# -*- coding: utf-8 -*-
import os

from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.contact_edit_page import ContactEditPage

'''
个人信息设置页
'''


class ContactDetailSettingPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def click_editmember(self):
        # self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.parse_yaml("../app/page/contactdetail_setting.yml", "click_editmember")
        return ContactEditPage(self.driver)

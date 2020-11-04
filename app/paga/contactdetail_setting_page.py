# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from app.paga.base_page import Base_Page
from app.paga.contact_edit_page import ContactEditPage

'''
个人信息设置页
'''


class ContactDetailSettingPage(Base_Page):
    # def __init__(self, driver):
    #     self.driver = driver

    def click_editmember(self):
        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        return ContactEditPage(self.driver)

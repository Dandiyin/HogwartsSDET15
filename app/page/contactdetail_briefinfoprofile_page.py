# -*- coding: utf-8 -*-
import os

from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.contactdetail_setting_page import ContactDetailSettingPage

'''
个人信息页
'''


class ContactDetailBriefInfoProfilePage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    def click_more(self):
        # self.find(MobileBy.ID, "com.tencent.wework:id/hxm").click()
        self.parse_yaml("../app/page/contactdetail_briefinfoprofile.yml", "click_more")
        return ContactDetailSettingPage(self.driver)

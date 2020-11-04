# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from app.paga.base_page import Base_Page
from app.paga.contactdetail_setting_page import ContactDetailSettingPage

'''
个人信息页
'''


class ContactDetailBriefInfoProfilePage(Base_Page):

    # def __init__(self, driver):
    #     self.driver = driver

    def click_more(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/hxm").click()
        return ContactDetailSettingPage(self.driver)

# -*- coding: utf-8 -*-
import os

from appium.webdriver.common.mobileby import MobileBy

from app.paga.base_page import BasePage
from app.paga.contactdetail_setting_page import ContactDetailSettingPage

'''
个人信息页
'''


class ContactDetailBriefInfoProfilePage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    def click_more(self):
        # self.find(MobileBy.ID, "com.tencent.wework:id/hxm").click()
        cur_path = os.path.dirname(os.path.realpath(__file__))
        yaml_path = os.path.join(cur_path, "contactdetail_briefinfoprofile.yml")
        # print(yaml_path)
        self.parse_yaml(yaml_path, "click_more")
        return ContactDetailSettingPage(self.driver)

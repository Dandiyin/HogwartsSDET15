# -*- coding: utf-8 -*-
import os

from appium.webdriver.common.mobileby import MobileBy

from app.paga.base_page import BasePage
from app.paga.contact_edit_page import ContactEditPage

'''
个人信息设置页
'''


class ContactDetailSettingPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def click_editmember(self):
        # self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        cur_path = os.path.dirname(os.path.realpath(__file__))
        yaml_path = os.path.join(cur_path, "contactdetail_setting.yml")
        # print(yaml_path)
        self.parse_yaml(yaml_path, "click_editmember")
        return ContactEditPage(self.driver)

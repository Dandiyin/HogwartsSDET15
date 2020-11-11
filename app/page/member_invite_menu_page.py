# -*- coding: utf-8 -*-
import os

from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage

'''
邀请页面
'''


class MemberInviteMenuPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    def add_member_menual(self):
        # self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.parse_yaml("../app/page/member_invite_menu_page.yml", "add_member_menu")
        # 局部导入
        from app.page.contact_add_page import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        result = self.get_toast_text()
        return result

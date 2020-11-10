# -*- coding: utf-8 -*-
import os

from appium.webdriver.common.mobileby import MobileBy

from app.paga.base_page import BasePage

'''
邀请页面
'''


class MemberInviteMenuPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    def add_member_menual(self):
        # self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        cur_path = os.path.dirname(os.path.realpath(__file__))
        yaml_path = os.path.join(cur_path, "member_invite_menu_page.yml")
        print(yaml_path)
        self.parse_yaml(yaml_path, "add_member_menu")
        # 局部导入
        from app.paga.contact_add_page import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        result = self.get_toast_text()
        return result

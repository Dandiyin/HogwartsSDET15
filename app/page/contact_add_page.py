# -*- coding: utf-8 -*-
# 编辑联系人页面
import os

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app.page.base_page import BasePage

'''
添加成员页
'''


class ContactAddPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    # def add_contact(self, name, gender, phonenum):
    #     self.find(MobileBy.XPATH,
    #               "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
    #     self.find(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']").click()
    #
    #     if gender == "男":
    #         WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
    #         self.find(MobileBy.XPATH, "//*[@text='男']").click()
    #     else:
    #         self.find(MobileBy.XPATH, "//*[@text='女']").click()
    #
    #     self.find(MobileBy.XPATH,
    #               '//*[contains(@text, "手机") and contains(@class, "TextView")]/..//android.widget.EditText').send_keys(
    #         phonenum)
    #     self.find(MobileBy.XPATH, "//*[@text='保存']").click()
    #     # 局部导入
    #     from app.page.member_invite_menu_page import MemberInviteMenuPage
    #     return MemberInviteMenuPage(self.driver)

    def add_contact(self):
        self.parse_yaml("../app/page/contact_add.yml", "add_contact")
        # 局部导入
        from app.page.member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)

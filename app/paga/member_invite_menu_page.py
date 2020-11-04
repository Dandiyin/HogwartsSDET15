# -*- coding: utf-8 -*-


from appium.webdriver.common.mobileby import MobileBy

from app.paga.base_page import Base_Page

'''
邀请页面
'''


class MemberInviteMenuPage(Base_Page):

    # def __init__(self, driver):
    #     self.driver = driver

    def add_member_menual(self):
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 局部导入
        from app.paga.contact_add_page import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        result = self.get_toast_text()
        return result

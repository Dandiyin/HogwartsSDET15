# -*- coding: utf-8 -*-

# 通讯录页面
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app.paga.base_page import Base_Page
from app.paga.contactdetail_briefinfoprofile_page import ContactDetailBriefInfoProfilePage
from app.paga.member_invite_menu_page import MemberInviteMenuPage

'''
通讯录列表页
'''


class AddressListPage(Base_Page):

    # def __init__(self, driver):
    #     self.driver = driver

    def click_addmember(self):
        self.find_by_scroll("添加成员").click()
        return MemberInviteMenuPage(self.driver)

    def select_member(self, name):
        self.find_by_scroll(name).click()
        return ContactDetailBriefInfoProfilePage(self.driver)

    def search_member(self, name):
        self.find(MobileBy.ID, "com.tencent.wework:id/hxw").click()
        self.find_and_sendkeys(MobileBy.XPATH, "//*[@text='搜索']", name)
        # return self.find(MobileBy.XPATH, "//*[contains(@text='网络查找手机/邮箱')]")
        return WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(MobileBy.XPATH, "//*[contains(@text,'网络查找手机/邮箱')]")).text

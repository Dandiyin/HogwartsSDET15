# -*- coding: utf-8 -*-
import os

from appium.webdriver.common.mobileby import MobileBy

from app.paga.base_page import BasePage

'''
编辑成员页
'''


class ContactEditPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    def click_delete(self):
        self.find_by_scroll("删除成员").click()
        # self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        cur_path = os.path.dirname(os.path.realpath(__file__))
        yaml_path = os.path.join(cur_path, "contact_edit.yml")
        # print(yaml_path)
        self.parse_yaml(yaml_path, "click_delete")
        from app.paga.addresslist_page import AddressListPage
        return AddressListPage(self.driver)

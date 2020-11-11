# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app.page.app import App


class TestContact:

    def setup(self):
        # 实例化app
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_add_contact(self):
        # name = "hogwarts_003"
        # gender = "男"
        # phonenum = "13500000003"
        result = self.main.goto_address() \
            .click_addmember() \
            .add_member_menual() \
            .add_contact().get_toast()
        assert '添加成功' == result

    def test_delete_contact(self):
        name = 'hogwarts_004'
        result = self.main.goto_address().select_member(
            name).click_more().click_editmember().click_delete().search_member()
        assert '网络查找手机/邮箱：' in result

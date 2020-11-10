# -*- coding: utf-8 -*-

"""
base_page.py 基类模块：主要用于初始化driver, 定义find, 常用的最基本的方法
"""
import os

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from app.paga.hand_black import handle_black


class BasePage:
    black_list = [(By.XPATH, "")]
    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @handle_black
    def find(self, by, locator=None):

        # 如果传的元素是一个，只有by
        if locator is None:
            result = self.driver.find_element(*by)
        # 如果传的元素是两个，既有by，又有locator
        else:
            result = self.driver.find_element(by, locator)
        return result

    def find_and_click(self, by, locator):
        return self.find(by, locator).click()

    def find_and_sendkeys(self, by, locator, text):
        return self.find(by, locator).send_keys(text)

    def find_by_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result

    def get_cur_path(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        return cur_path

    def parse_yaml(self, path, func_name):
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
            self.parse(data[func_name])

    def parse(self, steps):
        for step in steps:
            if 'click' == step['action']:
                self.find(step['by'], step['locator']).click()
            elif 'send_keys' == step['action']:
                self.find(step['by'], step['locator']).send_keys(step['content'])
            elif 'scroll' == step['action']:
                pass
                # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                #                          f'new UiScrollable(new UiSelector()\
                #                                  .scrollable(true).instance(0))\
                #                                  .scrollIntoView(new UiSelector()\
                #                                  .text("{text}").instance(0));')

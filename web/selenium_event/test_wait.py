# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.ID, '//*[@title="所有分类"]').click()

        # def wait(x):
        #     return len(self.driver.find_element(By.XPATH, '//*[@class="table-heading"]')) >= 1

        # WebDriverWait(self.driver, 10).until(wait)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(By.XPATH, '//*[@class="table-heading"]'))
        self.driver.find_element(By.XPATH, '//[*title="在最近的一年，一月，一周或一天最活跃的主题"]').click()

# -*- coding: utf-8 -*-
import yaml
from appium import webdriver

from app.paga.base_page import Base_Page
from app.paga.main_page import MainPage

with open('./config/caps.yml') as f:
    myconfig = yaml.safe_load(f)
    caps = myconfig['caps']
    ip = myconfig['server']['ip']
    port = myconfig['server']['port']


class App(Base_Page):
    def start(self):
        if self.driver == None:
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)

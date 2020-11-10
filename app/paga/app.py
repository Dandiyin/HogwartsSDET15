# -*- coding: utf-8 -*-
import yaml
from appium import webdriver

from app.paga.base_page import BasePage
from app.paga.main_page import MainPage

with open('./config/caps.yml') as f:
    myconfig = yaml.safe_load(f)
    caps = myconfig['caps']
    ip = myconfig['server']['ip']
    port = myconfig['server']['port']


class App(BasePage):
    def start(self):
        if self.driver is None:

            # 启动完停留在当前页面
            # 定义了一个字典
            # caps = {}
            # caps["platformName"] = "Android"
            # caps["platformVersion"] = "6.0.1"
            # caps["deviceName"] = 'emulator-5554'
            # caps["appPackage"] = "com.tencent.wework"
            # caps["appActivity"] = ".launch.LaunchSplashActivity"
            # caps["noReset"] = "True"
            # # 不停止应用，直接运行测试用例
            # # caps["dontStopAppOnReset"] = "true"
            # # caps['skipDeviceInitialization'] = 'true'
            # # caps['skipServerInstallation'] = 'true'
            # # caps["settings[waitForIdleTimeout]"] = 0
            # # 关键  localhost:4723  本机ip:server端口
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

# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 15:08
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : app.py
# @Software: PyCharm
from page.main import Main
from page.black import Black
from appium import webdriver
from base.configuration import GetConfiguration
from base.basePage import BaseAndroidOperation


class App(BaseAndroidOperation):
    _appPackage = "com.xueqiu.android"
    _appActivity = ".common.MainActivity"

    def start(self):

        if self._driver is None:
            caps = {"deviceName": '192.168.62.102:5555', "platformVersion": '6.0', "appPackage": self._appPackage,
                    "appActivity": self._appActivity}
            caps_common = GetConfiguration().get_driver_caps()
            # 将driver.yaml文件中参数读出。加入到caps
            caps.update(caps_common)
            print("加入driver.yaml参数:", caps)  # TODO to delete
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self._driver.start_activity(self._appPackage, self._appActivity)
        return self

    def main(self) -> Main:
        return Main(self._driver)

    def black(self)->Black:
        return Black(self._driver)


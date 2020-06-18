# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 0:46
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : Search.py
# @Software: PyCharm

from page import *
import allure


class Search(BaseAndroidOperation):

    def __init__(self, driver):
        self._driver = driver

    @allure.step("搜索关键词")
    def search(self, name):
        self._params["key"] = name
        self.steps("./page/Search.yaml")

    @allure.step("加自选")
    def add(self):
        self.steps("./page/Search.yaml")

    @allure.step("判断是否选中")
    def is_choozen(self):
        return self.steps("./page/Search.yaml")

    @allure.step("清空选中状态")
    def reset(self):
        self.steps("./page/Search.yaml")

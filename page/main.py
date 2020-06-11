# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 15:11
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : main.py
# @Software: PyCharm

from page import *
from page.black import Black
from page.searchPage import searchPage


class Main(BaseAndroidOperation):

    def __init__(self, driver):
        self._driver = driver


    def goto_search(self) -> searchPage:

        #print(self._driver.window_handles, "=================================")
        self.steps("page/main.yaml")
        return searchPage(self._driver)

    def goto_write(self) -> Black:
        self.steps(r"page\black.yaml")
        return Black(self._driver)

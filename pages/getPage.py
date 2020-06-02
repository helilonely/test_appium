# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 12:02
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : getPage.py
# @Software: PyCharm

from pages.MainPage import MainPage
from pages.SearchPage import SearchPage

class GetPage:
    def __init__(self,driver):
        self._driver = driver

    def get_main_page(self):
        return MainPage(self._driver)

    def get_search_page(self):
        return SearchPage(self._driver)
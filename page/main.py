# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 15:11
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : main.py
# @Software: PyCharm

from page import *
from page.Search import Search


class Main(BaseAndroidOperation):

    def __init__(self, driver):
        self._driver = driver
        self._driver.set_network_connection(6)

    def goto_search(self) -> Search:
        self.steps("page/main.yaml")
        return Search(self._driver)

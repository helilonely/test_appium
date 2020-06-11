# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 0:46
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : searchPage.py
# @Software: PyCharm

from page import *


class searchPage(BaseAndroidOperation):

    def __init__(self, driver):
        self._driver = driver


    def search(self):
        self.steps("./page/searchPage.yaml")

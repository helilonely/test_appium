# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 15:23
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : black.py
# @Software: PyCharm
from page import *


class Black(BaseAndroidOperation):
    def __init__(self, driver):
        self._driver = driver

    def goto_post(self) :
        self.steps("page/black_post.yaml")


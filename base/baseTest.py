# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 14:38
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : baseTest.py
# @Software: PyCharm
from page.app import App


class BaseTest:
    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app._driver.quit()

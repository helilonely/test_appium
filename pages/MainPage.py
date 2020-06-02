# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 15:30
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : MainPage.py
# @Software: PyCharm

from hamcrest import *
from pages import *


class MainPage(BaseAndroidOperation):

    def __init__(self, driver):
        self._driver = driver
        super().__init__(self._driver)
        self.eles = BaseYaml().get_all_data(path=r"pages\MainPage.yaml")

    @allure.step("跳转到搜索页面")
    def goto_search(self):
        ele1 = self.eles["search"][0]
        self.base_find_element(ele1).click()

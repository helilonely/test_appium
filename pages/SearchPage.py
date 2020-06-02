# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 18:09
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : SearchPage.py
# @Software: PyCharm
from pages import *
from appium import webdriver


class SearchPage(BaseAndroidOperation):

    def __init__(self, driver:webdriver):
        self._driver = driver
        super().__init__(self._driver)
        self.eles = BaseYaml().get_all_data(path=r"pages\SearchPage.yaml")

    @allure.step("输入搜索的文本")
    def input_search_text(self, text):
        ele1_locator = self.eles["search"][0]
        ele1=self.base_find_element(ele1_locator)
        ele1.click()
        ele1.clear()
        ele1.send_keys(text)

    @allure.step("选择代码为BABA的股票")
    def chose_first_one(self):
        ele1_locator = self.eles["choose"][0]
        ele1 = self.base_find_element(ele1_locator)
        ele1.click()
        ele2_locator = self.eles["choose"][1]
        ele2 = self.base_find_element(ele2_locator)
        self.base_scroll()
        return ele2.text




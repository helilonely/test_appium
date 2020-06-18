# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 16:17
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : test_search.py
# @Software: PyCharm
import os, sys
sys.path.append(os.getcwd())
import pytest
import hamcrest
import allure



from base.baseTest import BaseTest
import pytest




@allure.feature("雪球搜索功能")
class TestSearch(BaseTest):

    def setup(self):
        self._search=self.app.start().main().goto_search()

    @allure.story("搜索股票")
    @pytest.mark.yes
    @pytest.mark.parametrize("name", ["alibaba", "xiaomi"])
    def test_search(self, name):
        try:

            self._search.search(name)
            if self._search.is_choozen():
                self._search.reset()
                self._search.add()
            hamcrest.assert_that(self._search.is_choozen(), hamcrest.equal_to(True))
        except Exception as e:
            self.app.save_screen_shoot("")
            raise e

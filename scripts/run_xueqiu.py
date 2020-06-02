# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 16:01
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : run_xueqiu.py.py
# @Software: PyCharm
import allure
import os, sys
import time

import pytest

sys.path.append(os.getcwd())

from pages.getPage import GetPage
from base.get_driver import get_driver
from hamcrest import *

class TestXueQiu(object):
    def setup_class(self):
        self._driver = get_driver()
        self._getpage = GetPage(self._driver)

    def teardown_class(self):
        time.sleep(15)
        self._driver.quit()


    @allure.feature("雪球")
    @allure.story("主页搜索")
    @pytest.mark.parametrize("text", ["alibaba"])
    def test_search_alibaba(self, text):
        main_page = self._getpage.get_main_page()
        main_page.goto_search()
        search_page = self._getpage.get_search_page()
        #将搜索到的内容加到附件
        allure.attach("搜索的内容是%s"%text)
        search_page.input_search_text(text)
        result=search_page.chose_first_one()
        #hamcrest断言
        assert_that(result,equal_to("加自选"))

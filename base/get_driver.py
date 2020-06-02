# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 17:25
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : get_driver.py
# @Software: PyCharm

from base.File import BaseYaml
from appium import webdriver



def get_driver():
    try:
        caps = BaseYaml().get_all_data(path="base/driver.yaml")
        print(caps)           #TODO 查看获得的参数
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=caps)

        return driver
    except FileNotFoundError:
        raise "{}路径的dirver配置文件未找到！".format("base/driver.yaml")





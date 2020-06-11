# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 15:53
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : configuration.py
# @Software: PyCharm
import os
from appium import webdriver

from base.File import BaseYaml
import yaml


class GetConfiguration:
    # 读取yaml文件的内容
    caps: dict = yaml.safe_load(open(r"base/configuration.yaml", "r", encoding="utf-8"))
    # 将三个参数的值加上 绝对路径
    list1 = ["app", "chromedriverExecutableDir", "chromedriverChromeMappingFile"]

    def get_driver_caps(self) -> dict:
        try:
            for temp in self.list1:
                if temp in self.caps:
                    self.caps[temp] = os.getcwd() + self.caps.get(temp)
          #  print(self.caps)  # TODO 查看获得的参数  待删除
            return self.caps
        except FileNotFoundError:
            raise "{}路径的dirver配置文件未找到！".format("base/configuration.yaml")


if __name__ == '__main__':
    GetConfiguration().get_driver_caps()

# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 17:03
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : File.py
# @Software: PyCharm
import yaml


class BaseYaml(object):
    def get_all_data(self, path):
        with open(path, "r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)
        return self.data

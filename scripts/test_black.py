# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 16:17
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : test_main.py
# @Software: PyCharm
import os,sys

import pytest
import subprocess
sys.path.append(os.getcwd())

from base.baseTest import BaseTest


class TestBlack(BaseTest):

    @pytest.mark.no
    def test_main(self):
        self.app.start().main().goto_write().goto_post()
    @pytest.mark.no
    def test_pp(self):
        p=subprocess.Popen(r" adb devices | grep  -E '\bdevice\b'  | awk '{print $1}'",shell=True)
        print("dddddddddddddddddddd",p)

# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 15:54
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : conftest.py
# @Software: PyCharm


import os, shlex
import signal

import subprocess
import time

import pytest


@pytest.fixture(scope="module", autouse=True)
def record():
    cmd = shlex.split("scrcpy --record  vedio/{}.mp4".format(time.strftime("_%Y_%m_%d_%H_%M_%S")))

    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)
# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 15:09
# @Author  : heli
# @Email   : 1013828952@qq.com
# @File    : wrapper.py
# @Software: PyCharm
import logging
from functools import wraps
import time



def handler_black(func):

    #引用放在此处 ，避免循环引用。 basepage引用了wrapper
    # 此处引用是为了给instance加注解.
    # from base.basePage import BaseAndroidOperation

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='log/{}.log'.format(time.strftime("%Y_%m_%d")),
                        filemode='w')

    # @wraps(func)#
    def wrapper(*args, **kwargs):
        _black_lsit = [
                       ("id", "com.xueqiu.android:id/ib_close"),
                       ("id", "com.xueqiu.android:id/tv_agree"),
                       ("xpth", "//*[@text='下次再说' and @resource-id='com.xueqiu.android:id/tv_left']"),
                       ]

        _max_num = 3
        _error_num = 0
        instance = args[0]

        try:

            logging.info("run "+func.__name__+"\n args:"+repr(args)+"\n kwargs:"+repr(kwargs))

            element = func(*args, **kwargs)
            _error_num = 0
            instance._driver.implicitly_wait(15)
            return element
        except Exception as e:
            instance._driver.implicitly_wait(1)
            if _error_num > _max_num:
                raise e
            _error_num += 1

            for black in instance._black_lsit:
                elements = instance._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper

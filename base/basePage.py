# -*- encoding=utf8 -*-
# 作者           :heli 
# 创建时间       :2020/5/20  15:57
# 文件           :basePage.py
# IDE            :PyCharm
import inspect
import json
import logging

import time

import allure
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from base.wrapper import handler_black
import os

class BaseAndroidOperation:
    # 弹框中的元素若定位到说明弹框出现，一般为是使得弹窗消失的元素
    _black_lsit = [("id", "com.xueqiu.android:id/ib_close"), ("id", "com.xueqiu.android:id/tv_agree")]  #
    # 用于接收变量，如send_keys的变量
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver: WebDriver = driver

    def save_screen_shoot(self, name):
        ''' 截图 名字已包含时间戳
        :param name:
        :return:
        '''
        path=os.getcwd()+"/imgs/"
        time_name="{0}{1}.png".format(name, time.strftime("_%Y_%m_%d %H_%M_%S"))
        filename=path+time_name
        self._driver.save_screenshot(filename)
        with open(filename,"rb") as f:
            content=f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG)
        logging.error("something goes wrong")
    '''
    定位元素
    '''

    @handler_black
    def base_find_element(self, locator, timeout=10, frequency=0.5):

        return WebDriverWait(self._driver, timeout, frequency).until(lambda x: x.find_element(*locator))

    def base_find_elements(self, locator, timeout=10, frequency=0.5):

        return WebDriverWait(self._driver, timeout, frequency).until(lambda x: x.find_elements(*locator))

    '''
    点击元素
    '''

    def base_click_element(self, locator, timeout=10, frequency=0.5):
        self.base_find_element(locator, timeout, frequency).click()

    def base_send_text(self, locator, text, timeout=10, frequency=0.5, clear=True):
        '''
        :param locator:     定位 baokuo by
        :param text:        输入的文本
        :param clear:     为true清空原有文本
        '''
        el = self.base_find_element(locator, timeout, frequency)
        if clear:
            el.clear()
        el.send_keys(text)

    def steps(self, path):
        '''
        解析yaml文件元素，并根据元素信息进行操作
        :param path:  yaml文件路径
        '''
        with open(path, "r", encoding="utf-8") as f:
            # 此处取调用step的函数的函数名，yaml文件中，参数用函数名做标识
            func_name = inspect.stack()[1].function
            steps: list[dict] = yaml.safe_load(f)[func_name]

            '''
            yaml文件中变化的部分设置为变量。此处将变化的部分替换为需要的参数。 
            先转化为字符串。再将字符串中部分替换为需要的。
            '''
            raw = json.dumps(steps)
            not_raw = ""
            for _params_name, _params_value in self._params.items():
                not_raw = raw.replace("${" + _params_name + "}", _params_value)
            if len(not_raw) > 1:
                steps = json.loads(not_raw)

        element = None

        for step in steps:
            if "by" in step.keys():
                if "action" in step.keys():
                    action = step["action"]
                    if "len>0" == action:
                        element = self.base_find_elements((step["by"], step["locator"]))
                        return len(element) > 0
                    else:
                        element = self.base_find_element((step["by"], step["locator"]))
                        action_demo = ["click", "clear", "send"]
                        for x in action_demo:
                            if x in action:
                                # 记录信息
                                if x == "click":
                                    element.click()
                                elif x == "send":
                                    element.send_keys(step["value"])
                                elif x == "clear":
                                    element.clear()

    @property
    def driver(self):
        return self._driver


if __name__ == '__main__':
    # caps = {
    #     "platformVersion": "6.0.1",
    #     "platformName": "android",
    #     "appPackage": "com.android.browser",
    #     "appActivity": ".BrowserActivity",
    #     "deviceName": "127.0.0.1:7555",
    #     "noReset": "true",  # 不会重置用户数据
    #     "dontStopAppOnReset": "true",  # 复用的概念，不会重启app.
    #     "skipDeviceInitialization": "true"  # 跳过设备的初始化操作
    # }
    #
    # driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    #
    # ba = BaseAndroidOperation(driver)
    # ba.base_click_element((MobileBy.ID, "com.android.browser:id/close"))
    # time.sleep(2)
    # driver.quit()

    raw = json.dumps([{"by": "id", "locator": "com.xueqiu.android:id/search_input_text", "action": "click"},
                      {"by": "id", "locator": "com.xueqiu.android:id/search_input_text", "action": "clear send",
                       "value": "${key}"}])
    print(raw, type(raw))
    aaa = raw.replace(r"${key}", "alili")
    print(raw)
    print(aaa)

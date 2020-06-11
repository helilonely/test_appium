# -*- encoding=utf8 -*-
# 作者           :heli 
# 创建时间       :2020/5/20  15:57
# 文件           :basePage.py
# IDE            :PyCharm
import time

import yaml
from appium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy


class BaseAndroidOperation():
    # 弹框中的元素若定位到说明弹框出现，一般为是使得弹窗消失的元素
    _black_lsit = [("id", "com.xueqiu.android:id/ib_close"), ("id", "com.xueqiu.android:id/tv_agree")]  #

    def __init__(self, driver: webdriver = None):
        self._driver = driver
        # self._driver = webdriver.Remote("", "")

    def base_find_element(self, locator, timeout=10, frequency=0.5):
        '''
         1 定位元素，捕获异常，如果未找到，则有可能是出现弹窗。
         2 弹窗处理
        :param locator:
        '''
        try:

            return WebDriverWait(self._driver, timeout, frequency).until(lambda x: x.find_element(*locator))
        except:
            flag = 0
            for black in self._black_lsit:
                elements = self._driver.find_elements(*black)
                flag = len(elements)
                if flag > 0:
                    elements[0].click()
                    break
            if flag > 0:
                return self.base_find_element(locator, timeout, frequency)
            else:
                raise Exception("定位失败", locator)

    def base_click_element(self, locator, timeout=10, frequency=0.5):
        self.base_find_element(locator, timeout, frequency).click()

    def base_send_text(self, locator, text, timeout=10, frequency=0.5, clear=True):
        '''
        :param locator:     定位 baokuo by
        :param text:        输入的文本
        :param timeout:
        :param frequency:
        :param clear:     为true清空原有文本
        :return:
        '''
        el = self.base_find_element(locator, timeout, frequency)
        if clear:
            el.clear()
        el.send_keys(text)

    def steps(self, path):
        '''
        解析yaml文件元素，并根据元素信息进行操作
        :param path:  yaml文件路径
        :return:
        '''
        with open(path, "r", encoding="utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)
        element = None
        for step in steps:
            if "by" in step.keys():
                element = self.base_find_element((step["by"], step["locator"]))
            if "action" in step.keys():
                action = step["action"]
                action_demo = ["click", "clear", "send"]
                for x in action_demo:
                    if x in action:
                        if x == "click":
                            element.click()
                        elif x == "send":
                            element.send_keys(step["value"])
                        elif x == "clear":
                            element.clear()


if __name__ == '__main__':
    caps = {
        "platformVersion": "6.0.1",
        "platformName": "android",
        "appPackage": "com.android.browser",
        "appActivity": ".BrowserActivity",
        "deviceName": "127.0.0.1:7555",
        "noReset": "true",  # 不会重置用户数据
        "dontStopAppOnReset": "true",  # 复用的概念，不会重启app.
        "skipDeviceInitialization": "true"  # 跳过设备的初始化操作
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    ba = BaseAndroidOperation(driver)
    ba.base_click_element((MobileBy.ID, "com.android.browser:id/close"))
    time.sleep(2)
    driver.quit()

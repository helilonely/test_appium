# -*- encoding=utf8 -*-
# 作者           :heli 
# 创建时间       :2020/5/20  15:57
# 文件           :Base.py
# IDE            :PyCharm
import time

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions as STouchAction


class BaseAndroidOperation():
    def __init__(self, driver):
        self._driver = driver
        self._TouchAction = TouchAction(self._driver)
        self._TouchAction_selenium = STouchAction(self._driver)

        pass

    def base_find_element(self, locator, timeout=10, frequency=0.5):
        if isinstance(locator, tuple):
            return WebDriverWait(self._driver, timeout, frequency).until(EC.presence_of_element_located(locator))
        else:
            return WebDriverWait(self._driver, timeout, frequency).until(
                lambda x: x.find_element(locator.get("by"), locator.get("locator")))

    def base_click_element(self, locator, timeout=10, frequency=0.5):
        self.base_find_element(locator, timeout, frequency).click()

    def base_send_text(self, locator, text, timeout=10, frequency=0.5, clear=True):
        el = self.base_find_element(locator, timeout, frequency)
        if clear:
            el.clear()
        el.send_keys(text)

    def action(self):
        pass

    def base_scroll(self):
        self._TouchAction_selenium.scroll(0, 0.8 * self._driver.get_window_size().get("height"))


if __name__ == '__main__':
    caps = {
        "platformVersion": "6.0",
        "platformName": "android",
        "appPackage": "com.android.browser",
        "appActivity": ".BrowserActivity",
        "deviceName": "192.168.62.102:5555",
        "noReset": "true",  # 不会重置用户数据
        "dontStopAppOnReset": "true",  # 复用的概念，不会重启app.
        "skipDeviceInitialization": "true"  # 跳过设备的初始化操作
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    ba = BaseAndroidOperation(driver)
    print(ba.base_find_element((MobileBy.ID, "com.android.browser:id/close")).get_attribute("package"))
    ba.base_click_element((MobileBy.ID, "com.android.browser:id/close"))
    time.sleep(2)
    driver.quit()

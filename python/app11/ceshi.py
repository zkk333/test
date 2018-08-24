from appium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import app11.is_exist as f1
import os
import subprocess
'''
desired_caps = {
    'automationName': 'Uiautomator2',
    'platformName':'Android',
    'deviceName':'HMKDU17213004645',
    'platformVersion':'7.0',
    'appPackage':'com.taobao.taobao',
    'appActivity':'com.taobao.tao.welcome.Welcome',
}
'''
desired_caps = {
    "automationName": "Uiautomator2",
    "platformName": "Android",
    "platformVersion": "7.0",
    "deviceName":"192.168.21.0",  # 192.168.21.0:5555   HMKDU17213004645
    "udid":"192.168.21.0" ,  # 华为手机
    "noReset": True,
    "appPackage": "com.taobao.taobao",  # com.kk.storefront
    "appActivity": "com.taobao.tao.welcome.Welcome",  # com.kk.storefront.ui.activity.LoginActivity
    # "unicodeKeyboard": True,
    "resetKeyboard": True,
    "newCommandTimeout": "30"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.quit()
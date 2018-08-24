# coding=utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import app11.is_exist as f1
import os
#PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps={
      'automationName':'Uiautomator2',
    "platformName": "Android",
    "platformVersion": "7.0",
    "deviceName": "HMKDU17213004645",
    "udid": "HMKDU17213004645",
    "noReset": True,
    "appPackage": "com.kk.storefront",#com.kk.storefront
    "appActivity": "com.kk.storefront.ui.activity.SplashActivity",#com.kk.storefront.ui.activity.LoginActivity
    #"unicodeKeyboard": True,
    "resetKeyboard": True,
      'newCommandTimeout': 30
  }
#desired_caps['app'] = PATH(r"E:\kkcoach_active_3.5.1_198_20180613-0215_kktest.apk")
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# coding=utf-8
from appium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import app11.is_exist as f1
import os
import subprocess
import sys
def connect(udid):

        desired_caps={
              "automationName":"Uiautomator2",
            "platformName": "Android",
            "platformVersion": "7.0",
            "deviceName":udid ,#192.168.21.0:5555   HMKDU17213004645
            "udid":udid,#华为手机
            "noReset": True,
            "appPackage": "com.kk.storefront",#com.kk.storefront 被测app的包名
            "appActivity": "com.kk.storefront.ui.activity.SplashActivity",#com.kk.storefront.ui.activity.LoginActivity被测app入口activity名称
            #"unicodeKeyboard": True,
            "resetKeyboard": True,#支持中文输入
            "autoAcceptAlerts": True,
              "newCommandTimeout": "30"#没有新命令，30秒退出app
          }
        #subprocess.call('adb devices')
        #print(os.popen('adb connect 192.168.21.0:8888 ').read())
        subprocess.call('adb devices')
        global driver
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return driver
def allow_perssion():
    for i in range(5):
        try:
            message = "//android.widget.Button[contains(@text='允许')]"

            if WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.XPATH, message)) is True:
                driver.find_element_by_xpath(message).click()
        except:
            pass
class SecurityException(Exception):#自定义找不到元素异常
    def __init__(self,erro='权限问题'):
        Exception.__init__(self,erro)
class screen(object):





# 自动截图装饰器
 def __call__(self,func):
    '''截图装饰器'''

    def inner(*args, **kwargs):
        try:
            print('用到了装饰器')
            f = func(*args, **kwargs)

            return f
        except SecurityException:
            self.perssion()

        except:
            print(1)
            self.get_screen()  # 失败后截图
    return inner
 def perssion(self):
     message = "//*[@text='始终允许？']"
     if WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.XPATH, message)) is True:
         driver.find_element_by_xpath(message).click()
 def get_screen(self):
     '''截图'''
     import time
     img_folder = os.path.abspath(sys.path[0] + '/screenshots/')  # 返回path规范化的绝对路径
     isexist = os.path.exists(img_folder)
     if not isexist:
         os.makedirs(img_folder)
     else:
         pass
     nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
     img = img_folder + '/' + '%s.png' % nowTime
     driver.get_screenshot_as_file(img)

def perssion(fun):
    def inner(*args, **kwargs):
        #message = "//android.widget.Button[contains(@text='允许')]"
        message = "//*[@text='允许？']"

        if  WebDriverWait(driver, args).until(lambda driver: driver.find_element(By.XPATH, message)) is True:
             driver.find_element_by_xpath(message).click()
             return fun(*args, **kwargs)



    return inner





        #print(os.popen('adb connect 192.168.21.0').read())
@screen()

def connect_1():

        try:
            driver_1=f1.fengzhuang(driver)
            time.sleep(3)
           # a.get_screen()

            '''appium就应该装最新版 屁事没有'''

            #time.sleep(10)
            #WebDriverWait(driver,15).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[@text='忘记密码？']"))#显示等待，在15秒内查找到元素就执行下一步
            message="//android.widget.TextView[@text='忘记密码？']"
            driver_1.wait(By.XPATH,message)
            driver.find_element_by_xpath(message).click()

            time.sleep(2)
            driver_1.fanhui()
            message="com.kk.storefront:id/et_phone"
            driver_1.wait(By.ID,message)
            name=driver.find_element_by_id(message)
            name.clear()
            name.send_keys('13910211681')
            message='com.kk.storefront:id/et_pwd'
            driver_1.wait(By.ID,message)
            pwd=driver.find_element_by_id(message)
            pwd.clear()
            pwd.send_keys('12345')
            message="//android.widget.Button[@text='登 录']"
            driver_1.wait(By.XPATH,message)


            driver.find_element_by_xpath(message).click()
            #message = "//android.widget.Button[contains(@text='允许')]"
            #driver_1.permission(By.XPATH,message,1)
           # driver_1.wait(By.XPATH,message)






            c=driver_1.exist_toast(message='手机号无效')
            if c==True:
                print('登录失败')

            else:

                #time.sleep(10)
                '''下面那行代码主要是判断app是否登录成功。通过登陆成功页面的某个元素进行判断'''
                message = "//android.widget.Button[contains(@text='允许')]"
                #//*[contains(@text,%s)]
                driver_1.permission(By.XPATH,message,1)
                message1="//android.view.View[@content-desc='本月健康贡献值']"#class+content_desc实现定位
                driver_1.wait(By.XPATH,message1)

                #driver.find_elements_by_xpath("//android.widget.TextView[@content_desc='本月健康贡献值']").text

                driver_1.jindiankankan()
                time.sleep(3)
                driver_1.shezhi()
                message = 'com.kk.storefront:id/TextVersionTv'
                driver_1.wait(By.ID, message)
                banbenhao=driver.find_element_by_id(message).text
                print(banbenhao)
                #time.sleep(1)
                message="//android.widget.TextView[@text='重置密码']"
                driver_1.wait(By.XPATH,message)
                driver.find_element_by_xpath(message).click()#根据class和text属性定位
                time.sleep(1)
                driver_1.fanhui()
                #time.sleep(1)
                message="//android.widget.TextView[@text='退出登录']"
                driver_1.wait(By.XPATH, message)
                driver.find_element_by_xpath(message).click()
                #time.sleep(1)
                message='android:id/button2'
                driver_1.wait(By.ID,message)
                driver.find_element_by_id(message).click()#取消退出
                #time.sleep(1)
                message="//android.widget.TextView[@text='退出登录']"
                driver_1.wait(By.XPATH,message)
                driver.find_element_by_xpath(message).click()
                #time.sleep(1)
                message='android:id/button1'
                driver_1.wait(By.ID,message)
                driver.find_element_by_id(message).click()#确定退出

                driver.quit()
        except Exception as e:
            print(e)
            driver.quit()
if __name__ == '__main__':
    connect('a2ec3c30')
   # allow_perssion()
    connect_1()



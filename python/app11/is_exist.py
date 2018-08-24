from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
class NoSuchElementError(Exception):#自定义找不到元素异常
    def __init__(self,erro='找不到元素'):
        Exception.__init__(self,erro)

class fengzhuang():
    def __init__(self,driver):
        self.driver=driver

        '''当前手机屏幕大小'''
       # self._driver=driver.find_element_by_xpath()
        self.width = driver.get_window_size()['width']#
        self.height = driver.get_window_size()['height']

        #self.message=message
    def exist_toast(self,message):
        try:

            toast_loc = ("//*[contains(@text,%s)]"%message)#contains模糊定位元素  contains(@text,%s)模糊定位一个元素的test   contains(@text,'爱你爱我爱他')  "xpath",
            '''在10秒内每0.1秒去查找一个元素为message的元素，如果没找到那么就报错'''
            WebDriverWait(self.driver, 10, 0.1).until(lambda :self.driver.find_element_by_xpath(toast_loc))#lambda driver:self.driver.find_element_by_xpath(toast_loc)  EC.presence_of_element_located(toast_loc)
            #调用until方法提供的驱动程序作为一个参数，直到返回值不为 False
            return True
        except:
            return False
    def fanhui(self):


        a1 = 67 / 1080
        b1 = 153 / 1812
        # print(width,height)
        x1 = int(a1 * self.width)
        y1 = int(b1 * self.height)
        self.driver.swipe(x1, y1, x1, y1, 1)  # 返回键
        return self
    def jindiankankan(self):
        a1 = 810 / 1080
        b1 = 1758/ 1812
        # print(width,height)
        x1 = int(a1 * self.width)
        y1 = int(b1 * self.height)
        self.driver.swipe(x1, y1, x1, y1, 1)  # 点击进店看看
        return self
    def shezhi(self):
        a = 71 / 1080
        b = 296 / 1812
        x1 = int(a * self.width)
        y1 = int(b * self.height)
        self.driver.swipe(x1, y1, x1, y1, 1)
        return self

    def wait(self,by,message,*args):#在限定的时间里查找元素是否存在，显示等待的好处是，查找到元素时间就停止了

          #try:
           if args:


             WebDriverWait(self.driver, args).until(lambda driver: driver.find_element(by,message)) # 显示等待，在15秒内查找到元素就执行下一步
           else:

             WebDriverWait(self.driver,15).until(lambda driver: driver.find_element(by, message))
        #  except Exception :
             # print('找不到元素%s'%message)





         # return True
       # except NoSuchElementError as e:
          #  print(1)
           # print(e)
            #exit='没有找到元素'
            #print(exit)
            #return None
    def permission(self,by,message,time_out):
        if self.wait(by, message,time_out) is True:  # 判断权限
            self.driver.find_element_by_xpath(message).click()

        else:
            pass




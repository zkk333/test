'''from multiprocessing import Queue
if __name__ == "__main__":
    q = Queue(5)
    q.put("消息1")
    q.put("消息2")
    print(q.full())
    q.put("消息3")
    print(q.full())

    # 从消息队列取数据 推荐两种方法 1 捕获异常   2  判断

    try :
        q.put("消息4",True , 2)   # 尝试写入，如果满了 2秒后抛出异常
    except:
        print("已经满了，现有消息%s条"%q.qsize())
    try :
        q.put_nowait("消息4")   # 尝试写入 如果满了立即抛出异常
        #相当于q.put(item,False)
    except:
        print("已经满了，现有消息%s条"%q.qsize())

    if not q.full():
        q.put_nowait("消息4")

    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait())
            '''
'''
from multiprocessing import Pool
import os, time

def long_time_task(name):
 print ('Run task %s (%s)...' % (name, os.getpid()))
 start = time.time()
 time.sleep(0.1)
 end = time.time()
 print ('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
 print ('Parent process %s.' % os.getpid())
 mainStart = time.time()
 p = Pool(2)
 for i in range(16):
  p.apply_async(long_time_task, args=(i,))
 print ('Waiting for all subprocesses done...')
 p.close()
 p.join()
 print ('All subprocesses done.')
 mainEnd = time.time()
 print('All process ran %0.2f seconds.' % (mainEnd - mainStart))  # 主进程执行时间
 '''
#var_list = ['1,2,2', '3,4,5', '66,77,88']
#a=','
#a=','.join(var_list)
'''
import matplotlib.pyplot as plt

x = [0,0]
y = [0,0,0,1,1,1]

plt.plot(x, y, color="r", linestyle="--", linewidth=1.0)

plt.show()

'''
'''
import re
a=[[1,2,3],[1,2,3]]
a=str(a)
a= re.findall(r'[0-9]',a)
v=[[1,2,0,145],[1,2,]]
v=str(v)
v= re.findall(r'\d+',v)

b=[]
for i in  a:
  b.append(int(i))
print(b)
x=[]
for i in  v:
  x.append(int(i))
print(x)
print(len(x))
'''

import os
import sys
#ABSPATH=None

#if __name__ == '__main__':
ABSPATH=os.path.abspath(sys.argv[0])
ABSPATH=os.path.dirname(ABSPATH)+"/"
#targetpath=os.makedirs('d:/test/')
#os.open('d:/test/xx.txt','w')



#print(ABSPATH)


'''
import 查询数据.select_data as f
import json
data1 = f.data1()
data_ =data1.get('classDataList')
print(data_)
n=len(data_)
print(n)
for i in range(n) :
  #if data_(y)['weightData']==None:
      #pass
 # print(y)
 # else:
  #print(data_[i]['classesId'] )
  #print(b)

 if 'weightData' in data_[i] :
     b=data_[i]['bondDeviceId']
    # weight = data_(i).get('weightData')
     print(b)
 else:


    #

    pass

'''

import  imp

#print (imp.find_module('requests'))
import sys
#print(sys.version_info[0])
import assertpy.assertpy.assertpy as f4
fred = [ {'Bob1':'Bob','Bob1':'Bob','Bob1':'Bob','Bob11':'Bob'},{'Bob1':'Bob','Bob1':'Bob','Bob1':'Bob','Bob11':'Bob1'}]
bob= [ {'Bob1':'Bob','Bob1':'Bob','Bob1':'Bob','Bob11':'Bob'},{'Bob1':'Bob','Bob1':'Bob','Bob1':'Bob','Bob11':'Bob1'}]
people = [bob]

#f4.assert_that(people).extracting('first_name').is_equal_to(['Fred','Bob'])
#f4.assert_that(fred).contains(bob)
#f4.assert_that([{'a':1,'b':2},{'a':3,'b':2}]).is_equal_to([{'a':3,'b':2},{'b':2,'a':1}])
#f4.assert_that(fred ).is_same_as(bob)
lst=('name','name1')
import operator
# 循环:
#a=[(2426859464165376, 345), (1373548392761348, 103), (2408433346807808, 285), (2216980213942272, 142)]
#print(round(4.199999999999999,2))
#print(6*0.7)
a=3.355
b=8.355
#print(round(a,2))
#print(round(b,2))
#print(round(a)==round(b))
'''
list = [1,1,0,2,2,2,4,3,3,4,2,0,0]
new_list = []
i = 0
while True:
    temp = list[i]
    tempj = [temp]
    print(temp )
    print(tempj)
    for j in range(i+1, len(list)):
        if temp == list[j]:
            tempj.append(list[j])
            i += 1
        else:
            i = j
            break
    new_list.append(tempj)
    if i == len(list) - 1:
        break
print(new_list)
'''
# coding=gbk
'''
import time

def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)

    return wrapper

@decorator
def addfunc():
    time.sleep(0.8)
addfunc()
a=(2)
if a:
    print(1)
else:
    print(2)
'''
'''
#coding=utf-8

from selenium import webdriver

import time

browser = webdriver.Firefox()

url= 'https://www.baidu.com'

#通过get方法获取当前URL打印

print( "now access %s"%(url))

browser.get(url)

time.sleep(2)

browser.find_element_by_id("kw").send_keys("selenium")

browser.find_element_by_id("su").click()

time.sleep(3)

print(browser.capabilities['browserVersion'])
'''
import re
import time
import datetime
from datetime import timedelta, datetime
create_time='2018-04-07'
create_time1='2018-04-08'
y1 = datetime.strptime(create_time, '%Y-%m-%d')#把字符串变成日期
y2=datetime.strptime(create_time1, '%Y-%m-%d')
#print(y)
a=str(y1-y2)

a1=int(re.findall(r'\d+',a)[0])#d+主要是在一起的数字放在一起
a1=a1+1
#print(a1)
#print(y -timedelta(days=2))

class A(object):
    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print('A.__private()')

    def public(self):
        print('A.public()')


class B(A):
    def __private(self):
        print('B.__private()')

    def public(self):
        print('B.public()')

if __name__ == '__main__':
    #b = B()
    print(len('ssss'))

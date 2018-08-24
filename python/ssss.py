'''
L = ['Bart', 'Lisa', 'Adam']
i = 0

while i <= len(L)-1:
    print('Hello,%s'%L[i])
    i = i + 1
'''
'''
import os
import sys
img_folder = os.path.abspath(sys.path[0]+ '/screenshots/')#返回path规范化的绝对路径

paths = sys.path
cur_path = paths
print(img_folder,cur_path)
print(os.path.dirname(__file__))
def Tracer(aClass):
    class Wrapper:
        def __init__(self,*args,**kargs):
            self.fetches = 0
            self.wrapped = aClass(*args,**kargs)
        def __getattr__(self,attrname):
            print('Trace:'+attrname)
            self.fetches += 1
            return getattr(self.wrapped,attrname)
    return Wrapper

@Tracer
class Spam:
    def display(self):
        print('Spam!'*8)

@Tracer
class Person:
    def __init__(self,name,hours,rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate
'''
'''
from functools import wraps
from datetime import datetime

#类的装饰器写法，日志
class log(object):
    def __init__(self, logfile='F:\log.txt'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            print('用到了装饰器')
            self.writeLog(*args, **kwargs)    # 先调用 写入日志
            return func(*args, **kwargs)     # 正式调用主要处理函数
        return wrapped_func

   #写入日志
    def writeLog(self, *args, **kwargs):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_str = time+' 操作人:{0[0]} 进行了【{0[1]}】操作'.format(args)
        with open(self.logfile, 'a') as file:
            file.write(log_str + '\n')

@log()
def myfunc(name,age):
    print('姓名：{0},年龄：{1}'.format(name,age))

if __name__ == '__main__':
    myfunc('小白', '查询')
    myfunc('root', '添加人员')
    myfunc('小小', '修改数据')
'''
global i
i=0
class A(object):
    def run(self):
        print('wo ai ni ')
class B(A):
    def cat(self):
        A.run(self)
import json
import time
import log_mokuai as f1
import pymysql
def aa():
    #a=[]
    b=[u"SJ.MAN.JZ.ZC.65-80.3"]
    #a.append(b*3)
    a=b*3
    a=json.dumps(a)
    return a
def ss():
    for i in range(2):
        sum=0

        sum=sum+1
        return sum

def tongji():

    str='hello'
    return str
if __name__ == '__main__':
    '''
    a=eval(aa())
    b=[{'a':"SJ.MAN.JZ.ZC.65-80.3"}]
    print(a)
    x = [i for i in b]
    createTime = 1468830895840
    startTime = 1532142000000
    endTime = '1532144400000'
    msg=time.time()*1000-float(endTime)
    a=f1.log()
    a.info(msg)
    print(time.time()*1000-float(endTime))
    print('这是真的吗')
    print('hhhhhh ')
    print(pymysql.threadsafety)
    print(list('0123456789'*10))'''
    a=set('qyn')
    b=set('syk')
    print(a^b)



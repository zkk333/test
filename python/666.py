#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
import functools

def log(func):
    @functools.wraps(func)#保留原有函数的名称和docstring
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)#*args表示任何多个无名参数，它是一个tuple
#**kwargs表示关键字参数，它是一个dict
    return wrapper

@log
def now():
    print('2015-3-25')

now()
print(now.__name__)

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

today()
print(today.__name__)

#import functools

def log(func):
    @functools.wraps(func) # wrap '__name__'
    def wrapper(*args, **kw):
        print("begin call [%s]" % (func.__name__))
        func_tmp = func(*args, **kw)
        print("end call [%s]" % (func.__name__))
        return func_tmp
    return wrapper

@log # 借助Python的@语法，把decorator置于函数的定义处
def hello(a,b,c):
    print(a,b,c)

hello(1,2,3)

def deco(func):
    def _deco(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _deco

@deco

def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a+b

@deco
def myfunc2(a, b, c):
    print(" myfunc2(%s,%s,%s) called." % (a, b, c))
    return a+b+c

myfunc(1, 2)
myfunc(3, 4)
myfunc2(1, 2, 3)
myfunc2(3, 4, 5)
'''
'''
l = [1,2,3,4]

try:
    print(l[5])
except Exception as e :
          print(e)
      #pass
else:
          print("no error")
#finally:
          #print("finally")
print(111)
try:
  l[2]/0
#except IndexError:
  #print('IndexError')
#except ZeroDivisionError:
  #print('ZeroDivisionError')
except Exception as e:
    print(e)
#else:
  #print ('no error')
print(round(8.33333+0.006,2))
'''
#print(round(0.4597119341563786,2))

#coding=utf-8
'''
import re
import sys
import os

# 正则匹配电话号码
# phone="13893670000"
phone = input('please give a phone number:')
p2 = re.compile('^0\d{2,3}\d{7,8}$|^1[3589]\d{9}$|^14[57]\d{8}$|^199\d{8}')
phonematch = p2.match(phone)

if phonematch:
    print(phonematch.group())
else:
    print("phone number is error!")
'''

# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------
import datetime
#获取366天前的日期
day=(datetime.date.today() - datetime.timedelta(days=366)).strftime('%Y-%m-%d')
print(day)
#获取366天后的日期
day=(datetime.date.today() + datetime.timedelta(days=366)).strftime('%Y-%m-%d')
print(day)
#3周前期
day=(datetime.date.today() + datetime.timedelta(weeks=-3)).strftime('%Y-%m-%d')
print(day)
#-----------------------------------------------------------------------------------

'''获取当前日期前后N天或N月的日期'''

from time import strftime, localtime
from datetime import timedelta, date
import calendar


year = strftime("%Y", localtime())
mon = strftime("%m", localtime())
day = strftime("%d", localtime())
hour = strftime("%H", localtime())
min = strftime("%M", localtime())
sec = strftime("%S", localtime())


def today():
    '''''
    get today,date format="YYYY-MM-DD"
    '''''
    return date.today()

def todaystr():
    '''
    get date string, date format="YYYYMMDD"
    '''
    return year + mon + day

def datetime():
    '''''
    get datetime,format="YYYY-MM-DD HH:MM:SS"
    '''
    return strftime("%Y-%m-%d %H:%M:%S", localtime())

def datetimestr():
    '''''
    get datetime string
    date format="YYYYMMDDHHMMSS"
    '''
    return year + mon + day + hour + min + sec

def get_day_of_day(n=0):
    '''''
    if n>=0,date is larger than today
    if n<0,date is less than today
    date format = "YYYY-MM-DD"
    '''
    if (n < 0):
        n = abs(n)
        print(date.today())
        return date.today() - timedelta(days=n)
    else:
        print(date.today())
        return date.today() + timedelta(days=n)

def get_days_of_month(year, mon):
    '''''
    get days of month
    '''
    return calendar.monthrange(year, mon)[1]

def get_firstday_of_month(year, mon):
    '''''
    get the first day of month
    date format = "YYYY-MM-DD"
    '''
    days = "01"
    if (int(mon) < 10):
        mon = "0" + str(int(mon))
    arr = (year, mon, days)
    return "-".join("%s" % i for i in arr)

def get_lastday_of_month(year, mon):
    '''''
    get the last day of month
    date format = "YYYY-MM-DD"
    '''
    days = calendar.monthrange(year, mon)[1]
    mon = addzero(mon)
    arr = (year, mon, days)
    return "-".join("%s" % i for i in arr)

def get_firstday_month(n=0):
    '''''
    get the first day of month from today
    n is how many months
    '''
    (y, m, d) = getyearandmonth(n)
    d = "01"
    arr = (y, m, d)
    return "-".join("%s" % i for i in arr)

def get_lastday_month(n=0):
    '''''
    get the last day of month from today
    n is how many months
    '''
    return "-".join("%s" % i for i in getyearandmonth(n))

def getyearandmonth(n=0):
    '''''
    get the year,month,days from today
    befor or after n months
    '''
    thisyear = int(year)
    thismon = int(mon)
    totalmon = thismon + n
    if (n >= 0):
        if (totalmon <= 12):
            days = str(get_days_of_month(thisyear, totalmon))
            totalmon = addzero(totalmon)
            return (year, totalmon, days)
        else:
            i = totalmon / 12
            j = totalmon % 12
            if (j == 0):
                i -= 1
                j = 12
            thisyear += i
            days = str(get_days_of_month(thisyear, j))
            j = addzero(j)
            return (str(thisyear), str(j), days)
    else:
        if ((totalmon > 0) and (totalmon < 12)):
            days = str(get_days_of_month(thisyear, totalmon))
            totalmon = addzero(totalmon)
            return (year, totalmon, days)
        else:
            i = totalmon / 12
            j = totalmon % 12
            if (j == 0):
                i -= 1
                j = 12
            thisyear += i
            days = str(get_days_of_month(thisyear, j))
            j = addzero(j)
            return (str(thisyear), str(j), days)

def addzero(n):
    '''''
    add 0 before 0-9
    return 01-09
    '''
    nabs = abs(int(n))
    if (nabs < 10):
        return "0" + str(nabs)
    else:
        return nabs

def get_today_month(n=0):
    '''''
    获取当前日期前后N月的日期
    if n>0, 获取当前日期前N月的日期
    if n<0, 获取当前日期后N月的日期
    date format = "YYYY-MM-DD"
    '''
    (y, m, d) = getyearandmonth(n)
    arr = (y, m, d)
    if (int(day) < int(d)):
        arr = (y, m, day)
    return "-".join("%s" % i for i in arr)


if __name__ == "__main__":

    print (get_day_of_day(14))#获取20天后的日期，2017-12-22
    print (get_day_of_day(-3))#获取3天前的日期，2017-11-29




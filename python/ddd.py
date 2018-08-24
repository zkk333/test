'''
import datetime
import json
now=datetime.datetime.now()
a=str(now+datetime.timedelta(days=1))
print(a[:10])
b = [{'name':'Seal','age':99}]
print(type(b))
y = json.dumps(b)
c=[{"name":"Seal","age":99}]
c= json.dumps(c)

a=[{"name":"Seal","age":99}]
b=['{"name":"Seal","age":99}']
#b = [{'name':'Seal','age':99}]
#print(a==b)
print(y)
print(type(y))
d= {'name':'Seal','age':99}
print(type(d))
y = json.dumps(d)
print(y)
print(type(y))
y=[y]
print(y)
print(type(y))
f1='111'
print(len(f1))
print(type(f1))
f=json.dumps(f1)
print(len(f))'''
import os
import re
import subprocess
from appium import webdriver
#print(os.system('ipconfig')
#print(help(webdriver.Remote))
p=os.popen('ipconfig')
b=p.read()

a=re.findall(r"IPv4 地址(.*?)子网掩码 ",str(b),re.S)#re.S将会匹配换行符
b=str(a)


b=re.sub(r'\D','.',b)
ip=b[29:-7]#电脑ip地址
print(ip)
print(os.popen('adb devices').read())
subprocess.call('adb devices')
print(os.popen('adb connect 192.168.21.0:8888 ').read())
subprocess.call('adb devices')

for i in range(3):
    print(i)

#a1=re.findall(r'\d+', a)
#print(a1)
#print(len(a1))
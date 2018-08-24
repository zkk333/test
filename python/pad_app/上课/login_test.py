import pad_app.上课.login as f1
import os
import sys
import requests

# -*- coding: utf-8 -*-
#import log_mokuai
import logging
import log_mokuai
#def login_test(uname,pwd):
a=log_mokuai.log()


#json={'uname':'15600905550',
#          'pwd':'1234567'}
#headers=p.log(uname,pwd)
#print(headers)
#login_log=p.res_session.post(url='http://test.kuaikuaikeji.com/kcas/PadCoachLoginV2',headers=headers)
   #print(p.log(uname,pwd))
   #print(p.log(uname,pwd))
  # return  p.log(uname,pwd)
   #return (login_log.status_code)

def login_test1():
    '''uname =input('输入用户名:')
    pwd =input('输入密码:')'''
    #input('正确的用户名和密码：')
    print('用户名密码正确：')
    uname='15600905550'
    pwd='123456'
    res_session = requests.session()
    if  f1.log(uname,pwd,res_session).status_code==200:
        #print(log_mokuai)
        #cc='握手神'
        b='握手神'
        a.info(b)
        a.info(f1.log(uname,pwd,res_session).json())
        #print(a.json())
        print ('success')
    else:
        print ('status_code=%s'%(a))
    print('用户名正确，密码错误：')
    uname = '15600905550'
    pwd = '123456'
    res_session = requests.session()
    if f1.log(uname,pwd,res_session).status_code == 200:
        a.info(u'握手神')
        a.info(f1.log(uname, pwd, res_session).json())
        print('success')
    else:
        print('status_code=%s' % (f1.log(uname,pwd,res_session).status_code))
    print('用户名错误，密码错误：')
    uname='156009055501'
    pwd='1234567'
    res_session = requests.session()
    if f1.log(uname,pwd,res_session).status_code== 200:
        print('success')
    else:
        print('status_code=%s' % (f1.log(uname,pwd,res_session).status_code))
    print('用户名为空，密码正确：')
    uname = ''
    pwd = '123456'
    res_session = requests.session()
    if f1.log(uname, pwd,res_session).status_code == 200:
        print('success')
    else:
        print('status_code=%s' % (f1.log(uname,pwd,res_session).status_code))
    print('用户名正确，密码为空：')
    uname = '15600905550'
    pwd = ''
    res_session = requests.session()
    if f1.log(uname, pwd,res_session).status_code == 200:
        print('success')
    else:
        print('status_code=%s' % (f1.log(uname,pwd,res_session).status_code))

    #return p.log(uname, pwd)

if __name__ == '__main__':
    login_test1()








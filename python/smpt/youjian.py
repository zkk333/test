#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import assertpy.assertpy.assertpy as f4
import 智运.student.yuqiresult as f5
import requests
def erro_sendemail(error):
# 第三方 SMTP 服务
  mail_host="smtp.qq.com"  #设置服务器
  mail_user="2375101894"    #用户名
  mail_pass="hkcsaacgppblebcg"   #口令，qq邮箱登录码


  sender = '2375101894@qq.com'#发件人邮箱
  receivers = '1457348388@qq.com' # 接收人邮件，可设置为你的QQ邮箱或者其他邮箱
  #error='1234'
  message = MIMEText(error, 'plain', 'utf-8')
  message['From'] = Header("接口测试官方", 'utf-8')
  message['To'] =  Header("收件人", 'utf-8')

  subject = '接口测试的结果'
  message['Subject'] = Header(subject, 'utf-8')
#print(1)

  try:
    smtpObj = smtplib.SMTP_SSL(mail_host,465)#设置端口号为465
    #smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    #print(1)
    #smtpObj.set_debuglevel(1)#打印出和SMTP服务器交互的所有信息
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())#as_string()把MIMEText对象变成str
    print ("邮件发送成功")
  except smtplib.SMTPException:
    print ("Error: 邮件发送失败")
def is_email(ss,url,case1):
  try:

    f4.assert_that(ss.status_code).is_equal_to(200)
    a=ss.elapsed.total_seconds()#接口响应时间
    #print(a)
    #print(url)
  except AssertionError:
    error1 = url
    case=case1
    error2 = ss.status_code
    error3 = '出错的接口以及报错的状态码,测试用例'
    erro = error3 + ':' + str(error1) + ',' + str(error2)+str(case)
    #erro_sendemail(erro)
def is_email_coach_list(ss,url,role,gym_id):
  try:
    #print(ss.json()['coachList'])
    #print(f5.caoach_shiji(gym_id, role))
    f4.assert_that(ss.json()['coachList']).is_equal_to(f5.caoach_shiji(gym_id, role))
  except AssertionError:

    error1 = url
    error2 = ss.json()['coachList']
    error3 = '出错的接口以及响应的内容'
    erro = error3 + ':' + str(error1) + ',' + str(error2)
   # print(erro)
    erro_sendemail(erro)

def  is_zhengque(s1,s2,daqu):
  try:

      f4.assert_that(s1).is_equal_to(s2)


  except AssertionError:

    error1 = daqu
    error2 =s1
    error3 = s2
    erro =('计算后的值：',s1)  +('接口中的值：',s2) + ('出错的地域',daqu)
    print(erro)
    #erro_sendemail(erro)
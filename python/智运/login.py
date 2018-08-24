import requests

import sys
import json
import base64
import hashlib

import pad_app.主要接口.interface as f1
#import loginpage
'''authorazation认证主要流程：从服务器获取WWW-Authenticate这个值auth
计算digest认证response的值：1、先对密码进行MD5加密并且base64编码
2、把获取的auth值加上用户名和经过base64编码后的密码黏贴在一起
3、把2中的黏贴后的值先md5加密然后base64编码即response的值
4：encode和decode的用法不太看懂，代码中的都是报错后加的
md5编码只能是byte类型
'''
#global  res_session
def log(username,password,res_session):#主要是返回headers头文件
    # global  login_log
     #client1 = 'app'
     #global  res_session

     #global username,password
     # base64string=base64.encodebytes()
     #res_session = requests.session()#保证请求与响应在同一个会话下，因为http协议是无序的
     #super().__getattribute__(res_session)

     #json=res_session.urllib.parse.urlencode(json).encode('utf-8')
     headers = {'user_Agent': 'KKCoach/Android',
           'connection': 'Keep-Alive',
           'Accept-Encoding': 'gzip',
           'Host': 'test.kuaikuaikeji.com',
           'Cache-Control': 'no-cache',
           }
     res =res_session.post( url=f1.kk_zhiyun_url3+f1.智运登录接口,headers=headers)
    # print(res)
     #g_cookies=res.headers.get('Set-Cookie','').JSESSIONID
     #g_cookies="g_cookie=\""+JSESSIONID+"\" "

     #headers={'Cookie',g_cookies}
     #print(cookies)
    # auth = res.headers.get('WWW-Authenticate','')#authorization验证服务器返回的随机字符串

     #auth='2ab45f08-5733-4540-bd8b-36f02fb38a52'
     #if authorization and authorization[:6] == 'Basic ':
     #print(username,password)
     m=hashlib.md5()#创建md5对象
     m1=hashlib.md5()
     #m2=hashlib.md5()
     #password='123456'
     #username='15600905550'
     '''strs1=(username+password).encode('utf-8')

     m.update(strs1)#生成加密串
     ha=m.hexdigest()#获取加密串
     #print(ha)'''
     m.update(password.encode('utf-8'))
     pd = m.hexdigest()



     author="client=app,user="+username+",response="+pd+""
     #print(author)
     headers={'user_Agent':'KKCoach/Android',
         'connection': 'Keep-Alive',
         'Accept-Encoding': 'gzip',
         'Host': 'test.kuaikuaikeji.com',
         'Cache-Control': 'no-cache',
         'authorization': author,

        }

     login_log = res_session.post(url=f1.kk_zhiyun_url3+f1.智运登录接口, headers=headers)
     #coachId =login_log.json()['coachId']

    # return login_log
     return login_log

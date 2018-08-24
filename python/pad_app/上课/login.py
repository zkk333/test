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
     global  login_log
     #global  res_session
     url="http://test.kuaikuaikeji.com/kcas/PadCoachLoginV2"
     #global username,password
     # base64string=base64.encodebytes()
     #res_session = requests.session()#保证请求与响应在同一个会话下，因为http协议是无序的
     #super().__getattribute__(res_session)

     #json=res_session.urllib.parse.urlencode(json).encode('utf-8')
     headers = {'user_Agent': 'KKTabletUDP/Android',
           'connection': 'Keep - Alive',
           'Accept - Encoding': 'gzip',
           'Host': 'test.kuaikuaikeji.com',
           'Cache - Control': 'no-cache',
           }
     res =res_session.post( url=f1.kkweight_app_url2+f1.快快教瘦登录,headers=headers)
     #g_cookies=res.headers.get('Set-Cookie','').JSESSIONID
     #g_cookies="g_cookie=\""+JSESSIONID+"\" "

     #headers={'Cookie',g_cookies}
     #print(cookies)
     auth = res.headers.get('WWW-Authenticate','')#authorization验证服务器返回的随机字符串

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

     password1 = base64.encodebytes(pd.encode('utf-8'))[:-1]#base64编码
     password1=password1.decode('utf-8')
     #password2=password1.decode('utf-8')
    # print(password1)
     '''username1=username.encode('utf-8')#string类型转换成byte类型
      up=(username1+password1).encode('utf-8')
      print(up)#也可以用'''
     up=(username+password1)
     strs2=(auth+up).encode('utf-8')
     #print(strs2)




     m1.update(strs2)#生成加密串
     resp=m1.hexdigest()#获取加密串`
     #print(resp)
     #strs=password.encode('utf-8')
     #m2.update(strs)#生成加密串
     #psw=m2.hexdigest()#获取加密串
     response=base64.encodebytes(resp.encode('utf-8'))[:-1]

     response=response.decode('utf-8')#byte类型转换成string类型
     #print(response)
#str(base64string1)
#print(base64string1)
     author="user=\""+username+"\",response=\""+response+"\""
     #print(author)
     headers={'user_Agent':'KKTabletUDP/Android',
         'connection': 'Keep - Alive',
         'Accept - Encoding': 'gzip',
         'Host': 'test.kuaikuaikeji.com',
         'Cache - Control': 'no-cache',
         'authorization': author,

        }
     #print(headers)
#print(author)
#res.add_header('authorization',author)
#res.add_header('user_Agent','KKTabletUDP/Android')
#res.add_header('connection','Keep - Alive')
#res.add_header('Accept - Encoding','gzip')
#res.add_header('Host','test.kuaikuaikeji.com')
#res.add_header('Cache - Control','no-cache')

#m_cookie=res.get_header('cookie')
#res.add_header('cookie',m_cookie)
#print(res.headers)
     #res_session.post(url='http://test.kuaikuaikeji.com/kcas/PadLogV2',data=json,headers=headers)
     #s=res_session.get(url='http://test.kuaikuaikeji.com/kcas/PadLogV2',headers=headers)
     login_log = res_session.post(url=f1.kkweight_app_url2+f1.快快教瘦登录, headers=headers)
     #coachId =login_log.json()['coachId']


     return   login_log






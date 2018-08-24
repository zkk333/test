import requests

import pad_app.主要接口.interface as ff
import json
import base64
import hashlib
#import loginpage
import uuid
import time
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
     #url="http://test.kuaikuaikeji.com/kcas/PadCoachLoginV2"
     #global username,password
     # base64string=base64.encodebytes()
     #res_session = requests.session()#保证请求与响应在同一个会话下，因为http协议是无序的
     #super().__getattribute__(res_session)

     #json=res_session.urllib.parse.urlencode(json).encode('utf-8')
     headers = {#'User-Agent': 'KKUSER-3.7.4-test-19302/Android/4.4.4/vivo/vivo X5F',
           'connection': 'Keep - Alive',
           'Accept - Encoding': 'gzip',
          # 'Host': 'test.kuaikuaikeji.com',
           'Cache - Control': 'no-cache',
           }
     res =res_session.post( url=ff.kkuser_app_url1+ff.快快减肥登录,headers=headers)
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
     #print(password2)
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
     headers1={#'User-Agent': 'KKUSER-3.7.4-test-19302/Android/4.4.4/vivo/vivo X5F',
         'connection': 'Keep - Alive',
         'Accept - Encoding': 'gzip',
         'Host': 'test.kuaikuaikeji.com',
         'Cache - Control': 'no-cache',
         'authorization': author,

        }
     return headers1

def uuid_make():#生辰二维码相关信息
    uuid_make=str(uuid.uuid1())#str类型
    return uuid_make
def imitate_weight(res_session,uuid_make):#可有可无，操作是自助称重手机获取二维码的操作
    data = {'uuid': uuid_make}
    weight_code = res_session.post(ff.kkweight_app_url2+ff.获取用户称重信息, json=data)
    print('模拟自助称重的流程用的，报的就是404：')
    print(weight_code.status_code)
def log_succes(headers,uuid_make,res_session):


    # print(headers)
    login_log = res_session.post(url=ff.kkuser_app_url1+ff.快快减肥登录, headers=headers)#登录
    print('登录是否成功：')
    if login_log.status_code==200:
      print('登录成功')
    else:
        print('登录失败')

    url = 'http://test.kuaikuaikeji.com/kas/uploadweightuuid?uuid=' + uuid_make
    #print(url)
    sweep_code1_s = res_session.get(url=url, headers=headers)#get请求，不能用post请求，数据是在url中的，post请求是错误的#快快减肥app扫码操作时的接口
    print('快快减肥端扫码成功的文案：')
    print(sweep_code1_s.json().get('reason'))
def weight(headers,res_session,uuid_make):
    data={'uuid':uuid_make}
    getdata1 = requests.post(url=ff.kkweight_app_url2+ff.获取用户称重信息, json=data,
                             headers=headers
                             )  # 扫码完成后自助称重手机获取用户信息


    useruuid = getdata1.json().get('userUuid')

# print(getdata1)
    data = {
    "initWeightData": {
        "dataSourceType": 1,
        "entrailsFat": 5,  # 内脏脂肪
        "fatRate": 18,  # 脂肪率
        "macAddress": "F9:15:01:D8:AD:5A",
        "musleRate": 68.5,  # 肌肉率
        "resistance": 463.29998779296875,  # 电阻
        "skeletonRate": 4.6,  # 骨骼率
        "userBmr": 1547,  # 用户bmr
        "waterRate": 51.1,  # 水分率
        "weight": 64.2  # 体重
    },
    "userUuid": "492a685f-16a4-40c0-a0a3-17dec392c9bd"

}
    data['userUuid'] = useruuid
    #time1 =time.time()

    #time2 = time.time()

    #timeout=time2-time1
    #print(timeout)
    checkdata1 = requests.post(url=ff.kkweight_app_url2+ff.三次校验接口, json=data,
                           headers=headers)  # 三次校验
    time2 = time.time()
    #$timeout = time2-time1
    #print(timeout)
    if checkdata1.status_code==200:
       print('经过3次校验')

       data2 = checkdata1.json().get('corrWeightData')
       userUuid = checkdata1.json().get('userUuid')
       memo = checkdata1.json()['modifiedMemo']
       print(memo)
       data2['userUuid'] = userUuid
       data2['modifiedMemo'] = memo
       data2['dataSourceType'] = 3

# print(data2)
       updata1 = res_session.post(url=ff.kkweight_app_url2+ff.上传称重数据,
                           json=data2)  # 上传数据
       print('称重完成上传数据：')
       if updata1.status_code==200:
         print('上传成功')
       else:
         print('未插到数据库')
    else:
       print('没有校验')


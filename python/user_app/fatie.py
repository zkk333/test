import user_app.user_app_login as f1
import pad_app.主要接口.interface as f2
# pad_app.上课.login import log
import urllib3
import time
#from requests_toolbelt.multipart.encoder import MultipartEncoder
import urllib
import requests
import json
#mport requests
# 禁用安全请求警告
from urllib import parse
urllib3.disable_warnings()
_create_time2 = time.localtime(time.time())
create_time2 = time.strftime("%Y-%m-%d %H:%M:%S", _create_time2)
create_time21=str(create_time2)[:10]
create_time22=str(create_time2)[11:]
create_time4=create_time21.replace('-','')
create_time3=create_time22.replace(':','')
create_time=str(create_time4+create_time3)


username='17600958351'
password='123456'
resssion=requests.session()
a=f1.log(username,password,resssion).status_code
headers = {'Cache-Control': 'no-cache',
            'User-Agent': 'KKUSER-4.4.1-test-19727/Android/4.4.4/vivo/vivo X5F',
            'Content-Type': 'application/x-www-form-urlencoded',
          #  'Content-Length': 84,
             'Host':'ts.kuaikuaikeji.com',#
             'Connection': 'Keep-Alive',
             'Accept-Encoding': 'gzip'
      }
r=resssion.get(url=f2.kk_user_app_url3+f2.发现, headers=headers)
#print(r.json())
r=resssion.get(url=f2.kk_user_app_url3+f2.选择照片, headers=headers)
#print(r.json())
'''{'Content-Disposition': 'form-data;name="pic2";filename="_temp0152818701726_temp.jpg"',
'Content-Transfer-Encoding': 'binary',
'Content-Type':'application/octet-stream',
'Content-Length': '221680'}'''
headers={'Cache-Control': 'no-cache',
'User-Agent': 'KKUSER-4.4.2-test-19729/Android/4.4.4/vivo/vivo X5F',
#'Content-Type': 'multipart/form-data; boundary=f7288aad-6a93-4f31-8b53-35a038856dbe',#b41d20a5-eac0-4e32-a828-17a3d8949468
'Content-Length': '162814',
'Host': 'ts.kuaikuaikeji.com',
'Connection': 'Keep-Alive'
}

params={
       'pic1':open('D://IMG_20170228_210626.jpg','rb'),#Content-Disposition: form-data; name="pic1"; filename="IMG_20170228_21062_temp.jpg"
       'pic2':open('D://IMG_20170228_210626.jpg','rb'),
       'pic3':open('D://IMG_1310.PNG','rb'),
      # 'pic4':open('D://IMG_20170228_210626.jpg','rb')



}

r=resssion.post(url=f2.kk_user_app_url3+f2.发布消息,files=params,headers=headers)
picture_1=r.json()['pics']
data=[]
for picture_11 in picture_1:
    #print()
    thumbnail_pic=picture_11['thumbnail_pic']
    original_pic=picture_11['original_pic']
    bmiddle_pic=picture_11['bmiddle_pic']
    data1={'bmiddle_pic':bmiddle_pic,
      'original_pic':original_pic,
      'thumbnail_pic':thumbnail_pic}
    data.append(data1)
'''
data=json.dumps(data)
data=[data]
print(data)打印出的data值：字典外面，中括号里面有单引号  #字典先转成str类型，最后转成了list类型

'''
#data=[data]
data=json.dumps(data)    #    打印出的data值：字典外面，中括号里面没有单引号 字典先转列表，再转成str类型

#print(data)
#data.strip('')





params={ 'check_time':(None,create_time,'text/plain'),
       'media_type':(None,'1','text/plain'),
        'pics':(None,data,'text/plain'),
       }
headers={'User-Agent': 'KKUSER-4.4.2-test-19729/Android/4.4.4/vivo/vivo X5F',
'Content-Length': '1036',
'Host': 'ts.kuaikuaikeji.com',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip'

}
r=resssion.post(url=f2.kk_user_app_url3+f2.发布成功,files=params,headers=headers)
if r.status_code==200:
    print('success')
else:
    print(r.status_code)
headers={'User-Agent': 'KKUSER-4.4.2-test-19729/Android/4.4.4/vivo/vivo X5F',

'Host': 'ts.kuaikuaikeji.com',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip'

}
r=resssion.get(url=f2.kk_user_app_url3+f2.发帖成功后,headers=headers)    #头文件对是响应是否报错是有影响的
if r.status_code==200:
    print('success')
else:
    print(r.status_code)
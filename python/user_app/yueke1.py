import user_app.user_app_login as f1
import pad_app.主要接口.interface as f2
# pad_app.上课.login import log
import urllib3
import urllib
import requests
import datetime
import 查询数据.select_data as f3
#mport requests
# 禁用安全请求警告
from urllib import parse
urllib3.disable_warnings()
username='17600958351'
password='123456'
resssion=requests.session()
a=f1.log(username,password,resssion).status_code
user_uuid=f1.log(username,password,resssion).json()['uuid']

headers = {'Cache-Control': 'no-cache',
            'User-Agent': 'KKUSER-4.4.1-test-19727/Android/4.4.4/vivo/vivo X5F',
            'Content-Type': 'application/x-www-form-urlencoded',
          #  'Content-Length': 84,
             'Host':'ts.kuaikuaikeji.com',#
             'Connection': 'Keep-Alive',
             'Accept-Encoding': 'gzip'
      }
#data1=('city={name}&subject_show_id={id}&lat=39.90598&lon=116.640735&subject_code='.format(name=parse.quote(city),id=id))
#data1=('city=%E5%8C%97%E4%BA%AC&subject_show_id=12&lat=39.90598&lon=116.640735&subject_code=')

r=resssion.get(url=f2.kk_user_app_url3+f2.我的课程, headers=headers)
#print(r.json())

while 1:
 try:
     description = str(input('请输入课程类型.女子防暴搏击课,极效塑形FIGHTING,塑形防暴搏击课,SHOW腰课,SHOW腹课,SHOW腿课'))
     user_subject=str(f3.user_subject(description,user_uuid))
     subject_show_id=str(f3.course_type(description))
     #print(user_subject)
     r = resssion.get(url=f2.kk_user_app_url3 + f2.预约课程1(user_subject), headers=headers)
   #  print(r.json())
     r = resssion.get(url=f2.kk_user_app_url3 + f2.城市列表1(subject_show_id), headers=headers)
    # print(r.json())
     city=r.json()['cityList']
     city=str(input('请输入买课的城市{city}'.format(city=city)))
     r = resssion.get(url=f2.kk_user_app_url3 + f2.门店列表1(city=parse.quote(city),subject_show_id=subject_show_id), headers=headers)
     #print(r.json())
     gymlist=r.json()['gymList']
     gym_id=[gym1['name'] for gym1 in gymlist]
     gym_id = str(input('请输入买课的门店{gym}'.format(gym=gym_id)))
     id=f3.gym_id(gym_id)
    # print(id)

     r = resssion.get(url=f2.kk_user_app_url3 + f2.门店课程详细1(subject_show_id,id), headers=headers)
     #print(r.json())
     classVoMap = r.json()['classVoMap']
     day_time = [classVoMap1 for classVoMap1 in classVoMap]
     #print(day_time)

     # print(classVoMap[a])

     # print(b[0])

     # print(classVoMap)
     while 1:
         try:
             a = str(input('请输入需要选的日期{day_time},从这几个里面选:'.format(day_time=day_time)))
             b = [classvo['class_id'] for classvo in classVoMap[a]]
             n = 0
             while 1:
                 r = resssion.get(url=f2.kk_user_app_url3 + f2.预约课程信息1(b[n],user_subject), headers=headers)
                 # print(r.json()['text'])
                 if '名额已满' in r.json()['text']:
                     n = n + 1
                     classes_id = b[n]
                     # print(classes_id)
                     # exit()



                 else:
                     data1 = ('classes_id={classes_id}&user_subject_uuid={user_subject}'.format(
                         classes_id=b[n],user_subject=user_subject))
                     r = resssion.post(url=f2.kk_user_app_url3 + f2.预约成功, data=data1, headers=headers)
                     r = resssion.get(url=f2.kk_user_app_url3 + f2.预约成功详情1(b[n],user_subject), headers=headers)
                     if '预约成功' in r.json()['success_msg']:
                         print('success')
                     else:
                         print('pass')
                     # print(r.json())
                     # print(b[n])

                     exit()
         except IndexError:
             # now = datetime.datetime.now()
             # a = str(now + datetime.timedelta(days=1))
             # a=a[:10]
             print('当天没有可预约课，请换一天')
         except  KeyError:
             print('该日期无效')


 except IndexError:
     print('该学员没有购买该课程')



import 查询数据.select_data_1 as f2

from pad_app.上课.login import log
import requests
import pad_app.上课.upload_data as ff
import json
import copy
import time
from imp import  reload
import pad_app.上课.function  as fff
import pad_app.上课.add_user_class as ff2
#import weight_weighing.weight as ffff
import pad_app.weight_weighing.weight as ff1
import pad_app.主要接口.interface as f1
import requests
from aiohttp import ClientSession
import asyncio

#reload(ff2)
#def report_test():
#print(a)

   #data= f.data1()
   #print(data)
def report_test(data1):
     #print(data1)

     uname='17600958351'
     pwd='123456'
     res_session = requests.session()
     tme1=time.time()
     tme2=time.time()*1000  #毫秒级时间戳
     if log(uname,pwd,res_session).status_code==200:
       data_ =data1.get('classDataList')
       coachId = log(uname, pwd, res_session).json()['coachId']


       for y in data_:
           y=y

       coursecode = y.get('courseCode')
       classesid=y.get('classesId')

      # subjectid = y.get('subjectId')
       #print(data)
       n = int(len(data_))


       print( coursecode)

       if 'SJ' not in coursecode:


           classes_id=ff2.add_class1(coachId,classesid,coursecode,n) #加的课的id，不可缺少
           print('classid')
           print(classes_id)

           a=fff.A(2)
           gym_id = a.get_gymid(coachId)
           subjectid =a.get_subjectId(gym_id)



           #classesId =  y.get('classesId')  # 好简单 ，昨天试了半天。目前感觉还不是很好
        #startTime =  y.get('startTime')  # 毫秒级时间戳
        #endTime =  y.get('endTime')

        #print(tme1)




           data= {'coachId': coachId,
                   'listRange': 0,
                   'listSort': 0,
                   'pageIndex': 0,
                   'pageSize': 100}
           headers = {'user_Agent': 'KKTabletUDP/Android',
                   'connection': 'Keep - Alive',
                   'Accept - Encoding': 'gzip',
                   'Host': 'test.kuaikuaikeji.com',
                   'Cache - Control': 'no-cache'
                   }
           r= res_session.post(url=f1.kkweight_app_url2 + f1.获取课程列表信息, json=data, headers=headers)
           data1 = {
               'classesId': classes_id,
           }
           st= res_session.post(url=f1.kkweight_app_url2 + f1.开始课程, json=data1, headers=headers)
           #coursecode=st.json()
           data2 = {
                   'coachId ': coachId,
                    'classesId': classes_id,
                     'courseCode': coursecode

                    }
           cek1= res_session.post(url=f1.kkweight_app_url2 + f1.获取课程详细信息, json=data2, headers=headers)


           cek2 = res_session.post(url=f1.kkweight_app_url2 + f1.查看签到状态, json=data2, headers=headers)
           numbers = cek2.json().get('userCheckinMap')
           t = []
           i1 = len(numbers)
           #classes_id=(classes_id)
           for y in numbers:
               # b=numbers[y]

               t.append(y)  # 把人数换成列表格式
           # print(t[0])
           #data1 = f2.data1()
           #data1 = data1.get('classDataList')
           start_time1= (time.time())*1000
           #print(start_time1)
           #start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_time1)
             # print(start_time)
           end_time1 = (time.time()+3600)*1000
           #print(end_time1 )
           #end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_time1)
           #print(len(data1))
           classDataList = []

           #print(1)
           #print(n)
           for i in range(n):
                   # print(data_)
                   # classesId = '218527'
              #weight=data_[i]['weightData']
              #print(weight)
              #print(i)
              if 'weightData' in data_[i]:
                  data_[i]['weightData'] = data_[i]['weightData']
                  data_[i]['baseData']=data_[i]['baseData']

              else:
                  pass

              data_[i]['endTime'] = end_time1
              data_[i]['startTime'] = start_time1
                   #data1[i]['subjectId'] = subjectid
              data_[i]['userUuid'] = t[i]
              data_[i]['classesId']=classes_id
              data_[i]['subjectId']=subjectid

                   #data1[i]['courseCode'] = coursecode
              classDataList.append(data_[i])
                   #print(3)

                   # print(classDataList)


                   # cek3 = res_session.post(url='http://test.kuaikuaikeji.com/kcas/PadGetCoachClassInfoV2', json=data,headers=headers)  # 刷新后的页面，获取课程详情
           #print(2)
           data3 = {'classDataList': classDataList,
                        "uploadType": 1,
                    'uploadVersion': 3
                        }
           #print(coursecode )

           report1 = res_session.post(url=f1.kkweight_app_url2 + f1.上传报告, json=data3, headers=headers)
               # print(report1.json())
               # print(report1.status_code)
               #print(classesId)

           aa = fff.D()
           number = aa.number()
           #tmeout = (report1.elapsed.microseconds)/number#发送请求到服务器端响应的时间大于1秒，只会截取后面的小数部分
           tmeout1=report1.elapsed.total_seconds()#这个才是正确的 获取响应时间，发送请求到收到相应的时间差
           #report1.elapsed.
           print('上传报告所需时间', tmeout1)
           #print('上传报告所需时间', tmeout)
           if report1.status_code == 200:
               data4 = {'classesId': classes_id,
                        'subjectId': subjectid}
               getreport1 = res_session.post(url=f1.kkweight_app_url2 + f1.报告列表, json=data4, headers=headers)
           # print(getreport1.json())
               classReportList = getreport1.json().get('classReportList')
               for x in range(len(classReportList)):
                 cl = classReportList[x]
                 reurl = cl.get('reportUrl')
                 print(reurl)


                 #if getreport1.status_code!=200:
                       #print(classes_id)
                       #exit()

                   #else:
                     #  print('success')
                   #classReportList = getreport1.json().get('classReportList')
                 print(classes_id)

           else:
                   print('上传失败 ',report1.status_code )


       else:
           pass



     else:
        print('用户名或密码错误')

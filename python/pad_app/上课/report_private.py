import 查询数据.select_data as f

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
#data=f.data1().get('classDataList')
#print(a)
uname='18610728165'
pwd='123456'
res_session = requests.session()
tme1=time.time()
tme2=time.time()*1000  #毫秒级时间戳
#print(tme1)


if log(uname,pwd,res_session).status_code==200:

#print(p.log(uname,pwd).json()['coachId'])
   coachId = log(uname, pwd, res_session).json()['coachId']
   classdatalist=[]

# print(coachId)
   data = {'coachId': coachId,
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
   r = res_session.post(url=f1.kkweight_app_url2+f1.获取课程列表信息, json=data, headers=headers)
   #p = r.json()

   q = r.json()['classInfoList']
   if q :

     i=len(q)
     print(i)
     k=0
     while k <=i-1 :
      try:
         k = input('请输入课程节数:')#从0开始算
         k = int(k)
         a=q[k]
         #b = q[k].get('userList')
         #for j in range(len(b)):
             #usd = b[j]
             #user_uuid = usd.get('uuid')
             # print('userUuid=', user_uuid)
             # print(b)
             # user_uuid=a.get('uuid')
         coursecode = a.get('courseCode')
         classesId = a.get('classesId')  # 好简单 ，昨天试了半天。目前感觉还不是很好
         startTime = a.get('startTime')#毫秒级时间戳
         endTime = a.get('endTime')
         subjectId = a.get('subjectId')

             # print('classesId=', classesId)
             # print('classesId :', classesId,'coursecode:', coursecode)

                 # print(cek3.status_code)

                 #print(user_uuid)
         #print(startTime)



                 # print(classdatalist)
         if startTime<=tme2:
           data1 = {
                   'classesId': classesId,
                  }
           st = res_session.post(url=f1.kkweight_app_url2+f1.开始课程, json=data1,headers=headers)  # 开始课程接口
           rt=st.json().get('result')
           if rt==0:

# print(st.status_code)

              if st.status_code == 200:
                 data2 = {#'coachId ': coachId,
                    'classesId': classesId,
                  # 'courseCode': coursecode
                    }
    # cek1,cek2,cek3 三者基本是同步的，点击开始课程后的数据
                # cek1 = res_session.post(url=f1.kkweight_app_url2+f1.获取课程详细信息, json=data2, headers=headers)  # check这个字段不能用，之前报错，获取课程信息
    # print(cek1.json())
    # if cek.status_code==200:

                 cek2 = res_session.post(url=f1.kkweight_app_url2+f1.查看签到状态, json=data2,headers=headers)  # 查看是否签到
                 numbers=cek2.json().get('userCheckinMap')#字典格式
                 #print(numbers)
                 #y1 = numbers.keys(0)
                 #print(y1)
                 t = []
                 i1 = int(len(numbers))
                 for y in numbers:  #可以读取到键值也就是学员uuid
                     # b=numbers[y]

                     t.append(y)  # 把人数换成列表格式
                 # print(t[0])
                 data1 = f.data1()
                 data1 = data1.get('classDataList')
                 #print(len(data1))
                 classDataList = []
                 if i1 <= len(data1):
                     for i in range(i1):
                         # print(data_)
                         #classesId = '218527'

                         if 'weightData' in data1[i]:
                                 data1[i]['weightData'] = data1[i]['weightData']
                                 data1[i]['baseData'] = data1[i]['baseData']

                         else:
                                 pass
                         data1[i]['classesId'] =classesId
                         data1[i]['endTime'] =endTime
                         data1[i]['startTime'] =startTime
                         data1[i]['subjectId'] =subjectId
                         data1[i]['userUuid'] = t[i]
                         data1[i]['courseCode'] =coursecode
                         classDataList.append(data1[i])
                         #print(classDataList)


                  # cek3 = res_session.post(url='http://test.kuaikuaikeji.com/kcas/PadGetCoachClassInfoV2', json=data,headers=headers)  # 刷新后的页面，获取课程详情
                     data3 = {'classDataList': classDataList,
                           "uploadType": 1,
                           "uploadVersion": 3
                           }
                    #print(data3)
                     tme3=time.time()

                     ff1.weight_get(subjectId,classesId)#称重
                    #b3 = ffff.weight_get()

                     report1 = res_session.post(url=f1.kkweight_app_url2+f1.上传报告,json=data3, headers=headers)
                    #print(report1.json())
                    #print(report1.status_code)
                     print(classesId)
                     tme4=time.time()
                     tmeout=tme4-tme3
                     print('上传报告所需时间',tmeout)
                     if report1.status_code == 200:
                       data4 = {'classesId': classesId,
                            'subjectId': 0}
                       getreport1 = res_session.post(url=f1.kkweight_app_url2+f1.报告列表,json=data4, headers=headers)
                       #print(getreport1.json())
                       classReportList = getreport1.json().get('classReportList')
                       for x in range(len(classReportList)):
                         cl = classReportList[x]
                         reurl = cl.get('reportUrl')
                         print(reurl)
                       nn = int(input('删除课程请输入1:'))
                       b1=fff.B()
                       b1.deleteclass1(nn)

                     else:
                       print('报告上传失败')
                 else:
                   print('请确保上课人数与现网报告人数的一致性')




           else:
              print('该节课已上传报告，报告为：')
              data4 = {'classesId': classesId,
                        'subjectId': subjectId}
              getreport1 = res_session.post(url=f1.kkweight_app_url2+f1.报告列表,json=data4, headers=headers)
              classReportList = getreport1.json().get('classReportList')
              print(classesId)
              for x in range(len(classReportList)):
                  cl = classReportList[x]
                  reurl = cl.get('reportUrl')

                  print(reurl)
              nn = int(input('删除课程请输入1:'))
              b1 = fff.B()
              b1.deleteclass1(nn)


         else:
             time2 = time.localtime((startTime/1000))
             dt = time.strftime("%Y-%m-%d %H:%M:%S", time2)
             print('课程还未开始,开始时间：',dt)




    # print(cek2.status_code)
    # if cek2.status_code == 200:






         # r=json.dumps(data,indent=1)

         #print(b)
         k = k + 1
         #break
      except Exception:
        print('必须是整数或者课程不存在或者try里面出现错误')
   else:
       print('没有课程，请先添加好课程，再来上课QAQ')
       ff2.add_class(coachId)

       #a1.addclass(coachId)#调用需要执行的方法  首次加课
       #fff.addclasses(coachId)
       print('添加了一节课')












else:
    print('用户名或密码错误')

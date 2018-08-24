'''
import time
import threading
import multiprocessing
from multiprocessing import Pool
def A(a,b):
    try:
        for i in range(1,int(b)):
            a+=b

            if int(b)>4:

                return a
            else:

                a+=a

        return a
    except TypeError:
        return '参数错误'
    except ValueError:
        return '字符转换错误'

def B():
    for i in range(10):
        if i%2!=0:
            print('woshishen:',i)
            continue

        print(i)
        i+=2
        #print(i)
def num():
    print(1)
    #time.sleep(1)
def aa():
    t1 = threading.Thread(target=num)
    t2 = threading.Thread(target=num)
    t3 = threading.Thread(target=num)
    t4 = threading.Thread(target=num)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
if __name__ == '__main__':
   # print(A(1,4))
   # print(A(1,5))
   # print(A(1,1))
   # print(A('1',2))
    #print(A('1','2'))

   manager = multiprocessing.Manager()
   p = Pool(4)
   time1=time.time()
   for i in range(100):
       # time.sleep(3)
       # 将请求的进程一个个添加到池里，池满的话，等待之前的进程完成，释放池空间，然后继续添加进程  同步执行：执行完所需要调用函数里面的所有函数后才会继续下一个进程
       # 异步执行是在等待某个任物执行时在干其他事。由于函数内部调用的函数太多，使用异步导致数据大量丢失。。。
       p.apply(aa)
   p.close()
   p.join()
   time2=time.time()
   print(time2-time1)

  #  print(A('1','aa'))'''
import aiohttp
import ssss
#from aiohttp import ClientSession
import asyncio
import hashlib
import pad_app.主要接口.interface as f1
import base64
import time
import requests
from multiprocessing import Pool,Process
import pad_app.上课.add_user_class as ff2
import pad_app.上课.function  as fff
import 查询数据.select_data as f5
import log_mokuai as f7
log1=f7.log()
async def hello(data1):


    async with aiohttp.ClientSession() as session:
        headers = {'user_Agent': 'KKTabletUDP/Android',
                   'connection': 'Keep - Alive',
                   'Accept - Encoding': 'gzip',
                   'Host': 'test.kuaikuaikeji.com',
                   'Cache - Control': 'no-cache',
                   }
        username='17600958351'
        password='123456'

        async with session.post("http://test.kuaikuaikeji.com/kcas/PadCoachLoginV2", headers=headers) as res:

            auth = res.headers.get('WWW-Authenticate', '')
            m = hashlib.md5()  # 创建md5对象
            m1 = hashlib.md5()
            # m2=hashlib.md5()
            # password='123456'
            # username='15600905550'
            '''strs1=(username+password).encode('utf-8')

            m.update(strs1)#生成加密串
            ha=m.hexdigest()#获取加密串
            #print(ha)'''
            m.update(password.encode('utf-8'))
            pd = m.hexdigest()

            password1 = base64.encodebytes(pd.encode('utf-8'))[:-1]  # base64编码
            password1 = password1.decode('utf-8')
            # password2=password1.decode('utf-8')
            # print(password1)
            '''username1=username.encode('utf-8')#string类型转换成byte类型
             up=(username1+password1).encode('utf-8')
             print(up)#也可以用'''
            up = (username + password1)
            strs2 = (auth + up).encode('utf-8')

            m1.update(strs2)  # 生成加密串
            resp = m1.hexdigest()  # 获取加密串`

            response = base64.encodebytes(resp.encode('utf-8'))[:-1]

            response = response.decode('utf-8')  # byte类型转换成string类型

            author = "user=\"" + username + "\",response=\"" + response + "\""
            print(author)

            headers = {'user_Agent': 'KKTabletUDP/Android',
                       'connection': 'Keep - Alive',
                       'Accept - Encoding': 'gzip',
                       'Host': 'test.kuaikuaikeji.com',
                       'Cache - Control': 'no-cache',
                       'authorization': author,

                       }

            async with session.post("http://test.kuaikuaikeji.com/kcas/PadCoachLoginV2", headers=headers) as req:
                a=await req.json()
                if req.status==200:
                    data_ = data1.get('classDataList')
                    coachId=a['coachId']

                    for y in data_:
                        y = y


                    coursecode = y.get('courseCode')
                   # classesid = y.get('classesId')

                    # subjectid = y.get('subjectId')
                    # print(data)
                    n = int(len(data_))
                   # print(classesid)
                    #print( coursecode)

                    #print(''.format(classesid))

                    if 'SJ' not in coursecode:

                        classes_id = ff2.add_class1(coachId, coursecode, n)  # 加的课的id，不可缺少
                        #print('classid')
                      #  print(classes_id)


                        a = fff.A(2)
                        gym_id = a.get_gymid(coachId)
                        subjectid = a.get_subjectId(gym_id)

                        # classesId =  y.get('classesId')  # 好简单 ，昨天试了半天。目前感觉还不是很好
                        # startTime =  y.get('startTime')  # 毫秒级时间戳
                        # endTime =  y.get('endTime')

                        # print(tme1)




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
                       # r = res_session.post(url=f1.kkweight_app_url2 + f1.获取课程列表信息, json=data, headers=headers)
                       # data1 = {
                      #      'classesId': classes_id,
                     #   }
                       # st = res_session.post(url=f1.kkweight_app_url2 + f1.开始课程, json=data1, headers=headers)
                        # coursecode=st.json()
                        data2 = {
                            'coachId ': coachId,
                            'classesId': classes_id,
                            'courseCode': coursecode

                        }
                        #cek1 = res_session.post(url=f1.kkweight_app_url2 + f1.获取课程详细信息, json=data2, headers=headers)

                        async with session.post(url=f1.kkweight_app_url2 + f1.查看签到状态, json=data2, headers=headers) as req1:
                            numbers1 = await req1.json()
                            print(numbers1)
                            numbers=numbers1['userCheckinMap']
                            t = []
                            i1 = len(numbers)
                            # classes_id=(classes_id)
                            for y in numbers:
                                # b=numbers[y]

                                t.append(y)  # 把人数换成列表格式
                            # print(t[0])
                            # data1 = f2.data1()
                            # data1 = data1.get('classDataList')
                            start_time1 = (time.time()) * 1000
                            # print(start_time1)
                            # start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_time1)
                            # print(start_time)
                            end_time1 = (time.time() + 3600) * 1000
                            # print(end_time1 )
                            # end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_time1)
                            # print(len(data1))
                            classDataList = []

                            # print(1)
                            # print(n)
                            for i in range(n):
                                # print(data_)
                                # classesId = '218527'
                                # weight=data_[i]['weightData']
                                # print(weight)
                                # print(i)
                                if 'weightData' in data_[i]:
                                    data_[i]['weightData'] = data_[i]['weightData']
                                    data_[i]['baseData'] = data_[i]['baseData']

                                else:
                                    pass

                                data_[i]['endTime'] = end_time1
                                data_[i]['startTime'] = start_time1
                                # data1[i]['subjectId'] = subjectid
                                data_[i]['userUuid'] = t[i]
                                data_[i]['classesId'] = classes_id
                                data_[i]['subjectId'] = subjectid

                                # data1[i]['courseCode'] = coursecode
                                classDataList.append(data_[i])
                                # print(3)

                                # print(classDataList)


                                # cek3 = res_session.post(url='http://test.kuaikuaikeji.com/kcas/PadGetCoachClassInfoV2', json=data,headers=headers)  # 刷新后的页面，获取课程详情
                            # print(2)
                            data3 = {'classDataList': classDataList,
                                     "uploadType": 1,
                                     'uploadVersion': 3
                                     }
                            # print(coursecode )
                            time1 = time.time()

                            async with session.post(url=f1.kkweight_app_url2 + f1.上传报告, json=data3, headers=headers) as req2:
                                # print(report1.json())
                                # print(report1.status_code)
                                # print(classesId)

                                aa = fff.D()
                                number = aa.number()
                                # await req2.json()
                                time2 = time.time()
                                # tmeout = (report1.elapsed.microseconds)/number#发送请求到服务器端响应的时间大于1秒，只会截取后面的小数部分
                                # tmeout1 = req2.elapsed.total_seconds()  # 这个才是正确的 获取响应时间，发送请求到收到相应的时间差
                                # report1.elapsed.
                                timeout=time2 - time1
                                print('上传报告所需时间',timeout )
                                # print('上传报告所需时间', tmeout)
                                if req2.status == 200:
                                    data4 = {'classesId': classes_id,
                                             'subjectId': subjectid}
                                    async with session.post(url=f1.kkweight_app_url2 + f1.报告列表, json=data4,
                                                            headers=headers)  as req4:
                                        # print(getreport1.json())
                                        classReportList1 = await req4.json()
                                        classReportList = classReportList1['classReportList']
                                        for x in range(len(classReportList)):
                                            cl = classReportList[x]
                                            reurl = cl.get('reportUrl')
                                        log1.info('chenggong{} '.format(timeout))

                                        # print(reurl)

                                        # if getreport1.status_code!=200:
                                        # print(classes_id)
                                        # exit()

                                        # else:
                                        #  print('success')
                                        # classReportList = getreport1.json().get('classReportList')
                                        # print(classes_id)

                                else:
                                    print('上传失败 ', req2.status)
                                    log1.error('shibai{}{}'.format(req2.status,timeout))

                                    #print(classes_id)




                    else:
                        pass



                else:
                    print('用户名或密码错误')


                              #print(response)





def renwu():
    data2 = f5.data1()
    task = []
    loop = asyncio.get_event_loop()
    for i in range(120):
        task1 = loop.create_task(hello(data2))
        task.append(task1)

    # tasks=loop.create_task(task)
    loop.run_until_complete(asyncio.wait(task))
if __name__ == '__main__':
   p1=Process(target=renwu)
   #p2 = Process(target=renwu)
  # p3 = Process(target=renwu)
   #p4 = Process(target=renwu)
   p1.start()
  # p2.start()
  # p3.start()
  # p4.start()



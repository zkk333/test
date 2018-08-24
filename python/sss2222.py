import asyncio
import multiprocessing
import random
import time
import pad_app.上课.function  as fff
import requests
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import threading
from threading import Event
from multiprocessing import Process
import multiprocessing
import 查询数据.select_data_1 as f3
from multiprocessing import Queue
import user_app1.user_app.weightphone_main as ff
import pad_app.主要接口.interface as f2
import time
import requests
import os
from multiprocessing import Process
import multiprocessing
import pad_app.上课.add_user_class as ff2
from multiprocessing import Queue
import pad_app.主要接口.interface as f1

import time
import requests
import os
from multiprocessing import Pool
#import pad_app.updata1 as f7

from multiprocessing import Pool
import sssss as f5
import aiohttp
import hashlib
import base64
def worker(data1):
    print('haha{},,,hhh{}'.format(os.getpid(),time.time()))
   # print('{}'.format(threading.current_thread()))
    #print(data)
    print(33)
    #f1.report_test(data1)



class MySpider(object):
    def __init__(self):
        self.queue = asyncio.Queue(maxsize=1000) # 任务队列# 进程池self.event = Event()

        #self.p = Pool(4)
        self.event = Event()
    @classmethod
    def pool1(self):
        global pool3
        # data = f3.select_data1()

        # q = manager.Queue()
        pool3 = ProcessPoolExecutor(max_workers=4)
        print(pool3)
        return pool3

    async def hello(self,datas):

        async with aiohttp.ClientSession() as session:
            headers = {'user_Agent': 'KKTabletUDP/Android',
                       'connection': 'Keep - Alive',
                       'Accept - Encoding': 'gzip',
                       'Host': 'test.kuaikuaikeji.com',
                       'Cache - Control': 'no-cache',
                       }
            username = '17600958351'
            password = '123456'

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
                    a = await req.json()
                    if req.status == 200:
                        data_ = datas.get('classDataList')
                        coachId = a['coachId']
                        for y in data_:
                            y = y

                        coursecode = y.get('courseCode')
                        classesid = y.get('classesId')

                        # subjectid = y.get('subjectId')
                        # print(data)
                        n = int(len(data_))

                        print(coursecode)

                        if 'SJ' not in coursecode:

                            classes_id = ff2.add_class1(coachId, classesid, coursecode, n)  # 加的课的id，不可缺少
                            print('classid')
                            print(classes_id)

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
                            # cek1 = res_session.post(url=f1.kkweight_app_url2 + f1.获取课程详细信息, json=data2, headers=headers)

                            async with session.post(url=f1.kkweight_app_url2 + f1.查看签到状态, json=data2,
                                                    headers=headers) as req1:
                                numbers1 = await req1.json()
                                print(numbers1)
                                numbers = numbers1['userCheckinMap']
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
                                async with session.post(url=f1.kkweight_app_url2 + f1.上传报告, json=data3,
                                                        headers=headers) as req2:
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
                                    print('上传报告所需时间', time2 - time1)
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
                                                print(reurl)

                                                # if getreport1.status_code!=200:
                                                # print(classes_id)
                                                # exit()

                                                # else:
                                                #  print('success')
                                                # classReportList = getreport1.json().get('classReportList')
                                                print(classes_id)

                                    else:
                                        print('上传失败 ', req2.status)


                        else:
                            pass



                    else:
                        print('用户名或密码错误')




    @classmethod
    #@asyncio.coroutine
    def producer(self,q,i,data):# 生产控制者#

        data1 = data[i][0]
        url = (f2.获取上课数据 + data1)
        url = url + '.txt'
        # print(data)

        # webbrowser.open(url)
        p = requests.get(url)
        data1 = p.json()
       # print(data1)
        # a.txt


        q.put(data1)
        time.sleep(0.3)




          # data = f3.select_data1()

    #@asyncio.coroutine
    async def customer1(self, q):  # 生产者

        # print(data)
        print('haha???')
        global data1
        # print('{},,,{}'.format(os.getpid(), os.getppid()))
        while True:
            if q.empty():
                break
            data1 = q.get()
            print('haha')
        await self.customer2(data1)

    #@asyncio.coroutine
    async def customer2(self, data1):  # 生产者

        #data1=2

        # print(data)

        # print('{},,,{}'.format(os.getpid(), os.getppid()))

        await self.queue.put(data1)
















   # @asyncio.coroutine
    async def customer(self):# 消费者

            #print(data)

            #print('{},,,{}'.format(os.getpid(), os.getppid()))
            while True:
                if   self.queue.empty():
                    break
                data2=await self.queue.get()



                print('doubi')
                print('haha{},,,hhh{}'.format(os.getpid(), time.time()))
                await self.hello(data2)


                #self.pool.submit(worker, data2)
                #p.apply_async(worker, data2)







            '''
            while True:
                #try:

                    start_time = time.time()

                    data1 = q.get(False)
                    if data1 is None:
                        break
                    # lock.acquire()
                    #print('guolail?')

                    worker(data1)
                    #print(os.getpid())
                    # print(data1)

                    end_time = time.time()
                    timeout = end_time - start_time
                    print('执行程序需要时间', timeout)
                    print('- - - - - - -  - - - - -  -')'''
                #except:
                    #continue

                    # print('shiba'%(os.getpid()))





            #self.pool.submit(worker, data)
            #for i in range(3):
                 #self.pool.submit(worker, data)
            #self.worker(data)

            #print('{},,,{}'.format(os.getpid(), os.getppid()))
            #print('{}'.format(threading.current_thread()))
          #  f1.report_test(data)

            #self.pool.submit(worker, data)
            #self.pool.submit(worker,data)
           # self.pool.submit(worker, data)
















            #print('xioec',os.getppid())




   # @asyncio.coroutine
    async def start(self,q,loop):

        #asyncio.ensure_future(self.customer1(q))
        loop.create_task(self.customer1(q))
        loop.create_task(self.customer())

        #asyncio.ensure_future(self.customer())

        print('guolail?')

    @classmethod
    def renwu(self,q):
        global loop
        #print('guolail?')
        loop = asyncio.get_event_loop()  # asyncio.get_event_loop方法可以创建一个事件循环
        task1 = []
        for i in range(2):
            task = MySpider().start(q,loop)


            task1.append(task)


      #  task3 = MySpider().start(q)

      #  task4 = MySpider().start(q)
            # task5 = MySpider().start()
            ##  task6 = MySpider().start()
            # task7 = MySpider().start()



            # task4 = MySpider().start()
        # task5 = MySpider().start()tasks1

        #task1=[task3,task4 ]
        print(task1)

        time1 = time.time()
       # task = loop.create_task()
        # task = loop.create_task(tasks1)
        loop.run_until_complete(asyncio.wait(task1))

        #print(task)
        #print(task.result())
        # loop.run_until_complete(asyncio.wait(tasks))  # run_until_complete将协程注册到事件循环，并启动事件循环asyncio.wait(tasks)
        time2 = time.time()
        print(time2 - time1)
        # print(task.result())



if __name__ == '__main__':

   data=f3.select_data1()
   p = Pool(4)


   manager = multiprocessing.Manager()
   q =  manager.Queue()
   time1=time.time()
   for i in range(2):
       p.apply(MySpider.producer,args=(q,i,data))
       p.apply(MySpider.renwu,args=(q,))

   p.close()
   p.join()
   time2=time.time()
   print(time2-time1)


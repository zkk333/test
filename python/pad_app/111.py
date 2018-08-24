'''import uuid
import requests
import time
import hashlib

#import sys
#sys.path.append('F:\\untitled\\kk_user')
#import kk_user.kk_user_扫码
import user_app.weight_process as f


res_session= requests.session()

now_uuid=str(uuid.uuid1())
print(now_uuid)
url='http://test.kuaikuaikeji.com/kas/uploadweightuuid?uuid='+now_uuid
print(url)
json={"uuid":"xxxxx"}
json["uuid"]=now_uuid
print(json)
a=res_session.post('http://test.kuaikuaikeji.com/kcas/PadUserWeighingGetUserDataV2',json=json)
print(a)
#user_uuid=kk_user.kk_user_扫码.post_CR_cord(client,url)

#print(user_uuid)
username = '15600905501'
password = '123456'

headers = f.log( username, password,res_session)
login_userApp = res_session.post(url='http://test.kuaikuaikeji.com/kas/ulogin', headers=headers)
print(login_userApp.json())

weight = res_session.get(url=url, headers=headers)
print(weight.status_code)
print(weight.json())'''
'''data = {'uuid': uuid_make}
##print(data)


data={'uuid':uuid_make}
#json["uuid"]=uuid_make
#print(json)
weight_code=res_session.post('http://test.kuaikuaikeji.com/kcas/PadUserWeighingGetUserDataV2',json=data)#网址不能随意带空格。#主要是类似于生成二维码的
#print(a)
username='15234171516'
password='123456'
headers1=fff.log(username,password,res_session)
#print(headers)
login_log = res_session.post(url='http://test.kuaikuaikeji.com/kas/ulogin', headers=headers1)
#print(login_log.json())


url ='http://test.kuaikuaikeji.com/kas/uploadweightuuid?uuid='+uuid_make
print(url)
sweep_code1_s = res_session.get(url=url, headers=headers1)#get请求，不能用post请求，数据是在url中的，post请求是错误的#快快减肥app扫码操作时的接口
#print(uuid_make)
#print(sweep_code1_s.json())
print(sweep_code1_s.json())
#data = {'uuid': uuidl}
getdata1 = requests.post(url='http://test.kuaikuaikeji.com/kcas/PadUserWeighingGetUserDataV2', json=data,
                       headers=headers1
                        )#扫码完成后自助称重手机获取用户信息
useruuid=getdata1.json().get('userUuid')

#print(getdata1)
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
data['userUuid']=useruuid
checkdata1 = requests.post(url='http://test.kuaikuaikeji.com/kcas/PadGetUserCorrectWeightV2', json=data,
                           headers=headers1)#三次校验
data2=checkdata1.json().get('corrWeightData')
userUuid=checkdata1.json().get('userUuid')
memo=checkdata1.json()['modifiedMemo']
#print(memo)
data2['userUuid']=userUuid
data2['modifiedMemo']=memo
data2['dataSourceType']=3

#print(data2)
updata1=res_session .post(url='http://test.kuaikuaikeji.com/kcas/PadUserWeighingUploadWeightDataV2', json=data2)#上传数据
print(updata1.status_code)

#print(getdata1)
#print(b)
#uuid=b['uuid']

#print(uuid)'''

'''
import pad_app.上课.addclass1 as f
import uuid
import time
import re
uuid2=str(uuid.uuid1())
uuid2=uuid2.replace('-','')

time.sleep(1)
uuid3 = uuid.uuid1()
uuid3 = str(uuid3)
time.sleep(1)
uuid4 = uuid.uuid1()
uuid4 = str(uuid4)
a=f.A(2)
a.get_subject(uuid2,uuid3,uuid4)
'''
'''
import pad_app.上课.addclass1 as f
import re

gym_id='1443029947172864'
a=f.A(2)
#_class_id='214096'
#print(isinstance(_class_id,str))#判断是否是字符串

_class_id=a.get_everyday_classesId(gym_id)



a.isdelete(_class_id)
'''
'''
class CallbackBase:
   def __init__(self):
       self.__callbackMap = {}
       for k in (getattr(self,x) for x in dir(self)):
         if hasattr(k, "bind_to_event"):
           self.__callbackMap.setdefault(k.bind_to_event, []).append(k)
         elif hasattr(k, "bind_to_event_list"):
            for j in k.bind_to_event_list:
               self.__callbackMap.setdefault(j, []).append(k)

    ## staticmethod is only used to create a namespace
   @staticmethod
   def callback(event):
    def f(g, ev = event):
        g.bind_to_event = ev
        return g
    return f

   @staticmethod
   def callbacklist(eventlist):
      def f(g, evl = eventlist):
         g.bind_to_event_list = evl
         return g
      return f

   def dispatch(self, event):
      l = self.__callbackMap[event]
      f = lambda *args, **kargs: \
     map(lambda x: x(*args, **kargs), l)
      return f

## Sample
class MyClass(CallbackBase):
   EVENT1 = 1
   EVENT2 = 2

   @CallbackBase.callback(EVENT1)
   def handler1(self, param = None):
     print ('handler1 with param: %s" % str(param)')
     return None

   @CallbackBase.callbacklist([EVENT1, EVENT2])
   def handler2(self, param = None):
      print ('handler2 with param: %s" % str(param)')
      return None

   def run(self, event, param = None):
      self.dispatch(event)(param)


if __name__ == "__main__":
   a = MyClass()
   a.run(MyClass.EVENT1, 'mandarina')
   a.run(MyClass.EVENT2, 'naranja')

'''
import json
#import 查询数据.select_data as f

numbers = {'ecbd60c2-c40f-49cc-aef7-fe62f947178d': {'createTime': 1513652249000, 'status': 1, 'type': 0,
                                                    'uuid': 'ecbd60c2-c40f-49cc-aef7-fe62f947178d'},
           '1288c6c5-e5c1-4919-a774-246903cee842': {'createTime': 1513652249000, 'status': 1, 'type': 0,
                                                    'uuid': '1288c6c5-e5c1-4919-a774-246903cee842'},
           '3e4d6e11-bb41-4ec9-b2f5-75c4d8b93ab0': {'createTime': 1513652249000, 'status': 1, 'type': 0,
                                                    'uuid': '3e4d6e11-bb41-4ec9-b2f5-75c4d8b93ab0'}}
#b=numbers['3e4d6e11-bb41-4ec9-b2f5-75c4d8b93ab0']
#print(b)
#a=len(numbers)
'''
t = []
i1=len(numbers)
for y in numbers:
 # b=numbers[y]

   t.append(y)#把人数换成列表格式
#print(t[0])
data1=f.data1()
data1=data1.get('classDataList')
#print(data1)
classDataList=[]
for i in  range(len(data1)):
       #print(data_)
       classesId='218527'
       data1[i]['classesId'] =classesId
      # data1[i]['endTime'] = '11'
       #data1[i]['startTime'] = '1'
       #data1[i]['subjectId'] = '11'
       data1[i]['userUuid'] =t[i]
       #data_['courseCode'] ='123'
       classDataList.append(data1[i])
print(classDataList)'''
'''
import multiprocessing
from multiprocessing import Queue
import time

def dofunc(qname, num):
    qname.put(num)
    print("put %s to qname" % num)
    time.sleep(1)

def get_queue(q1):
    value = q1.get()
    print("get value %s from q" % value)
    time.sleep(1)


if __name__ == '__main__':
    q = Queue(5)
    for i in range(3):
        p = multiprocessing.Process(target=dofunc, args=(q, i))
        p.start()
    while 1:
       get_queue(q)
       if q.empty():
           break
    print("Finished")
    '''
'''
from multiprocessing import Process,Queue
import os
import time
import random
#首先得有生产者和消费者
# 生产者制造包子

def producter(q):
    for i in range(2):
        time.sleep(2) #生产包子得有个过程，就先让睡一会
        res = '包子%s'%i #生产了这么多的包子
        q.put(res)  #吧生产出来的包子放进框里面去
        print('\033[44m%s制造了%s\033[0m'%(os.getpid(),res))
    q.put(None) #只有生产者才知道什么时候就生产完了（放一个None进去说明此时已经生产完了）
# 消费者吃包子
def consumer(q):
    while True:#假如消费者不断的吃
        res = q.get()
        if res is None:break #如果吃的时候框里面已经空了，就直接break了
        time.sleep(random.randint(1,3))
        print('\033[41m%s吃了%s\033[0m' % (os.getpid(),res))
if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producter,args=(q,))
    p2 = Process(target=consumer,args=(q,))
    p2.daemon = True
    p1.start()
    p2.start()
    p1.join()
    p2.join()  #等待执行完上面的进程，在去执行主
    print('主')

'''
'''
from multiprocessing import Process
import multiprocessing
import user_app1.user_app.weightphone_main as ff
import time
from multiprocessing import Pool
import pad_app.updata1 as f1
def _data(q1):
    data=f1.data_()
    q1.put(data)
    q1.join()
    time.sleep(10)
def class_id(q2):
    data=q1.get()
    class_id=f1.classesId(data)
    q2.put(class_id)
    q2.join()

    q2.task_done()
    time.sleep(12)
    #print(class_id)
#multiprocessing
def f(q1,q2):#定义一个函数第一个进程
  #while True:#print('第一个进程')
    start_time=time.time()
    data=q1.get()
    class_id=q2.get()


    f1.report_test(class_id,data)

    end_time=time.time()
    timeout=end_time-start_time
    print('执行程序需要时间',timeout)
    print('- - - - - - -  - - - - -  -')
    q2.task_done()


    time.sleep(20)


class Myprocess(Process):  # 这个类myprocess 继承Process类第二个继承，两种方法
    def run(self):

        print('这是第二个进程')
def duojincheng():#多继承分主进程与子进程
    for i in range(3):
        #time.sleep(5)
        p1 = Process(target=f, args=(i,))#多进程调用f函
        #p2=Myprocess()
        #p2=Process

        print(p1.name)
        p1.start()
        #p2.start()
        #print(p2.ppid)
        print(p1.pid)

        p1.join(100)

#  上面的函数是简单的多进程


if __name__ == '__main__':
    #p2 = Myprocess()
    #p2.start()
    #p1=Process(target=f,args=())#多进程调用f函数
    #p1.start()
    #print('1234')
    manger=multiprocessing.Manager()
    q1=manger.Queue()
    q2=manger.Queue()
    po=Pool(1)#进程池
    for i in range(1):  #请求的进程数量
       p1=po.apply_async(_data,args=(q1,))
       p2=po.apply_async(class_id,args=(q2,))#将请求的进程一个个添加到池里，池满的话，等待之前的进程完成，释放池空间，然后继续添加进程  同步执行：执行完所需要调用函数里面的所有函数后才会继续下一个进程
       # 异步执行是在等待某个任物执行时在干其他事。由于函数内部调用的函数太多，使用异步导致数据大量丢失。。。

       p3=po.apply_async(f,args=(q1,q2))
       p2.daemon = True
       p3.daemon = True
    po.close()
    po.join()
'''#无法实现
'''
import uuid
import time
name='d1aaa4cc-306f-472a-ae09-da32d32b18f3'\
time=str(time.time())
namespace=uuid.NAMESPACE_DNS
namespace1=uuid.NAMESPACE_URL
namespace2=uuid.NAMESPACE_OID
print(namespace)
print(namespace1)
uuid1=uuid.uuid3(namespace,name+time)
uuid2=uuid.uuid3(namespace1,name+time)
uuid3=uuid.uuid3(namespace2,name+time)
print(uuid1)
print(uuid2)
print(uuid3)
'''

from multiprocessing import Process
import multiprocessing
import 查询数据.select_data_1 as f3
from multiprocessing import Queue
import user_app1.user_app.weightphone_main as ff
import pad_app.主要接口.interface as f2
import time
import requests
from multiprocessing import Pool
import pad_app.updata1 as f1
def c(q):
   data=f3.select_data()
   for data in data:
       data = data[0]
       # a.txt
       url = (f2.获取上课数据 + data)
       url = url + '.txt'
       #print(data)

       # webbrowser.open(url)
       p = requests.get(url)
       data1 = p.json()
       q.put(url)
       time.sleep(1)


#multiprocessing
def f(q):#定义一个函数第一个进程
  #while True:#print('第一个进程')
  while True:
     if not q.empty():
       start_time=time.time()
       data1=q.get()
       #f1.report_test(data1)
       print(data1)

       end_time=time.time()
       timeout=end_time-start_time
       print('执行程序需要时间',timeout)
       print('- - - - - - -  - - - - -  -')



       time.sleep(2)


class Myprocess(Process):  # 这个类myprocess 继承Process类第二个继承，两种方法
    def run(self):

        print('这是第二个进程')
def duojincheng():#多继承分主进程与子进程
    for i in range(3):
        #time.sleep(5)
        p1 = Process(target=f, args=(i,))#多进程调用f函
        #p2=Myprocess()
        #p2=Process

        print(p1.name)
        p1.start()
        #p2.start()
        #print(p2.ppid)
        print(p1.pid)

        p1.join(100)

#  上面的函数是简单的多进程


if __name__ == '__main__':
    #p2 = Myprocess()
    #p2.start()
    #p1=Process(target=f,args=())#多进程调用f函数
    #p1.start()
    #print('1234')
    manger = multiprocessing.Manager()
    q=manger.Queue()

    po=Pool()#进程池
    for i in range(5):  #请求的进程数量
       po.apply_async(c,args=(q,))
      #将请求的进程一个个添加到池里，池满的话，等待之前的进程完成，释放池空间，然后继续添加进程  同步执行：执行完所需要调用函数里面的所有函数后才会继续下一个进程
       # 异步执行是在等待某个任物执行时在干其他事。由于函数内部调用的函数太多，使用异步导致数据大量丢失。。。
       po.apply_async(f,args=(q,))

    po.close()
    po.join()
    #duojincheng()#主进程
    #p2 = Myprocess()
   # p2.start()

   # print(2222)










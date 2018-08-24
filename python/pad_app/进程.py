from multiprocessing import Process
import multiprocessing
import 查询数据.select_data_1 as f3
from multiprocessing import Queue
import user_app1.user_app.weightphone_main as ff
import pad_app.主要接口.interface as f2
import time
import requests
import os
from multiprocessing import Pool
import pad_app.updata1 as f1
def c(q,i,data):


       # print(i)
        data1 = data[i]
       # a.txt
        url = (f2.获取上课数据 + data1)
        url = url + '.txt'
       #print(data)

       # webbrowser.open(url)
        p = requests.get(url)
        data1 = p.json()


        q.put(data1)


        q.put(None)
        time.sleep(0.3)



#multiprocessing
def f(q):#定义一个函数第一个进程
  #while True:#print('第一个进程')
  while True:
    try:
       start_time=time.time()

       data1=q.get(False)
       if data1 is None:
           break
       #lock.acquire()
       #f1.report_test(data1)
       print(os.getpid())
      # print(data1)

       end_time=time.time()
       timeout=end_time-start_time
       print('执行程序需要时间',timeout)
       print('- - - - - - -  - - - - -  -')

       #print('shiba'%(os.getpid()))



    except:
       # print('1')
        continue




       #time.sleep(2)
if __name__ == '__main__':
    #p2 = Myprocess()
    #p2.start()
    #p1=Process(target=f,args=())#多进程调用f函数
    #p1.start()
    #print('1234')
    manager = multiprocessing.Manager()
    q = manager.Queue()
    #lock=manager.Lock()
    p=Pool(4)#进程池
     #请求的进程数量
    #data = f3.select_data()
   # data = f3.select_data()
    data = ['c275c8a2-4753-439d-97d5-3c27b790eff6', 'c275c8a2-4753-439d-97d5-3c27b790eff6',
            'c275c8a2-4753-439d-97d5-3c27b790eff6', 'c275c8a2-4753-439d-97d5-3c27b790eff6','c275c8a2-4753-439d-97d5-3c27b790eff6', 'c275c8a2-4753-439d-97d5-3c27b790eff6',
            'c275c8a2-4753-439d-97d5-3c27b790eff6', 'c275c8a2-4753-439d-97d5-3c27b790eff6']

   # print(data)
   # a=len(data)
    time1=time.time()
    for i in range(1):
      p.apply(c,args=(q,i,data))
      #time.sleep(3)
      #将请求的进程一个个添加到池里，池满的话，等待之前的进程完成，释放池空间，然后继续添加进程  同步执行：执行完所需要调用函数里面的所有函数后才会继续下一个进程
       # 异步执行是在等待某个任物执行时在干其他事。由于函数内部调用的函数太多，使用异步导致数据大量丢失。。。
      p.apply(f,args=(q,))

    p.close()
    p.join()
    #duojincheng()#主进程
    time2 = time.time()
    print(time2-time1)
    #p2 = Myprocess()
   # p2.start()

   # print(2222)
import asyncio
import multiprocessing
import random
import time
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
import sssss as f5
import time
import requests
import os
from multiprocessing import Process
import multiprocessing

from multiprocessing import Queue


import time
import requests
import os
from multiprocessing import Pool
import pad_app.updata1 as f1

from multiprocessing import Pool


def worker(data):
    print('jincheng{}'.format(os.getpid()))
   # print('{}'.format(threading.current_thread()))
    #print(data)
    f1.report_test(data)


class MySpider(object):
    def __init__(self):
        self.queue = asyncio.Queue(maxsize=1000) # 任务队列# 进程池self.event = Event()

        self.pool =ProcessPoolExecutor(max_workers=1)
        self.event = Event()





    @asyncio.coroutine
    def producer(self):# 生产控制者#
        print('hages')
        for i in range(1):#5ca17dc0-15e6-4904-ad38-d49d1bfc3f71
           data=['e166b3fe-a763-4538-9a77-b2516d59034e','30e287fa-3802-44e0-b9d4-ddd130f2a1ca','30e287fa-3802-44e0-b9d4-ddd130f2a1ca','30e287fa-3802-44e0-b9d4-ddd130f2a1ca']
           #data=data[i]
          # data = f3.select_data1()
           print('hageshepi')
           yield from self.producer_003(i,data)
           self.event.set()






    @asyncio.coroutine
    def producer_003(self,i,data):# 最后一个生产者,负责把生产的东西加到队列里
        #item = random.randint(1, 100)

        data1 = data[i]

        url = (f2.获取上课数据 + data1)
        url = url + '.txt'
        # print(data)

        # webbrowser.open(url)
        p = requests.get(url)
        data1 = p.json()
        #item=i
        #print('xioecheng',os.getpid())
        #print("put Item", item)
        print('haha')
        yield from self.queue.put(data1) #await 可用来获取一个协程的执行结果

    @asyncio.coroutine
    def customer(self):# 消费者
        print('guolail?')
        while True:
            if self.event.is_set() and self.queue.empty():#self.event.is_set() and
                break
            data = yield from self.queue.get()
            #print(data)
            #print('{},,,{}'.format(os.getpid(), os.getppid()))


           # self.pool.submit(worker, data)


           # self.pool.submit(worker,data)
            #self.pool.submit(worker, data)
            #for i in range(3):
                 #self.pool.submit(worker, data)
            #self.worker(data)

            #print('{},,,{}'.format(os.getpid(), os.getppid()))
            #print('{}'.format(threading.current_thread()))
            f1.report_test(data)

            #self.pool.submit(worker, data)
            #self.pool.submit(worker,data)
           # self.pool.submit(worker, data)
















            #print('xioec',os.getppid())




    @asyncio.coroutine
    def start(self):

        asyncio.ensure_future(self.producer())
        asyncio.ensure_future(self.customer())

    @classmethod
    def renwu(self):
        global loop
        loop = asyncio.get_event_loop()  # asyncio.get_event_loop方法可以创建一个事件循环
        task1 = []
        for i in range(2):
            task = MySpider().start()

            task1.append(task)
            # task3 = MySpider().start()

            # ask4 = MySpider().start()
            # task5 = MySpider().start()
            ##  task6 = MySpider().start()
            # task7 = MySpider().start()



            # task4 = MySpider().start()
        # task5 = MySpider().start()tasks1


        print(task1)
        time1 = time.time()
        task = loop.create_task(asyncio.wait(task1,0.1))
        # task = loop.create_task(tasks1)
        loop.run_until_complete(task)
        #print(task)
        #print(task.result())
        # loop.run_until_complete(asyncio.wait(tasks))  # run_until_complete将协程注册到事件循环，并启动事件循环asyncio.wait(tasks)
        time2 = time.time()
        #print(time2 - time1)
        # print(task.result())


if __name__ == '__main__':
   '''
   p = Pool(4)
   time1=time.time()
   for i in range(4):
      p.apply_async(MySpider.renwu)
   p.close()
   p.join()
   time2=time.time()
   print(time2-time1)'''
   global loop
   loop = asyncio.get_event_loop()  # asyncio.get_event_loop方法可以创建一个事件循环
   task1 = []
   for i in range(2):
       task = MySpider().start()

       task1.append(task)
       # task3 = MySpider().start()

       # ask4 = MySpider().start()
       # task5 = MySpider().start()
       ##  task6 = MySpider().start()
       # task7 = MySpider().start()



       # task4 = MySpider().start()
   # task5 = MySpider().start()tasks1


   print(task1)
   time1 = time.time()
   task = loop.create_task(asyncio.wait(task1))
   # task = loop.create_task(tasks1)
   loop.run_until_complete(task)
   # print(task)
   # print(task.result())
   # loop.run_until_complete(asyncio.wait(tasks))  # run_until_complete将协程注册到事件循环，并启动事件循环asyncio.wait(tasks)
   time2 = time.time()
   time2 = time.time()
   print(time2 - time1)


















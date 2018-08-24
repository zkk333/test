from multiprocessing import Process
import multiprocessing
import 查询数据.select_data_1 as f3
from multiprocessing import Queue
import user_app1.user_app.weightphone_main as ff
import pad_app.主要接口.interface as f2
import time
import requests
import os
import pad_app.上课.function  as fff
from multiprocessing import Pool
import pad_app.updata1 as f1
import threading


#multiprocessing
def f():#定义一个函数第一个进程
  #while True:#print('第一个进程')
  a = fff.A(1)
  a.user()

def aa():
    t1 = threading.Thread(target=f)

    t2 = threading.Thread(target=f)

    t3 = threading.Thread(target=f)

    t4 = threading.Thread(target=f)


    t1.start()

    t2.start()

    t3.start()

    t4.start()




       #time.sleep(2)
if __name__ == '__main__':
    #p2 = Myprocess()
    manager = multiprocessing.Manager()

    # lock=manager.Lock()
    #p = Pool(4)  # 进程池
    # 请求的进程数量
    #p2.start()
    #p1=Process(target=f,args=())#多进程调用f函数
    #p1.start()
    #print('1234')
    for i in range(32):

        # time.sleep(3)
        # 将请求的进程一个个添加到池里，池满的话，等待之前的进程完成，释放池空间，然后继续添加进程  同步执行：执行完所需要调用函数里面的所有函数后才会继续下一个进程
        # 异步执行是在等待某个任物执行时在干其他事。由于函数内部调用的函数太多，使用异步导致数据大量丢失。。。
        p1 = Process(target=f)
        p1.start()
        p2 = Process(target=f)
        p2.start()
        p3 = Process(target=f)
        p3.start()






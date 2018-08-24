import 查询数据.select_data_1 as f1
import pad_app.主要接口.interface as f2
import multiprocessing
from multiprocessing import Queue

import requests
import time
import os
def c(q):
   data=f1.select_data()
   for data in data:
       data = data[0]
       # a.txt
       url = (f2.获取上课数据 + data)
       url = url + '.txt'
       #print(data)

       # webbrowser.open(url)
      # p = requests.get(url)
       q.put(url)
       time.sleep(2)
def f(q):
    while True:
     if not q.empty():
       cc=q.get()
       dd=cc
       print(os.getppid(),dd)
if __name__ == '__main__':
    q=Queue()
    p1=multiprocessing.Process(target=c,args=(q,))
    p2=multiprocessing.Process(target=f, args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()




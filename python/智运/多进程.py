import pad_app.主要接口.interface as f1
import 智运.login as f2
import 智运.kk_storefront_sql as f3
import requests
from  multiprocessing import queues
from multiprocessing import Pool
import multiprocessing
import 智运.健康贡献.yuedulv as f5
import random
uname='13910211681'
pwd='123456'
res_session=requests.session()
login_log=f2.log(uname,pwd,res_session)
gym_id2=[]
if login_log.status_code==200:
    headers = {'user_Agent': 'KKCoach/Android',
           'connection': 'Keep-Alive',
           'Accept-Encoding': 'gzip',
           'Host': 'test.kuaikuaikeji.com',
           'Cache-Control': 'no-cache',
           }
def c(q,i,id):


      gym_id=id[i][0]
      q.put(gym_id)
      q.put(None)
      q.put(0)

def f(q):
    while True:
      try:
       gym_id = q.get(False)
       if gym_id is 0:
           break
       if gym_id is None:
          break
       retio1=f5.yuedulv(gym_id)
       retio2=f5.yuedulv_ranzhi(gym_id)
       f5.gym_id1(retio1,retio2)

   # stdClassExpireStatus=range[3]

      except:
    # print('1')
        continue


if __name__ == '__main__':
    # p2 = Myprocess()
    # p2.start()
    # p1=Process(target=f,args=())#多进程调用f函数
    # p1.start()
    # print('1234')
    manager = multiprocessing.Manager()
    q = manager.Queue()
    #lock = manager.Lock()
    p = Pool(4)  # 进程池
    # 请求的进程数量
    # data = f3.select_data()
    id = f3.gym_id()
   # print(data)
    # a=len(data)
    for i in range(200):
        p.apply_async(c, args=(q, i, id))
        # time.sleep(3)
        # 将请求的进程一个个添加到池里，池满的话，等待之前的进程完成，释放池空间，然后继续添加进程  同步执行：执行完所需要调用函数里面的所有函数后才会继续下一个进程
        # 异步执行是在等待某个任物执行时在干其他事。由于函数内部调用的函数太多，使用异步导致数据大量丢失。。。
        p.apply_async(f, args=(q, ))

    p.close()
    p.join()
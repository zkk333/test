from multiprocessing import Process,Pool
import multiprocessing
import os,time

def run_proc(q,i):        ##定义一个函数用于进程调用
    #for i in range(5):

        #print(i)
    #休眠0.2秒
        q.put(i)


        time.sleep(0.1)


        #time.sleep(1)

#执行一次该函数共需1秒的时间
def run_proc1(q,):
    if not q.empty():
       # name=name
        data1 = q.get()
        # f1.report_test(data1)
        data1=data1+1
        print(data1)
    else:
        print('为空')

if __name__ =='__main__': #执行主进程
    print ('Run the main process (%s).' % (os.getpid()))
    manger = multiprocessing.Manager()
    q=manger.Queue()

    mainStart = time.time() #记录主进程开始的时间
    p = Pool(2)           #开辟进程池
    for i in range(200):   #开辟14个进程
        #print(q.qsize())
        p.apply_async(run_proc,args=(q,i,))#每个进程都调用run_proc函数，
       # time.sleep(2)
        p.apply_async(run_proc1, args=(q, ))

        #args表示给该函数传递的参数。\
    p.close()  # 关闭进程池
    p.join()

    print ('Waiting for all subprocesses done ...')
   # p.close() #关闭进程池
   # p.join()  #等待开辟的所有进程执行完后，主进程才继续往下执行
    print ('All subprocesses done')
    mainEnd = time.time()  #记录主进程结束时间
    print ('All process ran %0.2f seconds.' % (mainEnd-mainStart) ) #主进程执行时间
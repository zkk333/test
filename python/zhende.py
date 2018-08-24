'''
import time
import asyncio
import multiprocessing
from multiprocessing import Pool
# 定义异步函数
async def hello():
    #asyncio.sleep(1)
    print('Hello World:%s' % time.time())
async def hello1():
    #asyncio.sleep(1)
    print('Hello Worldhaha:%s' % time.time())
async def start():
    #asyncio.sleep(1)
    asyncio.ensure_future(hello())
    asyncio.ensure_future(hello1())
def run():
    for i in range(5):
        loop.run_until_complete(hello())
def renwu():
    global loop
    loop = asyncio.get_event_loop()
    task = []
    for i in range(5):
        task1 = start()
        task.append(task1)

    loop.run_until_complete(asyncio.wait(task))


if __name__ =='__main__':

    p = Pool(4)

    manager = multiprocessing.Manager()
    q = manager.Queue()
    time1 = time.time()
    for i in range(1):
        #p.apply(MySpider.producer, args=(q, i, data))
        p.apply(renwu)'''
import threading
import asyncio

@asyncio.coroutine

def hello1():
    print('Hello world1! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again1! (%s)' % threading.currentThread())

@asyncio.coroutine

def hello2():
    print('Hello world2! (%s)' % threading.currentThread())
    yield from asyncio.sleep(2)
    print('Hello again2! (%s)' % threading.currentThread())

@asyncio.coroutine

def hello3():
    print('Hello world3! (%s)' % threading.currentThread())
    yield from asyncio.sleep(3)
    print('Hello again3! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello1(),hello2(),hello3()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()







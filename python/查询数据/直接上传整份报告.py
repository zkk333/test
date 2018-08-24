import 查询数据.select_data_1 as f2
import 查询数据.select_data as f
from pad_app.上课.login import log
import requests
import pad_app.上课.upload_data as ff
import json
import copy
import time
from imp import  reload
import pad_app.上课.function  as fff
import pad_app.上课.add_user_class as ff2
#import weight_weighing.weight as ffff
import pad_app.weight_weighing.weight as ff1
import pad_app.主要接口.interface as f1
import requests
uname = '18610728165'
pwd = '123456'
res_session = requests.session()
if log(uname,pwd,res_session).status_code==200:
    data3=f.data1()
    headers = {'user_Agent': 'KKTabletUDP/Android',
               'connection': 'Keep - Alive',
               'Accept - Encoding': 'gzip',
               'Host': 'test.kuaikuaikeji.com',
               'Cache - Control': 'no-cache'
               }
    report1 = res_session.post(url=f1.kkweight_app_url2 + f1.上传报告, json=data3, headers=headers)
    print(report1.status_code)


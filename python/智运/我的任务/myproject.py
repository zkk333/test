import pad_app.主要接口.interface as f1
import 智运.login as f2
import pad_app.上课.function  as f6
import 智运.kk_storefront_sql as f3
import 智运.student.yuqiresult as f5
import requests
import time
import assertpy.assertpy.assertpy as f4
uname='13910211681'
pwd='123456'
f=f6.D()
#number=f.number()
res_session=requests.session()
login_log=f2.log(uname,pwd,res_session)
headers = {'user_Agent': 'KKCoach/Android',
           'connection': 'Keep-Alive',
           'Accept-Encoding': 'gzip',
           'Host': 'test.kuaikuaikeji.com',
           'Cache-Control': 'no-cache',


                           }
data = {"gymId":1383430562842624,
        "oneLevelCondition":2,#今日任务
        "pageControl": {"listSort": 1, "listSortField":1,"pageCount":-1,"pageIndex":0,"pageSize":50,"recordCount":-1},
        "twoLevelCondition":0,
        "userChar":"134"}#搜索框
ss = res_session.post(url=f1.kk_zhiyun_url3 + f1.智运我的任务接口, json=data, headers=headers)
f4.assert_warn(ss.status_code).is_equal_to(200)
data1={"gymId":1383430562842624}
ss1=res_session.post(url=f1.kk_zhiyun_url3+f1.获取我的任务里面的销售人员,json=data1,headers=headers)
f4.assert_warn(ss.status_code).is_equal_to(200)


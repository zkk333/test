import pad_app.主要接口.interface as f1
import 智运.login as f2
import pad_app.上课.function  as f6
import 智运.kk_storefront_sql as f3
import 智运.student.yuqiresult as f5
import requests
import time
import smpt.youjian as f7
import assertpy.assertpy.assertpy as f4
uname='13910211681'
pwd='123456'
#f=f6.D()

res_session=requests.session()
login_log=f2.log(uname,pwd,res_session)
headers = {'user_Agent': 'KKCoach/Android',
           'connection': 'Keep-Alive',
           'Accept-Encoding': 'gzip',
           'Host': 'test.kuaikuaikeji.com',
           'Cache-Control': 'no-cache',
           }
data={"queryDate":1526885336000,"gymId":1827944532281344}
url=f1.店员指标排名
ss = res_session.post(url=f1.kk_zhiyun_url3 + url, json=data, headers=headers)
f7.is_email(ss,url,None)
data={"queryDate":1520784000000,
      "gymId":1349430987786240,#门店id不重要，随意
      "coachId":2408433346807808,
      "queryDateType":3}#1和2
url=f1.具体店员指标月详情
ss1 = res_session.post(url=f1.kk_zhiyun_url3 + url, json=data, headers=headers)
#ss1.elapsed.total_seconds()
f7.is_email(ss1,url,None)



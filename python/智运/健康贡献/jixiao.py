import pad_app.主要接口.interface as f1
import 智运.login as f2
import pad_app.上课.function  as f6
import 智运.kk_storefront_sql as f3
import 智运.student.yuqiresult as f5

import requests
import excle11
import time
import math
import assertpy.assertpy.assertpy as f4

uname = '13910211681'
pwd = '123456'
gym_id='2047479369435136'
res_session=requests.session()
login_log=f2.log(uname,pwd,res_session)
headers = {'user_Agent': 'KKCoach/Android',
               'connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'Host': 'test.kuaikuaikeji.com',
               'Cache-Control': 'no-cache',
               }
data={"gymId":gym_id,
          "monthDate":1521684902000}
ss= res_session.post(url=f1.kk_zhiyun_url3 + f1.绩效接口, json=data, headers=headers)
coachdatalist=ss.json()['coachDataList']

for coachdatalist1 in coachdatalist:
    coachid=coachdatalist1['coachId']
    #print(coachid)
    performancerate=coachdatalist1['performanceRate']
    role=coachdatalist1['coachMainRole']#(coachid,) in f5.isoldcoachid()
    coach_set = (coachid, performancerate)
    coach_shiji = f5.old_performance(gym_id, coachid, role)
    #isold=f5.isoldcoachid()
    if (coachid,) in f5.isoldcoachid() :
        #print(abs(coach_set[1]-coach_shiji[1]))

        if abs(coach_set[1]-coach_shiji[1])<0.01:#由于精度误差，所有误差小于0.01就判断正确,python的精度很尴尬，所以0.01变成了0.011
            #if coach_set == f5.old_performance(gym_id,coachid,role):
                print('success')
        else:
                #pass
                print(coach_set,coach_shiji)
           # print(1)
    else:
        coach_shiji=f5.new_performance(coachid)
        if abs(coach_set[1] - coach_shiji[1]) < 0.01:
            print('success')
        else:
            # pass
            print(coach_set,coach_shiji)

    #print(performancerate)


import pad_app.主要接口.interface as f1
import 智运.login as f2
import pad_app.上课.function  as f6
import 智运.kk_storefront_sql as f3
import 智运.student.yuqiresult as f5
import requests
import excle11
import time
import math
import smpt.youjian as f7
import 智运.beiyong_11 as f8
import assertpy.assertpy.assertpy as f4
def dianyuanzhibiao(gym_id):
    uname = '13910211681'
    pwd = '123456'
    gym_id='1827944532281344'
    res_session=requests.session()
    login_log=f2.log(uname,pwd,res_session)
    headers = {'user_Agent': 'KKCoach/Android',
                   'connection': 'Keep-Alive',
                   'Accept-Encoding': 'gzip',
                   'Host': 'test.kuaikuaikeji.com',
                   'Cache-Control': 'no-cache',
                   }
    data={"queryDate":1526885336000,"gymId":gym_id}
    ss= res_session.post(url=f1.kk_zhiyun_url3 + f1.店员指标排名, json=data, headers=headers)
    #print(ss.json())
    incomemoney=ss.json()['coachDataList']#
    create_time1='2018-05'
    for incomemoney1 in incomemoney:
          income=incomemoney1['incomeMoney']
          coach_id=incomemoney1['coachId']
          coachname=incomemoney1['coachName']
          income1=f3.income_money(create_time1,gym_id,coach_id)/100

          f7.is_zhengque(income1,income,coachname)


def gym_id():
    gym_id = f8.gym_id1('kk_buz')
    #print(gym_id)
    for gym_id1 in gym_id:
        #print(gym_id1)
        gym_id1 = gym_id1[0]
        dianyuanzhibiao(gym_id1)
if __name__ == '__main__':
    gym_id()
      #print(income,coach_id)
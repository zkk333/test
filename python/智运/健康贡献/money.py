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

#f=f6.D()

def money(gym_id):
    uname = '13910211681'
    pwd = '123456'

    res_session=requests.session()
    login_log=f2.log(uname,pwd,res_session)
    headers = {'user_Agent': 'KKCoach/Android',
               'connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'Host': 'test.kuaikuaikeji.com',
               'Cache-Control': 'no-cache',
               }
    data={"gymId":gym_id,
          "monthDate":1526885336000}
    ss = res_session.post(url=f1.kk_zhiyun_url3 + f1.健康贡献接口, json=data, headers=headers)


    f4.assert_warn(ss.status_code).is_equal_to(200)

    #ss = res_session.post(url=f1.kk_zhiyun_url3 + f1.绩效接口, json=data, headers=headers)
    coachdata=ss.json()['coachDataList']

    for i in range(0,len(coachdata)):
        coachid=coachdata[i]['coachId']
        money=math.floor(coachdata[i]['commissionMoney'])

        coachname=coachdata[i]['coachName']
        #role=coachdata[i]['coachMainRole']
       # print(role)


        if (coachid,money) in  f5.calculate(i,coachid,gym_id):
            #print(coachname, (coach, money))
            print('success')
        else:
            print((coachname,(coachid,money)),( f5.calculate(i,coachid,gym_id)))
    f4.assert_warn(ss.status_code).is_equal_to(200)
def money_test():
    gym_name=excle11.main()
    for gym_name1 in gym_name:
        #print(gym_name1)
        gym_id=str(f3.gym_id_get(gym_name1))
       # gym_id='2655728082929664'
        money(gym_id)

       # print(a)
if __name__ == '__main__':
    gym_id = '2655728082929664'
    money(gym_id)



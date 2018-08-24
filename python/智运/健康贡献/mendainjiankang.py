import pad_app.主要接口.interface as f1
import 智运.login as f2
import pad_app.上课.function  as f6
import 智运.kk_storefront_sql as f3
import 智运.student.yuqiresult as f5
import requests
import excle11
import smpt.youjian as f8
import time
import math
import 智运.beiyong_11 as f7
import assertpy.assertpy.assertpy as f4
import copy
def mendian(gym_id):
    uname = '13910211681'
    pwd = '123456'
    # gym_id='2020192387647488'
    res_session = requests.session()
    login_log = f2.log(uname, pwd, res_session)
    headers = {'user_Agent': 'KKCoach/Android',
               'connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'Host': 'test.kuaikuaikeji.com',
               'Cache-Control': 'no-cache',
               }
    data = {"coachId":1976755360827392,"gymId":gym_id,"queryDate":1527230059000}
    ss = res_session.post(url=f1.kk_zhiyun_url3 + f1.门店端, json=data, headers=headers)
    mendianshouru=str(math.ceil(ss.json()['mainData']['realPerformance']))
    sale_time_1='2018-05'
    #gym_id='1827944532281344'
    mendianshouru_1=str(math.ceil(f7.ty_fee('kss',gym_id,sale_time_1)+f7.sijiao_money('kss',gym_id,sale_time_1)+f7.zhengshike('kss',gym_id,sale_time_1)+f7.yinpin('kk_buz',gym_id,sale_time_1)))
    print(f7.ty_fee('kss',gym_id,sale_time_1),f7.sijiao_money('kss',gym_id,sale_time_1),f7.zhengshike('kss',gym_id,sale_time_1),f7.yinpin('kk_buz',gym_id,sale_time_1))
    f8.is_zhengque(mendianshouru,mendianshouru_1,gym_id)
def gym_id():
    gym_id = f7.gym_id1('kk_buz')
    for gym_id1 in gym_id:
        gym_id1=gym_id1[0]
        #gym_id1='1956552506558464'
        mendian(gym_id1)
if __name__ == '__main__':
    gym_id()
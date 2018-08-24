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
def yuedulv(gym_id):
    uname = '13910211681'
    pwd = '123456'
    #gym_id='2020192387647488'
    res_session=requests.session()
    login_log=f2.log(uname,pwd,res_session)
    headers = {'user_Agent': 'KKCoach/Android',
                   'connection': 'Keep-Alive',
                   'Accept-Encoding': 'gzip',
                   'Host': 'test.kuaikuaikeji.com',
                   'Cache-Control': 'no-cache',
                   }
    data={"coachId":1976755360827392,"gymId":gym_id}
    ss= res_session.post(url=f1.kk_zhiyun_url3 + f1.今日课程, json=data, headers=headers)
    #a=ss.json()
    #print(ss.json())
    retio=ss.json()['monthMainData']['checkinRoomRate']

    id=f7.classes_id('kk_buz',gym_id)
    #print(id)
    capacity=0
    sum=0#上课总人数
    count=0#开设的课程数
    for classes_id in id:
      #print(classes_id)
      sum1=f7.user_subject_free('kk_buz',classes_id)
      sum2=f7.user_subject('kk_buz',classes_id)
      if sum1==sum2 and sum2!=0:#如果该节课不计费类型的赠送课的人数等于上课人数，那么移除该节课
          #id1.remove(classes_id)
          pass

      else:
          sum3=f7.user_subject('kk_buz',classes_id)#上课人数
          #print(sum3)
          count=count+1
          capacity1=f7.classes_capacity('kk_buz',classes_id)
          capacity=capacity+capacity1
          sum=sum+sum3
          #print(sum,count,capacity)
    try:
        retio1 = math.floor(sum / capacity * 100)
        return (retio1, retio)
    except ZeroDivisionError:
        retio1 = 0
        return (retio1, retio)


def yuedulv_ranzhi(gym_id):
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
        data = {"coachId": 1976755360827392, "gymId": gym_id}
        ss = res_session.post(url=f1.kk_zhiyun_url3 + f1.今日课程, json=data, headers=headers)
        # a=ss.json()
        # print(ss.json())
        retio = ss.json()['monthMainData']['checkinRoomRate']

        id = f7.classes_id_ranzhi('kk_buz', gym_id)
        capacity = 0
        sum = 0  # 上课总人数
        count = 0  # 开设的课程数
        for classes_id in id:
            # print(classes_id)
            sum1 = f7.user_subject_free('kk_buz', classes_id)
            sum2 = f7.user_subject('kk_buz', classes_id)
            if sum1 == sum2 and sum2 != 0:  # 如果该节课不计费类型的赠送课的人数等于上课人数，那么移除该节课
                # id1.remove(classes_id)

                pass

            else:
                sum3 = f7.user_subject('kk_buz', classes_id)  # 上课人数
                #print(sum3)
                count = count + 1
                capacity1 = f7.classes_capacity('kk_buz', classes_id)
                capacity = capacity + capacity1
                sum = sum + sum3
       # print(sum,count,capacity)
        try:
            retio1 = math.floor(sum / capacity * 100)
            return (retio1, retio)
        except ZeroDivisionError:
            retio1 = 0
            return (retio1, retio)
    #f8.is_zhengque(retio1,retio,gym_id)
def gym_id():
   gym_id=f7.gym_id1('kk_buz')
   #print(gym_id)
   for gym_id1 in gym_id:
      # print(gym_id1)
       gym_id1='2047495611598848'
       #gym_id1=gym_id1[0]
       retio1=yuedulv(gym_id1)[0]
       retio=yuedulv(gym_id1)[1]
       retio2=yuedulv_ranzhi(gym_id1)[0]
       if retio1>=retio2:
           f8.is_zhengque(retio1, retio, gym_id)
       else:
           f8.is_zhengque(retio2, retio, gym_id)

def gym_id1(retio1,retio2):

     retio11=retio1[0]
     retio=retio1[1]
     retio12=retio2[0]
     if retio11 >= retio12:
        f8.is_zhengque(retio11, retio, gym_id)
     else:
            f8.is_zhengque(retio12, retio, gym_id)

       #print(yuedulv(gym_id1))
      # print(yuedulv_ranzhi(gym_id1))
if __name__ == '__main__':


    gym_id()

#for classes_id1 in id1:




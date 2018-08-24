import pad_app.主要接口.interface as f1
import 智运.login as f2
#import pad_app.上课.function  as f6
import 智运.beiyong_11 as f3
import 智运.student.yuqiresult as f5
import requests
import time
import 智运.总部报表.baobiao1 as f11
import smpt.youjian as f7
import assertpy.assertpy.assertpy as f4
import math
def baobioa_yue(vl1,sale_time):
    uname='13910211681'
    pwd='123456'
    #f=f6.D()
    from requests.auth import HTTPBasicAuth
    res_session=requests.session()
    login_log=f2.log(uname,pwd,res_session)
    headers = {'user_Agent': 'KKCoach/Android',
               'connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'Host': 'test.kuaikuaikeji.com',
               'Cache-Control': 'no-cache',
               }
    #本日实际完成健康贡献值 dailyFeeYuan
    #本日健康贡献分配值 dailyTotalIncome
    #本月截止至当日已完成健康贡献monthFeeYuan
    #本月健康贡献分配值monthTotalIncome
    #本月截止至当日已完成健康贡献加饮料 totalMonthFeeYuan
    #本日实际完成健康贡献值加饮料 totalDailyFeeYuan
    #data={'day':'2018-05-09',
          #'_':1525859715026,
        #  'regionId':1,
      #    'vl':2}
    day1=math.floor(f3.shijian()[0]*1000)
    day_time=f3.shijian()[1]
    a='day=%s'%day_time
    _='_=%d'%day1
    vl='vl=%d'%vl1
    f=a+'&'+_+'&'+'regionId=1'+'&'+vl
    data1=(f)
    data1=('day={day_time}&_={day1}&regionId=1&vl={vl}'.format(day_time=day_time,day1=day1,vl=vl))

    #print(f)
    url=f1.报表

    ss = res_session.post(url=f1.kk_zhiyun_url3 + url,data=data1)#data字段可以传元组，json字段一般传json串
    statdata=ss.json()['statData']
    for statdara1 in statdata:
        #print(statdara1)
        gym_id=statdara1['gym_id']
        gym_id1=f11.baobiao(gym_id)[vl1]

        gymName=statdara1['gymName']
        monthFeeYuan=math.floor(statdara1['monthFeeYuan'])
        monthTotalIncome=math.floor(statdara1['monthTotalIncome'])
        totalMonthFeeYuan=math.floor(statdara1['totalMonthFeeYuan'])
        dailyFeeYuan=math.floor(statdara1['dailyFeeYuan'])
        dailyTotalIncome=math.floor(statdara1['dailyTotalIncome'])
        sum=0
        sum2=0
        #a={}
        for gym_id11 in gym_id1:
            sale=f3.gym_coach_sale('kss',gym_id11,sale_time)+f3.gym_coach_sale1('kss',gym_id11,sale_time)+f3.ty_fee('kss',gym_id11,sale_time)+f3.yinpin('kk_buz',gym_id11,sale_time)
            #print(sale)
            sum=sale+sum
        sum1=math.floor(sum)
        f7.is_zhengque(sum1,monthTotalIncome,gymName)
        for gym_id11 in gym_id1:
            sale1=f3.orders('kss',gym_id11,sale_time)+f3.yinpin('kk_buz',gym_id11,sale_time)
            sum2 = sale1 + sum2
        sum2=math.floor(sum2)
        f7.is_zhengque(sum2,totalMonthFeeYuan, gymName)
def baobioa_ri(vl1,sale_time):
    uname='13910211681'
    pwd='123456'
    #f=f6.D()
    from requests.auth import HTTPBasicAuth
    res_session=requests.session()
    login_log=f2.log(uname,pwd,res_session)
    headers = {'user_Agent': 'KKCoach/Android',
               'connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'Host': 'test.kuaikuaikeji.com',
               'Cache-Control': 'no-cache',
               }
    #本日实际完成健康贡献值 dailyFeeYuan
    #本日健康贡献分配值 dailyTotalIncome
    #本月截止至当日已完成健康贡献monthFeeYuan
    #本月健康贡献分配值monthTotalIncome
    #本月截止至当日已完成健康贡献加饮料 totalMonthFeeYuan
    #data={'day':'2018-05-09',
          #'_':1525859715026,
        #  'regionId':1,
      #    'vl':2}
    day1=math.floor(f3.shijian()[0]*1000)
    #day_time=f3.shijian()[1]
    a='day=%s'%sale_time
    _='_=%d'%day1
    vl='vl=%d'%vl1
    f=a+'&'+_+'&'+'regionId=1'+'&'+vl
    data1=(f)

    #print(f)
    url=f1.报表

    ss = res_session.post(url=f1.kk_zhiyun_url3 + url,data=data1)#data字段可以传元组，json字段一般传json串
    print(ss.elapsed.total_seconds())
    statdata=ss.json()['statData']
    for statdara1 in statdata:
        #print(statdara1)
        gym_id=statdara1['gym_id']
        gym_id1=f11.baobiao(gym_id)[vl1]

        gymName=statdara1['gymName']
        monthFeeYuan=math.floor(statdara1['monthFeeYuan'])
        monthTotalIncome=math.floor(statdara1['monthTotalIncome'])
        totalMonthFeeYuan=math.floor(statdara1['totalMonthFeeYuan'])
        totalDailyFeeYuan=math.floor(statdara1['totalDailyFeeYuan'])
        dailyTotalIncome=math.floor(statdara1['dailyTotalIncome'])
        sum=0
        sum2=0
        #a={}
        for gym_id11 in gym_id1:
            sale=f3.gym_coach_sale('kss',gym_id11,sale_time)+f3.gym_coach_sale1('kss',gym_id11,sale_time)+f3.ty_fee('kss',gym_id11,sale_time)+f3.yinpin('kk_buz',gym_id11,sale_time)
            #print(sale)
            sum=sale+sum
        sum1=math.floor(sum)
        f7.is_zhengque(sum1,dailyTotalIncome,gymName)
        for gym_id11 in gym_id1:
            sale1=f3.orders('kss',gym_id11,sale_time)+f3.yinpin('kk_buz',gym_id11,sale_time)
            sum2 = sale1 + sum2
        sum2=math.floor(sum2)
        f7.is_zhengque(sum2,totalDailyFeeYuan, gymName)
if __name__ == '__main__':
    sale_time = '2018-05'
    sale_time2='2018-05-01'
   # baobioa_yue(2,sale_time)#2：a大区 3：城市 5：门店
    baobioa_ri(2,sale_time2)



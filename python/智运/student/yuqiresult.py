import 智运.kk_storefront_sql as f3
import operator
import math
import 智运.student.retio as f2
import time
import 智运.kk_buz as f4
import re

import time
import datetime
from datetime import timedelta
def caoach_shiji(gym_id,role):

   a=f3.sale_coach_id1(gym_id,role)
   a=list(a)
   a=sorted(a,key=lambda a:a[1])#对名字进行排序
   #print(a)
   gym_name=f3.gym_name(gym_id)
   coachList=[]
   for a in a :
      #print(a)
      coach_Id=a[0]
      coach_Name=a[1]
      roles1=a[2]
      data={"coachId":coach_Id,
        "coachName":coach_Name,
        "gymId":int(gym_id),
        "gymName":gym_name,
        "roles": roles1}


      coachList.append(data)

   return coachList
def money_per(gym_id):
        coach_commissiom=f3.money_per(gym_id, '2018-05-01')



        return coach_commissiom
def gym_money(gym_id):
    gym_money=f3.money_gym(gym_id, '2018-05-01')
    return gym_money
def calculate(i,coachid,gym_id):
    #print(coach,sale,private_sale,coins_pay)
    coach_commissiom=money_per(gym_id)
    #print(coach_commissiom)
    commission=[]
    for coach_commissiom in coach_commissiom:

        coach = coach_commissiom[0]
        sale = coach_commissiom[1]#非橙卡健康贡献
        private_sale = coach_commissiom[2]
        coins_pay = coach_commissiom[3]
        sale1=sale+private_sale*f2.private_sale()+coins_pay*f2.coins_pay()#个人健康贡献
        #print(sale1)
        #role=coach_commissiom[4]
        if i==0 and coachid==coach:
          sale = sale / 100
          private_sale = private_sale / 100
          coins_pay = coins_pay / 100
          sale1=sale1/100
        #print(f2.sale_retio(sale))
        #print(sale*f2.sale_retio(sale))
          print(sale1)

          commission1=math.floor((sale*f2.sale_retio(sale))+(private_sale*f2.private_sale_retio())+(coins_pay*f2.coins_pay_retio())+ismanger(sale1,gym_id))
          #print(ismanger(sale))
          commission.append((coach, commission1))
          #print(commission)
        elif i>0 and coachid==coach:
           sale = sale / 100
           private_sale = private_sale / 100
           coins_pay = coins_pay / 100
           print(sale)
           commission1 =math.floor((sale * f2.sale_retio(sale)) + (private_sale * f2.private_sale_retio()) + (coins_pay * f2.coins_pay_retio()))#math.floor向下取整 个人健康价值
           commission.append((coach,commission1))
           #print(commission)

    return commission
def time_zh(year1,m1):
    a = datetime.datetime(year1, m1, 1)
    create_time1 = time.mktime(a.timetuple())
    create_time1 = time.localtime(create_time1)
    create_time2 = time.strftime('%Y-%m-%d', create_time1)
    return create_time2
def month():
    _create_time = time.localtime(time.time())
    create_time = time.strftime("%Y-%m-%d ", _create_time)
    return create_time
def month1():
    _create_time = time.localtime(time.time())
    create_time = time.strftime("%Y-%m", _create_time)
    return create_time
def ismanger(sale,gym_id):
    gym_money1=gym_money(gym_id)
    #print(gym_money1)
    fee=gym_money1[0]
    mch_fee=gym_money1[1]
    gym_money2=(fee+mch_fee)/100
    #print(gym_money2)
    #print(sale)

    shop_comission=f2.manger_retio(gym_money2)*(gym_money2-sale)
    #print(shop_comission)
    return shop_comission
def teach_score(teach):
    if teach:
        sum = 0
        times = 0
        for a1 in teach:
            score = a1[0]
            # print(score)
            times1 = a1[1]
            sum1 = score * times1
            times = times + times1

            sum = sum + sum1
        avage_score = sum / times
    else:
        avage_score=0

    return avage_score
def gym_class_per(gym_class):
    zs_checkin_count=gym_class[0]
    exp_checkin_count=gym_class[1]
    gym_capacity=gym_class[2]
    gym_class_per=(zs_checkin_count+exp_checkin_count)/gym_capacity
    return gym_class_per
def lc_per(lc):
    need_renewal_users=lc[0]
    retention_of_need_users=lc[1]
    return retention_of_need_users/need_renewal_users
def yuefen(create_time,n1):
    #create_time = month1()
    a = create_time.replace('-', '')
    year = int(a[:4])
    m = int(a[4:6])
    #print(year)
    #print(m - 2)
    if m - n1<= 0:
        a = abs(m - n1) / 12
        n = math.ceil(a)
        #print(n)
        if n==0:
            m1 = 12  - abs(m - n1)
            year1 = year
            month=time_zh(year1, m1)
        else:
            m1 = 12 * n - abs(m - n1)
            year1 = year - n
            month=time_zh(year1, m1)
    else:
        m1 = m-n1
        year1 = year
        month=time_zh(year1, m1)
    return month
def riqi(create_time1,create_time2):
    y1 = datetime.datetime.strptime(create_time1, '%Y-%m-%d')  # 把字符串变成日期
    y2 = datetime.datetime.strptime(create_time2, '%Y-%m-%d')
    # print(y)
    a = str(y1 - y2)

    a1 = int(re.findall(r'\d+', a)[0])  # d+主要是在一起的数字放在一起
    number1 = a1 + 1

    return number1
def isoldcoachid():
    create_time=month1()
    month_at =str(yuefen(create_time,1))#两个自然月
   # print(month_at)
    coach_id=f4.old_coach(month_at)
   # print(coach_id)
    return coach_id
def is_new_gym():
    create_time = month1()
    month_at=str(yuefen(create_time,3))
    gym_id=f4.old_gym(month_at)
    return gym_id
def gym_class_per1(gym_id):
    if (int(gym_id),) in is_new_gym():
        month_at1 = month1()
        gym_class = f3.gym_class(gym_id, month_at1)
        gym_class_per2 = gym_class_per(gym_class)
        return gym_class_per2
    else:
        return 0.4


def lc_per1(gym_id):
    if (int(gym_id),) in is_new_gym():
        month_at1 = month1()
        lc = f3.lc(gym_id, month_at1)
        lc_per2 = lc_per(lc)
       # print(1)
        return lc_per2
    else:
        #print(False)
        return 0.8
def xiaoshu(a):
    a = float('%.2f' % a)
    return a
def old_performance(gym_id,coach_id,role):
    '''gym_new_user_retio 门店新增学员数
    gym_class_retio 门店学员上课率
    gym_user_lc_retio 学员留存率 由于留存率的sql语句太难写，所以默认研发给的应续课学员以及应续课学员未流失人数字段是正确的
    money_retio  个人健康贡献'''

    #month_at = month()
    month_at1=month1()
    gym_new_user=f3.gym_new_user(gym_id,month_at1)
    gym_class_per2=gym_class_per1(gym_id)
    #print(gym_class_per2)
    lc_per2=lc_per1(gym_id)
    #print(lc_per2)
    coach_commissiom = money_per(gym_id)
    for coach_commissiom in coach_commissiom:
        coach = coach_commissiom[0]
        #role_list=f4.role(coach)
        sale = coach_commissiom[1]  # 非橙卡健康贡献
        private_sale = coach_commissiom[2]
        coins_pay = coach_commissiom[3]
        sale1 = sale + private_sale * f2.private_sale() + coins_pay * f2.coins_pay()  # 个人健康贡献

        if coach_id==coach and role==1:
            a = f2.Dianzhang()
            sale1=sale1/100

           # shopperformance=xiaoshu(a1)+xiaoshu(a2)+xiaoshu(a3)+xiaoshu(a4)
            #print(a.gym_new_user_retio(gym_new_user), a.gym_class_retio(gym_class_per2),a.gym_class_retio(gym_class_per2),
               #  a.money_retio(sale1))
            shopperformance=a.gym_new_user_retio(gym_new_user)+a.gym_class_retio(gym_class_per2)+a.gym_user_lc_retio(lc_per2)+a.money_retio(sale1)
            #shopperformance=float(str(shopperformance)[:4])#保留两位小数目前只能靠截取
            #print(a.gym_new_user_retio(gym_new_user),a.gym_class_retio(gym_class_per1),a.gym_user_lc_retio(lc_per1),a.money_retio(sale1),lc_per1,gym_class_per1)
            #print(shopperformance)
            shopperformance = float('%.3f' % shopperformance)
            return (coach_id,shopperformance)
        elif coach_id==coach and role==3:
            a=f2.Zhujiaolian()
            teach_score_coach= f4.teach(coach_id, month_at1)
            teach_score_gym = f4.teach_gym(gym_id, month_at1)
            teach=teach_score( teach_score_coach)
            teach1=teach_score(teach_score_gym)
            #print(a.gym_class_retio_zjl(gym_class_per2), a.gym_user_lc_retio_zjl(lc_per2), f2.teach_retio(teach),
                #  f2.user_teach_effect(teach1),lc_per2)
            shopperformance=a.gym_class_retio_zjl(gym_class_per2)+a.gym_user_lc_retio_zjl(lc_per2)+0.6#+f2.teach_retio(teach)+f2.user_teach_effect(teach1)
            #shopperformance = float(str(shopperformance)[:4])  # 保留两位小数目前只能靠截取
            #print(shopperformance)
            shopperformance = float('%.3f' % shopperformance)
            return (coach_id,shopperformance)
        elif coach_id==coach and role==2:
            sale1=sale1/100
            a=f2.Xiaoshou()
            num=f3.num(coach_id,month_at1)
            num1=num[0]
            num2=num[1]
            #print(a.geren_new_user_xs(num2),a.gym_user_lc_retio_xs(lc_per2),a.ty_num_xs(num1),a.money_retio_xs(sale1),lc_per2)
            shopperformance=a.geren_new_user_xs(num2)+a.gym_user_lc_retio_xs(lc_per2)+a.ty_num_xs(num1)+a.money_retio_xs(sale1)
           # print(shopperformance)
            #shopperformance = float(str(shopperformance)[:4])  # 保留两位小数目前只能靠截取
            shopperformance=float('%.3f' % shopperformance)

            return (coach_id,shopperformance)
        elif coach_id==coach and role==0:
            sale1 = sale1 / 100
            a = f2.Jiaolian()
            num = f3.num(coach_id, month_at1)
            teach_score_coach = f4.teach(coach_id, month_at1)
            #print(teach_score_coach)
            teach = teach_score(teach_score_coach)
            num1 = num[0]
            num2 = num[1]
            #print(a.geren_new_user_jl(num2),a.ty_num_jl(num1),a.money_retio_jl(sale1),f2.teach_retio(teach))
            shopperformance=a.geren_new_user_jl(num2)+a.ty_num_jl(num1)+a.money_retio_jl(sale1)+0.3#+f2.teach_retio(teach)
            #shopperformance = float(str(shopperformance)[:4])  # 保留两位小数目前只能靠截取
           # print(shopperformance)
            shopperformance = float('%.3f' % shopperformance)
            return (coach_id,shopperformance)
def new_performance(coachid):
    return (coachid,1)
if __name__ == '__main__':
    riqi()












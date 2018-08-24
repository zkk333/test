import pad_app.主要接口.interface as f1
import 智运.login as f2
import pad_app.上课.function  as f6
import 智运.kk_storefront_sql as f3
import 智运.student.yuqiresult as f5
import requests
import excle11
import time
import math
import 智运.kk_buz as f7
import datetime
import assertpy.assertpy.assertpy as f4
import django

def ty(coach_id,pay_fee):
    yeji=pay_fee*0.3
    return yeji
def ss():
    sale_coach_id='1953722829309952'
    create_time1='2018-04'
    #print(datetime.datetime(2018, 3, 12, 19, 20, 22))
    yeji=f3.yejifencheng1(sale_coach_id,create_time1)
    for yeji1 in yeji:
        user_uuid=yeji1[2]
        create_time=yeji1[0]
        pay_fee=yeji1[1]
        coins_pay=yeji1[3]

       #print(user_uuid)
        yeji2=f7.yejifencheng2(user_uuid)

        print(yeji2)
        a = []
        for i in range(len(yeji2)):

            if 'jianzhity'in yeji2[i][0]:
               coach_id1=yeji2[i][2]


               #pass
            if 'jianzhi' in yeji2[i][0]:
                a1=list(yeji2[i])
                a.append(a1)
            else:
                pass

        c=a[0]#体验课购买后的正式课
        buy_time=c[1]
        coach_id2=c[2]

        print(coach_id1)
        #ticheng=0
        '''
        if int(sale_coach_id)==int(coach_id1) and int(coach_id2)!=int(coach_id1):#教练买体验课，正式课其他教练买的
            yeji11= pay_fee
           # print(1)
            print(yeji11)
        else:

            yeji11=pay_fee*0.7
            #coach

        '''

    '''
        b=str(buy_time.strftime("%Y-%m-%d"))
        print(b)
        expire_time=f5.yuefen(b,-6)
        print(expire_time)
    '''
def zs_shijian(user_uuid):
    yeji2 = f7.yejifencheng2(user_uuid)

    a=[]
    for i in range(len(yeji2)):
         all_times=int(yeji2[i][3])
         if 'jianzhi' in yeji2[i][0] and all_times>1:
            a1 = list(yeji2[i])
            a.append(a1)


    c=a[0]
    buy_time=c[1]

    return buy_time
def ty_shijian(user_uuid):
    yeji2 = f7.yejifencheng2(user_uuid)

    a = []
    for i in range(len(yeji2)):
        all_times = int(yeji2[i][3])
        if 'jianzhi' in yeji2[i][0] and all_times==1:
            a1 = list(yeji2[i])
            a.append(a1)

    c = a[0]
    buy_time = c[1]
    return buy_time
def zs_id0(user_uuid,sale_coach_id):
    yeji2 = f7.yejifencheng2(user_uuid)
    c=[]
    for i in range(len(yeji2)):

        create_time=str(yeji2[i][1])
        all_times = int(yeji2[i][3])
        coach_id=str(yeji2[i][2])
        coins_pay=yeji2[i][4]
        pay_fee=yeji2[i][5]
        if 'jianzhi' in yeji2[i][0] and all_times > 1 and coach_id==sale_coach_id:
            fencheng=pay_fee
            create_time=create_time
            a= (create_time,fencheng,coach_id)
            c.append(a)
    return  c


def ll1():#体验课无教练，正式课为本教练或者没有体验课，正式课为本教练
    sale_coach_id = '1953722829309952'
    zs_xueyuan1 = f7.zs_xueyuan(sale_coach_id)
    #zs_xueyuan11=zs_xueyuan1[0]
    #print(zs_xueyuan1)
    fencheng1=0
    for user_uuid in zs_xueyuan1:
        user_uuid=user_uuid
        tydingdan=f7.tyxueyaun_wu(user_uuid)

        #print(tydingdan)
        for tydingdan1 in tydingdan:
           if tydingdan1:
               coach_id=tydingdan1[0]
               user_uuid1=tydingdan1[3]
               if coach_id==0:
                   a=zs_id0(user_uuid1,sale_coach_id)
                   fencheng=0
                   for a1 in a:
                        time1=a1[0]
                        fenchengs=a1[1]/100
                        if time1<'2018-04-01':
                            pass
                        else:
                            #fenchengs=fenchengs
                            fencheng=fenchengs+fencheng
                   return fencheng
           else:
               fencheng1=f7.zs_dingdan(user_uuid)
               fenchengs1=0
               for fencheng11 in fencheng1:
                   fenchengs=fencheng11[1]/100
                   fenchengs1=fenchengs1+fenchengs
               return fenchengs1







               #print(user_uuid)
def ll11():#体验课为其他教练，正式课为本教练
    sale_coach_id = '1953722829309952'
    zs_xueyuan1 = f7.zs_xueyuan(sale_coach_id)
    #zs_xueyuan11=zs_xueyuan1[0]
    #print(zs_xueyuan1)
    fencheng1=0
    for user_uuid in zs_xueyuan1:
        user_uuid=user_uuid
        tydingdan=f7.tyxueyaun_wu(user_uuid)

        #print(tydingdan)
        for tydingdan1 in tydingdan:
           if tydingdan1:
               coach_id=tydingdan1[0]
               user_uuid1=tydingdan1[3]
               buy_timety=str(tydingdan1[4])
               buy_time = str(zs_shijian(user_uuid1))
               a = zs_id0(user_uuid1, sale_coach_id)
               buy_time1=buy_time[0:10]
               buy_timety1 = buy_timety[0:10]
               fencheng = 0
               for a1 in a:
                   time1 = a1[0]
                   fenchengs = a1[1] / 100
                   riqi = f5.riqi(buy_time1, buy_timety1)

                   if riqi <= 15:
                       if int(coach_id) != int(sale_coach_id) and time1 == buy_time:#体验课其他人，转化为当前教练
                           fencheng1=fenchengs*0.3
                           print(fencheng1)
                       elif int(coach_id) != int(sale_coach_id) and time1>buy_time:  # 体验课其他人，续课为当前教练
                            fencheng1 = fenchengs * 0.7
                            print(fencheng1)
                       fencheng = fencheng1 + fencheng
                       return fencheng

                   else:
                       if int(coach_id) != int(sale_coach_id) and time1 == buy_time:  # 体验课其他人，转化为当前教练。15天以后
                            fencheng1 = fenchengs * 1.0
                            print(fencheng1)
                       elif  int(coach_id) != int(sale_coach_id) and time1 > buy_time:  # 体验课其他人，续课为当前教练
                            fencheng1 = fenchengs * 0.7
                            print(fencheng1)
                       fencheng = fencheng1 + fencheng
                       return fencheng







           else:
               pass







               #print(user_uuid)








def ll():#教练的体验课，对正式课做判断
    sale_coach_id = '1953722829309952'
    zsdingdan = f7.tyxueyuan(sale_coach_id)#教练的体验课查找的正式课订单
    print(zsdingdan)
    #aa=f7.user(sale_coach_id)
    #print(aa)
    fencheng1 = 0
    fencheng2=0
    for zsdingdan1 in zsdingdan:
        price_code=zsdingdan1[0]
        create_time=str(zsdingdan1[1])
        coach_id=zsdingdan1[2]
        coins_pay=zsdingdan1[3]
        pay_fee=zsdingdan1[4]
        user_uuid=zsdingdan1[5]
        buy_time=str(zs_shijian(user_uuid))#第一次买正式课的时间
        buy_timety=str(ty_shijian(user_uuid))
        #print(buy_time)
        #print(pay_fee)
        #a=str(price_code)
        buy_time1 = buy_time[0:10]
        buy_timety1 = buy_timety[0:10]


        riqi=f5.riqi(buy_time1,buy_timety1)

        if riqi<=15:
            if int(coach_id) != int(sale_coach_id) and create_time==buy_time:#教练买体验课，其他教练买正式课，转化业绩
                #print(pay_fee)
                #print(create_time)
                #print(price_code)
                fencheng = (pay_fee/100) * 0.7
                print(fencheng)
            elif int(coach_id) != int(sale_coach_id) and create_time>buy_time :#续课业绩
                fencheng=(pay_fee/100)*0.3
                print(fencheng)
            elif int(coach_id) == int(sale_coach_id) and create_time==buy_time:#教练的体验课，教练的正式课，转化
                fencheng=pay_fee/100
                print(fencheng)
            elif int(coach_id) == int(sale_coach_id) and create_time > buy_time:  # 教练的体验课，教练的正式课，续课
                fencheng = pay_fee/100
                print(fencheng)
            fencheng1 = fencheng1 + fencheng
            return fencheng1

        else:
            if int(coach_id) != int(sale_coach_id) and create_time == buy_time:  # 教练买体验课，其他教练买正式课，大于15天不算转化
                # print(pay_fee)
                # print(create_time)
                # print(price_code)
                fencheng = (pay_fee / 100) * 0
                print(fencheng)
            elif int(coach_id) != int(sale_coach_id) and create_time > buy_time:  # 续课业绩
                fencheng = (pay_fee / 100) * 0
                print(fencheng)
            elif int(coach_id) == int(sale_coach_id) and create_time == buy_time:
                fencheng = pay_fee / 100
                print(fencheng)
            elif int(coach_id) == int(sale_coach_id) and create_time > buy_time:
                fencheng = pay_fee / 100
                print(fencheng)
        fencheng1 = fencheng1 + fencheng
        return fencheng1






if __name__ == '__main__':
    fencheng=ll()+ll1()+ll11()
    print(fencheng)





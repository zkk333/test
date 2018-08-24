
import  pymysql
import requests
import re
import time
import uuid
import random
import string
import sys
import warnings
warnings.filterwarnings('ignore')
import excle11 as f1

# coding: UTF-8
#单次课程
'''
try:

    con = pymysql.connect(host="192.168.41.41",
                          user="test",
                          password="test@kuaikuai",
                          db="kk_buz",
                          port=3306,
                          charset='utf8')  # 连接数据库utf-8放进去报错，找了半天原因  ，只是在数据库中用utf8而已，就是指代一种编码
    cursor = con.cursor()
except:
    print('连接失败')
'''

try:

    con = pymysql.connect(host="192.168.40.233",
                          user="kk_stat",
                          password="kuaikuaikss_123",
                          db="kss",
                          port=3306,
                          charset='utf8')  # 连接数据库utf-8放进去报错，找了半天原因  ，只是在数据库中用utf8而已，就是指代一种编码
    cursor = con.cursor()
except:
    print('连接失败')

def coachId(tel):
    sql='select id from coach where tel=%s'
    cursor.execute(sql,tel)
    id=cursor.fetchone()
    id=id[0]
    return id
def gym_id():
    sql='select id from gym where status=1'
    cursor.execute(sql)
    id=cursor.fetchall()
    return id

def gym_id_get(gym_name):
    sql='select id from gym where name=%s'
    cursor.execute(sql,gym_name)
    id=cursor.fetchall()
    if id:
      id=id[0][0]
    else:
        id=0
    return id
def gym_name(gym_id):
    sql='select name from gym where id=%s'
    cursor.execute(sql,gym_id)
    name=cursor.fetchall()
    name=name[0][0]
    return name
def gym_class(gym_id,month):

    sql='select zs_checkin_count,exp_checkin_count,gym_capacity from gym_month_rank where gym_id= \''+gym_id+'\' AND month_at like \'%'+ month+ '%\''
    cursor.execute(sql)
    id=cursor.fetchall()
    id=id[0]
    return id
def gym_new_user(gym_id,month):
    month='%'+month+'%'
    sql='select new_user from gym_month_rank where gym_id= \''+gym_id+'\' AND month_at like %s '#本质上需要换的sql语句，注释掉
    cursor.execute(sql,month)
    new_user=cursor.fetchall()
    #print(new_user)
    new_user=new_user[0][0]
    return new_user
def lc(gym_id,month):
    sql='select need_renewal_users,retention_of_need_users from gym_month_zhibiao where gym_id= \''+gym_id+'\' AND month like \'%'+ month+ '%\''
    cursor.execute(sql)
    lc = cursor.fetchall()
    if lc:
      lc = lc[0]
    else:
        print('baocuo')
    return lc
def num(coach,month):
    month = '%' + month+ '%'
    sql='SELECT exp_order_count,exp_off_order_count FROM coach_month_rank WHERE coach_id=%s  AND month_at LIKE %s'
    args=(coach,month)
    cursor.execute(sql,args)
    num=cursor.fetchall()
   # print(num)
    num=num[0]
    return num

def get_orders_id():
    sql = 'select max(id)+1 from orders '
    cursor.execute(sql)
    id1 = cursor.fetchall()
    id1 = id1[0][0]
    return id1
def sale_coach_id2(name):
    sql='select id from coach where name=%s'
    cursor.execute(sql,name)
    id=cursor.fetchone()
    if id:
      id=id[0]
    else:
      id=0

    return id

def get_user_subject_id():
    sql = 'select max(id)+1 from user_subject '
    cursor.execute(sql)
    id2 = cursor.fetchall()
    id2 = id2[0][0]
    return id2
def sale_coach_id(gym_id):
    sql='select id from coach where gym_id=%s'
    cursor.execute(sql,gym_id)
    id=cursor.fetchone()
    id=id[0]
    return id
def sale_coach_id1(gym_id,role):
    #tel='" + login_id + "
    #gym_id = \'' + gym_id + '\'
    role='%'+role+'%'
    sql='select id,name,role_list from coach where gym_id=' + gym_id+ ' and role_list like %s'
    #args=(gym_id,role)
    cursor.execute(sql,role)
    id=cursor.fetchall()
    #name=cursor.fetchall()
    id=id

    return id
def yejifencheng1(coach_id,create_time):
    create_time='%'+create_time+'%'
    sql='select create_time,pay_fee,user_uuid,coins_pay from user_order where sale_coach_id=%s and create_time like %s  and status=1'
    cursor.execute(sql,(coach_id,create_time))
    id=cursor.fetchall()
    id=id
    return id




def get_subjectFB( uuid2, uuid3,uuid4, gym_id,price_code,all_times,subject_show_id,deal_price,coins_pay,pay_fee,create_time1, create_time3,user_uuid,sale_coach_id1):
    # user_uuid=self.useruuid()
    # for user_uuid in user_uuid:


    # user_uuid = '492a685f-16a4-40c0-a0a3-17dec392c9bd'

    id1 = get_orders_id()
    id2 = get_user_subject_id()
    #sale_coach_id1=sale_coach_id(gym_id)
    _create_time = time.localtime(time.time() - 3600*24*2)
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", _create_time)
    start_data = time.strftime("%Y-%m-%d", _create_time)
    # end_data = time.strftime("%Y-%m-%d", _create_time)
    _create_time1 = time.localtime(time.time() - 3600*24 + 600)
   # create_time1 = time.strftime("%Y-%m-%d %H:%M:%S", _create_time1)
    _create_time2 = time.localtime(time.time() - 3600 + 365 * 24 * 3600)
    create_time2 = time.strftime("%Y-%m-%d %H:%M:%S", _create_time2)

    end_data = time.strftime("%Y-%m-%d", _create_time2)

    sql = 'insert into orders (id, price_code, all_times, subject_show_id, subject_id, deal_price, coins_pay, create_time, status, user_uuid,payment_no, expire_time, tele, order_uuid, pay_type, pay_time, pay_fee, discount_fee, mch_id, order_type, number,recommend_reward, recommend_type,  gym_id, sale_coach_id, sale_coach_status, new_order_status )  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
   #fangbaoziwei36_60
    args = (
        id1,price_code,all_times,subject_show_id, '0',deal_price, coins_pay, create_time1, '1', user_uuid, '1111',
        create_time3,
        '13810676427', uuid2, '1', create_time1, pay_fee, '0', '1', '0', '1', '0', '0', gym_id, sale_coach_id1, '1', '0')
    cursor.execute(sql, args)
    con.commit()

    #sql = 'insert into user_subject (id, subject_show_id, user_uuid, subject_id, create_time, order_uuid, type, leave_times, start_date, end_date, checkin_times, uuid, reward_uuid,all_times, use_times, expire_time, adjust_times, adjust_use_times, expire_type, is_charging,  free_type, is_expire, update_time, source_type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    #args1 = (id2, subject_show_id, user_uuid, 0, create_time1, uuid2, 0, 0, start_data, end_data, 0, uuid3, uuid4, 36, 0,
             #create_time2, 9, 0, 0, 0, 0, 0, create_time, 0)
    #cursor.execute(sql, args1)
    #con.commit()
def  add_order():
    data1 =f1.main()
    dingdan=f1.yongli(data1)#price_code,all_times,subject_show_id,deal_price,coins_pay,pay_fee,create_time1, create_time3,user_uuid
    #print(dingdan)
    for dingdan1 in dingdan:
        if dingdan1:
            price_code=dingdan1[0]
            all_times= dingdan1[1]
            subject_show_id = dingdan1[2]
            deal_price = dingdan1[3]
            coins_pay = dingdan1[4]
            pay_fee = dingdan1[5]
            create_time1= dingdan1[6]
            create_time3 = dingdan1[7]
            user_uuid = dingdan1[8]
            sale_coach_id=dingdan1[9]
            gym_id =dingdan1[10]
            sale_coach_id=sale_coach_id2(sale_coach_id)
            #delete(user_uuid)

            #print(sale_coach_id)
            time1=str(time.time())
            #user_uuid = 'b87112bf-7605-4941-9145-03eca62c61cb'
            gym_id =gym_id_get(gym_id)
            namespace = uuid.NAMESPACE_DNS
            namespace1 = uuid.NAMESPACE_URL
            namespace2 = uuid.NAMESPACE_OID
            # print(namespace)
            # print(namespace1)
            uuid2 = uuid.uuid3(namespace, user_uuid + time1)
            uuid3 = str(uuid.uuid3(namespace1, user_uuid + time1))
            uuid4 = str(uuid.uuid3(namespace2, user_uuid + time1))
            uuid2 = str(uuid2)
            # print(uuid2)
            uuid2 = uuid2.replace('-', '')


            uuid5 = get_subjectFB(uuid2, uuid3, uuid4,gym_id,price_code,all_times,subject_show_id,deal_price,coins_pay,pay_fee,create_time1, create_time3,user_uuid,sale_coach_id)
            print(uuid5)
        else:
            pass
def money_per(gym_id,month_at):
    sql='select coach_id,sale,private_sales,coins_pay from coach_month_rank where gym_id= \''+gym_id+'\'and month_at= \''+month_at+'\''
    cursor.execute(sql)
    id=cursor.fetchall()

    return id
def money_gym(gym_id,month_at):
    sql='select fee,mch_fee from gym_month_rank where gym_id= \''+gym_id+'\'and month_at= \''+month_at+'\''
    cursor.execute(sql)
    id=cursor.fetchall()
    if id :
        id = id[0]
    else:
       print('获取到的字段为空，报错，详情为:',id)
       sys.exit()


   # print(id)
    return id
def delete(user_uuid):
    sql = 'delete  FROM orders WHERE user_uuid=%s'
    cursor.execute(sql,user_uuid)
    sql = 'delete  FROM user_subject WHERE user_uuid=%s'
    cursor.execute(sql, user_uuid)
    con.commit()

def delete1(self, gym_id,create_time1):
     #self.get_classesId()
    create_time1 = '%' + create_time1 + '%'
    sql = 'delete  FROM orders WHERE sale_coach_id IN (SELECT id FROM coach WHERE gym_id=%s) AND create_time LIKE %s'
    cursor.execute(sql, (gym_id,create_time1))


    con.commit()
def income_money(create_time1,gym_id,sale_coach_id):
    create_time = '%'+ create_time1+'%'
    #print(create_time)
    sql='select sum(pay_fee) from user_order where sale_coach_id=%s and gym_id=%s and create_time like %s and status=1'
    cursor.execute(sql,(sale_coach_id,gym_id,create_time))
    id=cursor.fetchall()
    id=id[0][0]
    return id
if __name__ == '__main__':
    user_uuid=('15ce2e663df14a33946fab848a214494','ab2ce37b-daa2-43a1-8503-ea6db5462521')
    for useruuid in user_uuid:
       delete(useruuid)
    add_order()



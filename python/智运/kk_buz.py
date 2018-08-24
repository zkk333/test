import pymysql
import time
import warnings
warnings.filterwarnings('ignore')
try:

    con = pymysql.connect(host="101.201.142.45",
                          user="look",
                          password="LookForDev",
                          db="kk_buz",
                          port=33061,
                          charset='utf8')  # 连接数据库utf-8放进去报错，找了半天原因  ，只是在数据库中用utf8而已，就是指代一种编码
    cursor = con.cursor()
except:
    print('连接失败')
def role(coach):
    sql='select role_list from coach where id=%s'
    cursor.execute(sql,coach)
    role=cursor.fetchall()
    role=role[0][0]
    return role
def teach(coach_id,create_time):
    create_time='%'+create_time+'%'
    #print(create_time)
    sql='select average_score,class_times from coach_teach_count where coach_id=%s and create_time like %s'
    cursor.execute(sql,(coach_id,create_time))
    id=cursor.fetchall()
    return id
def teach_gym(gym_id,create_time):
    create_time='%'+create_time+'%'
    #print(create_time)
    sql='select average_score,class_times from coach_teach_count where gym_id=%s and create_time like %s'
    cursor.execute(sql,(gym_id,create_time))
    id=cursor.fetchall()
    return id
def old_coach(employment_date):
    sql='SELECT id FROM coach WHERE  employment_date<%s AND employment_date!=%s AND STATUS=1'
    cursor.execute(sql,(employment_date,''))
    id=cursor.fetchall()
    #print(id)
    return id
def old_gym(start_date):
    sql = 'SELECT id FROM gym WHERE  start_date<%s AND start_date!=%s AND STATUS=1'
    cursor.execute(sql, (start_date, ''))
    id = cursor.fetchall()
    # print(id)
    return id
def yejifencheng2(user_uuid):

    sql='SELECT price_code,create_time,sale_coach_id,all_times,coins_pay,pay_fee FROM orders WHERE  user_uuid=%s and status=1'
    cursor.execute(sql,user_uuid)
    id=cursor.fetchall()
    return id
def zs_dingdan(user_uuid):
    create_time1 = '2018-04'
    create_time1 = '%' + create_time1 + '%'
    sql='SELECT coins_pay,pay_fee FROM orders WHERE  user_uuid=%s and status=1  AND all_times>1 and create_time LIKE %s'
    cursor.execute(sql,(user_uuid,create_time1))
    id=cursor.fetchall()
    return id
def zs_xueyuan(coach_id):
    create_time1 = '2018-04'
    create_time1 = '%' + create_time1 + '%'
    sql='SELECT user_uuid FROM orders WHERE sale_coach_id=%s AND STATUS=1 AND all_times>1 AND create_time LIKE %s'
    cursor.execute(sql, (coach_id, create_time1))
    id = cursor.fetchall()
    return id
def tyxueyaun_wu(user_uuid):

    sql='select sale_coach_id,coins_pay,pay_fee,user_uuid,create_time from orders where user_uuid=%s AND STATUS=1 AND all_times=1'
    cursor.execute(sql, user_uuid)
    id = cursor.fetchall()
    return id
def tyxueyuan(coach_id):#6个自然月的体验课 在当月的正式课订单
    create_time='2017-11-01'
    price_code='jianzhity'
    price_code='%'+price_code+'%'
    #create_time='%'+create_time+'%'
    create_time1='2018-04'
    create_time1 = '%' + create_time1 + '%'
    sql = 'SELECT price_code,create_time,sale_coach_id,coins_pay,pay_fee,user_uuid FROM orders WHERE user_uuid IN (SELECT user_uuid FROM orders WHERE sale_coach_id=%s AND create_time>%s AND STATUS=1 AND price_code LIKE %s and subject_show_id=1) AND create_time LIKE %s AND STATUS=1 AND all_times>1 '
    cursor.execute(sql, (coach_id,create_time,price_code,create_time1))
    id = cursor.fetchall()
    return id
def user(coach_id):
    create_time = '2017-11-01 00:00:00'
    price_code = 'jianzhity'
    price_code = '%' + price_code + '%'
    #create_time1 = '%' + create_time + '%'
    #reate_time1 = '2018-03'
    #create_time1 = '%' + create_time1 + '%'
    sql='SELECT price_code,create_time FROM orders WHERE sale_coach_id=%s AND create_time > %s AND STATUS=1 AND price_code LIKE %s and subject_show_id=1'
    cursor.execute(sql, (coach_id, create_time, price_code))
    id = cursor.fetchall()
    return id
def subject_show_id(classesid):
    con.ping(reconnect=True)
    sql='select subject_show_id from classes where id=%s'
    cursor.execute(sql,classesid)
    id=cursor.fetchall()
    id=id[0][0]
    return id
def subject_show_id_course(coursecode):
    con.ping(reconnect=True)
    sql='select subject_show_id from classes where course_code=%s'
    cursor.execute(sql,coursecode)
    id=cursor.fetchall()
    id=id[0][0]
    return id

if __name__ == '__main__':
   # _create_time = time.localtime(time.time())
    #time.
   # create_time = time.strftime("%Y-%m", _create_time)
    a=old_gym('2017-12-01')
    print(a)


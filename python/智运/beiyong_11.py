import pymysql
import time
def dbconnect(db):
  try:

     con = pymysql.connect(host="192.168.40.233",
                          user="kk_stat",
                          password="kuaikuaikss_123",
                          db=db,
                          port=3306,
                          charset='utf8')  # 连接数据库utf-8放进去报错，找了半天原因  ，只是在数据库中用utf8而已，就是指代一种编码
     cursor = con.cursor()
     return cursor
  except:
      print('连接失败')
def gym_id(db,region_id):
    cursor=dbconnect(db)
    sql='select gym_id from region_gym where region_id=%s'
    cursor.execute(sql,region_id)
    id=cursor.fetchall()
    #print(id)

    return id
def gym_id_city(db,city_id):
    cursor=dbconnect(db)
    sql='select gym_id from region_gym where city_id=%s'
    cursor.execute(sql,city_id)
    id=cursor.fetchall()
    #print(id)

    return id
def gym_id_id(db,gym_id):
    cursor=dbconnect(db)
    sql='select id from gym where id=%s'
    cursor.execute(sql,gym_id)
    id=cursor.fetchall()
    #print(id)

    return id
def gym_coach_sale(db,gym_id,sale_time_1):
    cursor = dbconnect(db)
    sale_time1=sale_time(sale_time_1)
    sql = 'select sum(sale) from gym_coach_sale where gym_id=%s and sale_time like %s and price_code_type!=4'
    cursor.execute(sql, (gym_id,sale_time1))
    id = cursor.fetchall()
    id=id[0][0]
    if id:
        return id/100
    else:
        id=0
        return id

    #id=id/1000

    #return id
def gym_coach_sale1(db,gym_id,sale_time_1):
    cursor = dbconnect(db)
    sale_time1=sale_time(sale_time_1)
    sql = 'select sum(pay_fee) from gym_coach_sale where gym_id=%s and sale_time like %s and price_code_type=4'
    cursor.execute(sql, (gym_id,sale_time1))
    id = cursor.fetchall()
    id = id[0][0]
    if id:
        return id / 100
    else:
        id = 0
        return id
def ty_fee(db,gym_id,sale_time_1):
    cursor = dbconnect(db)
    sale_time1 = sale_time(sale_time_1)
    sql = 'select sum(pay_fee) from user_order where gym_id=%s and create_time like %s and price_code_type=1 and status=1'
    cursor.execute(sql, (gym_id, sale_time1))
    id = cursor.fetchall()
    id = id[0][0]
    if id:
        return id / 100
    else:
        id = 0
        return id
def orders(db,gym_id,sale_time_1):
    cursor = dbconnect(db)
    sale_time1 = sale_time(sale_time_1)
    sql = 'select sum(pay_fee) from user_order where gym_id=%s and create_time like %s  and status=1'
    cursor.execute(sql, (gym_id, sale_time1))
    id = cursor.fetchall()
    id = id[0][0]
    if id:
        return id / 100
    else:
        id = 0
        return id

def yinpin(db,gym_id,sale_time_1):
    cursor = dbconnect(db)
    sale_time1 = sale_time(sale_time_1)
    sql = 'select sum(pay_fee) from orders_merchandise where gym_id=%s and create_time like %s and status=1'
    cursor.execute(sql, (gym_id, sale_time1))
    id = cursor.fetchall()
    #id = id[0][0]
    id = id[0][0]
    if id:
        return id / 100
    else:
        id = 0
        return id
def sale_time(sale_time1):
   #sale_time='2018-05'
    sale_time='%'+sale_time1+'%'
    return sale_time
def shijian():
    create_time1=time.time()
    _create_time = time.localtime(create_time1)
    create_time = time.strftime("%Y-%m-%d", _create_time)
    return (create_time1,create_time)

def user_subject_free(db,classes_id):#不计费类型的课
    cursor = dbconnect(db)
    #create_time1 = '2018-05-01'
    #create_time2 = '2018-05-17'
    sql = 'select count(*) from user_subject  where uuid in (select user_subject_uuid from user_classes where classes_id=%s and status=0) and order_uuid=%s and is_charging=0'
    cursor.execute(sql, (classes_id,''))
    id = cursor.fetchall()
    try:
        id = id[0][0]
    except IndexError:
        print('erro')
        print(classes_id)
    return id

def user_subject(db,classes_id):
    cursor = dbconnect(db)
    #create_time1 = '2018-05-01'
    #create_time2 = '2018-05-17'
    sql = 'select count(*) from user_subject  where uuid in (select user_subject_uuid from user_classes where classes_id=%s and status=0 ) '
    cursor.execute(sql, classes_id)
    id = cursor.fetchall()
    try:
        id = id[0][0]
    except IndexError:
        print('erro')
        print(classes_id)
    return id
def classes_capacity(db,classes_id):
    cursor = dbconnect(db)
    # create_time1 = '2018-05-01'
    # create_time2 = '2018-05-17'
    sql = 'select capacity from classes where id=%s '
    cursor.execute(sql, classes_id)
    id = cursor.fetchall()
    try:
      id = id[0][0]
    except IndexError:
        print('erro')
        print(classes_id)

    return id
def classes_capacity_sj(db,classes_id):
    cursor = dbconnect(db)
    create_time1 = '2018-05-01'
    create_time2 = '2018-05-25'
    sql = 'select capacity from classes where gym_id=%s and start_time>=%s and start_time<=%s and subject_show_id=3  and has_cancel=0'
    cursor.execute(sql, (classes_id,create_time1,create_time2))
    id = cursor.fetchall()
    try:
        id = id[0][0]
    except IndexError:
        print('erro')
        print(classes_id)
    return id
def classes_id(db,gym_id):
    cursor = dbconnect(db)
    create_time1='2018-05-01'
    create_time2='2018-05-25'
    sql = 'select id from classes where gym_id=%s and start_time>=%s and start_time<=%s and subject_show_id!=3 and has_cancel=0'
    cursor.execute(sql, (gym_id,create_time1,create_time2))
    id = cursor.fetchall()
    #id = id[0][0]

    return id
def classes_id_ranzhi(db,gym_id):
    cursor = dbconnect(db)
    create_time1='2018-05-01'
    create_time2='2018-05-25'
    sql = 'select id from classes where gym_id=%s and start_time>=%s and start_time<=%s and subject_show_id=1 and has_cancel=0'#hascacel=0 该节课正常
    cursor.execute(sql, (gym_id,create_time1,create_time2))
    id = cursor.fetchall()
    #id = id[0][0]

    return id
def gym_id1(db):
    cursor = dbconnect(db)
    sql = 'select id from gym where status=1'
    cursor.execute(sql)
    id = cursor.fetchall()
    # print(id)

    return id
def ty_money(db,gym_id,sale_time_1):
    cursor = dbconnect(db)
    sale_time1 = sale_time(sale_time_1)
    sql = 'select sum(pay_fee) from user_order where gym_id=%s and create_time like %s  and status=1 and price_code_type=1'
    cursor.execute(sql, (gym_id, sale_time1))
    id = cursor.fetchall()
    id = id[0][0]
    if id:
        return id / 100
    else:
        id = 0
        return id
def sijiao_money(db,gym_id,sale_time_1):
    cursor = dbconnect(db)
    sale_time1 = sale_time(sale_time_1)
    sql = 'select sum(pay_fee) from user_order where gym_id=%s and create_time like %s  and status=1 and price_code_type=4'
    cursor.execute(sql, (gym_id, sale_time1))
    id = cursor.fetchall()
    id = id[0][0]
    if id:
        return id / 100
    else:
        id = 0
        return id
def zhengshike(db,gym_id,sale_time_1):
    cursor = dbconnect(db)
    sale_time1 = sale_time(sale_time_1)
    sql = 'select sum(sale) from gym_coach_sale where gym_id=%s and sale_time like %s  and price_code_type!=4'
    cursor.execute(sql, (gym_id, sale_time1))
    id = cursor.fetchall()
    id = id[0][0]
    if id:
        return id / 100
    else:
        id = 0
        return id
if __name__ == '__main__':
    print( classes_capacity('kk_buz','259'))
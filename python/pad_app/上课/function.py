
import  pymysql
import requests
import re
import time
import uuid
import random
import string
import warnings
import 智运.kk_buz as  kk_buz
import multiprocessing

import pad_app.上课.db_connect as f2
warnings.filterwarnings('ignore')


# coding: UTF-8
#单次课程

#input('想要上的课程'%name)
    #global  id1
'''
try:
    a=int(input('请输入1，代表测试环境。2代表廊坊环境'))
    con=f2.db_test(a)
    cursor=con.cursor()
except AttributeError:
    exit()
'''

try:

    con = pymysql.connect(host="192.168.41.20",
                          user="kms",
                          password="kuaikuaikms",
                          db="kk_test",
                          port=33061,
                          charset='utf8',
                          connect_timeout=6000)  # 连接数据库utf-8放进去报错，找了半天原因  ，只是在数据库中用utf8而已，就是指代一种编码
    # ursor = con.cursor()
    cursor=con.cursor()


except:
    print('连接失败')  # 测试环境
class A():
 def __init__(self,coachId):#实例化方法，必须有，但是里面是啥就无所谓了，可有可无
     self.coachId=coachId
 def coursecode(self,classesid):
     sql='SELECT course_code FROM  classes WHERE id=%s '
     cursor.execute(sql,classesid)
     id=cursor.fetchall()
     id=id[0][0]
     return id
 def user(self):




     sql = 'SELECT *FROM user_report limit 0,500'

     cursor.execute(sql)

     return self

 def get_subjectid_by_id(self,classesid):
     sql = 'SELECT subject_id FROM  classes WHERE id=%s '
     cursor.execute(sql, classesid)
     id = cursor.fetchall()
     id = id[0][0]
     return id
 def user_name_pwd(self):
     sql='SELECT tel,psd FROM coach where status=1 limit 0,20'
     cursor.execute(sql)
     id=cursor.fetchall()
     id=id
     return id

 def classes_number(self,classesid):
     sql='SELECT count(*) FROM  user_classes_checkin WHERE classes_id=%s '
     cursor.execute(sql,classesid)
     id=cursor.fetchall()
     id=id[0][0]
     return id
 def get_gymid(self,coachId):
 #a=str(self.coachId)

    con.ping(reconnect=True)

    sql = "SELECT gym_id FROM  coach WHERE id=%s"  # 参数化，防止sql攻击
    cursor.execute(sql,coachId)

    gym_id = cursor.fetchone()
    gym_id = gym_id[0]  # 本来指望正则表达式实现的，结果正则看了会 没看懂
    con.commit()

    # print(gym_id)
    return  gym_id
 def get_gymid_name(self,name1):
     sql='select id from gym where name like \'%' + name1+ '%\''
     cursor.execute(sql)
     gym_id=cursor.fetchall()
     con.commit()
     return gym_id
 def get_uuid_code(self,user_code):
     sql = 'select uuid from user where user_code=%s'
     cursor.execute(sql,user_code)
     id=cursor.fetchone()
     id=id[0]
     con.commit()
     return id
 def get_subjectId(self,gym_id):
    #self.gym_id=gym_id
    con.ping(reconnect=True)
    sql = "SELECT id FROM subject WHERE gym_id=%s "
    cursor.execute(sql, (gym_id))
    subject_id = cursor.fetchone()
    subject_id = subject_id[0]
    con.commit()

    return subject_id
    # print(subject_id1)
 def get_classesId(self):
    con.ping(reconnect=True)

    sql = "select max(id)+1 from classes"

    cursor.execute(sql)
    id = cursor.fetchall()
    id1 = id[0][0]

    con.commit()

    return id1
 def useruuid(self):
     useruuid= [

         '2bf935fa-bf21-4d8d-8c4a-0d1d6db5af9d',

         'e3890058-8af7-470f-9687-42274957371b',
         '772d3968-d5ab-4ea9-9668-8232d8066508',

         '4c73f62e-50df-4504-9a7a-925bcc2c7101',
      'ecbd60c2-c40f-49cc-aef7-fe62f947178d',
      '1288c6c5-e5c1-4919-a774-246903cee842',
      '3e4d6e11-bb41-4ec9-b2f5-75c4d8b93ab0',
      '3588e0f6-da85-475d-9654-643f26e2d905',
      '915ab89d-4e86-48ae-b0bd-9b0212525d55',
      'd1aaa4cc-306f-472a-ae09-da32d32b18f3',

      '502623a7-8ce9-45ba-a6c4-60023f2d2500',
      '90a723e4-6f1d-4b14-b4b6-a716f00a5e64',
      '54e91942-3363-45da-9135-ef95cca864c7',
      '07ce018b-e4e8-4654-9a1f-0fe8e640b368',
      '3cada9f2-85cc-46be-a2b5-9b3a03276263',
      'f2cfb74b-e593-4a02-bdd3-49d09ef60ed1',
      '602f5ea2-aba3-4581-8687-fbe59a06e638']
     return useruuid

 def useruuid_private(self):
     useruuid = [
         'ba323c49-2830-4dae-809f-ca450101e31d',

         'bc03b028-dbc5-485a-9c7a-b984428e12aa',


                 ]
     return useruuid
 def get_coachId(self,tel):
     sql='select id from coach where tel=%s'
     #args=(tel)
     cursor.execute(sql,tel)
     coachId=cursor.fetchall()
     coachId=coachId[0][0]
     return coachId

 def get_course_code(self,user_uuid):
     sql='select type from user_personal_subject where user_uuid=%s'
     cursor.execute(sql,user_uuid)
     course_code=cursor.fetchall()
     course_code=course_code[0][0]
     return course_code

 def get_course_code_usetimes(self, user_uuid):
     sql = 'select circle_times from user_personal_subject where user_uuid=%s'
     cursor.execute(sql, user_uuid)
     circle_times= cursor.fetchall()
     circle_times = circle_times[0][0]
     return  circle_times

 def get_tel_gymId(self,tel ):
     sql = 'select gym_id from coach where tel=%s'
     # args=(tel)
     cursor.execute(sql, tel)
     gym_id = cursor.fetchall()
     gym_id = gym_id[0][0]
     return gym_id
 #def updata
 def get_orders_id(self):
     sql = 'select max(id)+1 from orders '
     cursor.execute(sql)
     id1 = cursor.fetchall()
     id1 = id1[0][0]
     return id1
 def get_user_subject_id(self):
     sql = 'select max(id)+1 from user_subject '
     cursor.execute(sql)
     id2 = cursor.fetchall()
     id2 = id2[0][0]
     return id2
 def get_course_code_private_num(self,user_uuid):
     n = self.get_course_code_usetimes(user_uuid)
     while 1:
         if n > 16:
             n = n - 16
             if n < 16:
                 n=n
                 break
         else:
             n=n
             break




     return n

 def get_subject(self,uuid2,uuid3,uuid4,user_uuid):
     #user_uuid=self.useruuid()
     #for user_uuid in user_uuid:
       a=D()
       payment=a.payment()

       con.ping(reconnect=True)
       #user_uuid = '492a685f-16a4-40c0-a0a3-17dec392c9bd'
       sql = 'select uuid from user_subject where user_uuid=\''+user_uuid+'\' and all_times-use_times>0'
       cursor.execute(sql)
       uuid11=cursor.fetchone()
       #print(uuid1)
       #_uuid1=cursor.fetchone()#获取有课的课程第一条uuid
       #print(_uuid1)
       #uuid1=uuid1[0]
       #print(uuid11)
       if (uuid11):

            uuid11=uuid11[0]
            #print(uuid11)

           #pass
       else:

           _create_time = time.localtime(time.time() - 3600)
           create_time = time.strftime("%Y-%m-%d %H:%M:%S", _create_time)
           start_data = time.strftime("%Y-%m-%d", _create_time)
           # end_data = time.strftime("%Y-%m-%d", _create_time)
           _create_time1 = time.localtime(time.time() - 3600 + 600)
           create_time1 = time.strftime("%Y-%m-%d %H:%M:%S", _create_time1)
           _create_time2 = time.localtime(time.time() - 3600 + 365 * 24 * 3600)
           create_time2 = time.strftime("%Y-%m-%d %H:%M:%S", _create_time2)

           end_data = time.strftime("%Y-%m-%d", _create_time2)
           con.ping(reconnect=True)
           sql = 'insert ignore into orders ( price_code, all_times, subject_show_id, subject_id, deal_price, coins_pay, create_time, status, user_uuid,payment_no, expire_time, tele, order_uuid, pay_type, pay_time, pay_fee, discount_fee, mch_id, order_type, number,recommend_reward, recommend_type,  gym_id, sale_coach_id, sale_coach_status, new_order_status )  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
           args = (
            'jianzhi240', '240', '1', '0', '19200', '1920000', create_time, '1', user_uuid, payment, create_time1,
           '15234118888', uuid2, '1', create_time, '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0')

           cursor.execute(sql, args)
           con.commit()
           con.ping(reconnect=True)
           sql = 'insert ignore into user_subject (subject_show_id, user_uuid, subject_id, create_time, order_uuid, type, leave_times, start_date, end_date, checkin_times, uuid, reward_uuid,all_times, use_times, expire_time, adjust_times, adjust_use_times, expire_type, is_charging,  free_type, is_expire, update_time, source_type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
           args1 = (1, user_uuid, 0, create_time, uuid2, 0, 0, start_data, end_data, 0, uuid3, uuid4, 240, 0,
                    create_time2, 60, 0, 0, 0, 0, 0, create_time, 0)

           cursor.execute(sql, args1)
           con.commit()
           uuid11=uuid3
          # print(uuid11)
           #cursor.close()
           #return  uuid33

       return uuid11

 def get_subjectFB(self, uuid2, uuid3, uuid4, user_uuid):
     # user_uuid=self.useruuid()
     # for user_uuid in user_uuid:

         a = D()
         payment = a.payment()
     # user_uuid = '492a685f-16a4-40c0-a0a3-17dec392c9bd'

         id1 = self.get_orders_id()
         id2 = self.get_user_subject_id()
         _create_time = time.localtime(time.time() - 3600)
         create_time = time.strftime("%Y-%m-%d %H:%M:%S", _create_time)
         start_data = time.strftime("%Y-%m-%d", _create_time)
         # end_data = time.strftime("%Y-%m-%d", _create_time)
         _create_time1 = time.localtime(time.time() - 3600 + 600)
         create_time1 = time.strftime("%Y-%m-%d %H:%M:%S", _create_time1)
         _create_time2 = time.localtime(time.time() - 3600 + 365 * 24 * 3600)
         create_time2 = time.strftime("%Y-%m-%d %H:%M:%S", _create_time2)

         end_data = time.strftime("%Y-%m-%d", _create_time2)

         sql = 'insert into orders (id, price_code, all_times, subject_show_id, subject_id, deal_price, coins_pay, create_time, status, user_uuid,payment_no, expire_time, tele, order_uuid, pay_type, pay_time, pay_fee, discount_fee, mch_id, order_type, number,recommend_reward, recommend_type,  gym_id, sale_coach_id, sale_coach_status, new_order_status )  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

         args = (
             id1, 'fangweiboji24_60', '36', '4', '0', '3398', '339800', create_time, '1', user_uuid, payment,
             create_time1,
             '15234118888', uuid2, '1', create_time, '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0')
         cursor.execute(sql, args)
         con.commit()

         sql = 'insert into user_subject (id, subject_show_id, user_uuid, subject_id, create_time, order_uuid, type, leave_times, start_date, end_date, checkin_times, uuid, reward_uuid,all_times, use_times, expire_time, adjust_times, adjust_use_times, expire_type, is_charging,  free_type, is_expire, update_time, source_type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

         args1 = (id2, 4, user_uuid, 0, create_time, uuid2, 0, 0, start_data, end_data, 0, uuid3, uuid4, 36, 0,
                  create_time2, 9, 0, 0, 0, 0, 0, create_time, 0)
         cursor.execute(sql, args1)
         con.commit()

 def get_chengwei(self, uuid2,uuid4,uuid5,user_uuid,price,price1):
     # user_uuid=self.useruuid()
     # for user_uuid in user_uuid:

     a = D()
     payment = a.payment()
     # user_uuid = '492a685f-16a4-40c0-a0a3-17dec392c9bd'

     id1 = self.get_orders_id()
     id2 = self.get_user_subject_id()
     _create_time = time.localtime(time.time())
     create_time = time.strftime("%Y-%m-%d %H:%M:%S", _create_time)
     start_data = time.strftime("%Y-%m-%d", _create_time)
     # end_data = time.strftime("%Y-%m-%d", _create_time)
     _create_time1 = time.localtime(time.time()+ 600)
     create_time1 = time.strftime("%Y-%m-%d %H:%M:%S", _create_time1)
     _create_time2 = time.localtime(time.time() - 3600 + 50*365 * 24 * 3600)
     create_time2 = time.strftime("%Y-%m-%d %H:%M:%S", _create_time2)

     end_data = time.strftime("%Y-%m-%d", _create_time2)

     sql = 'insert into orders (id, price_code, all_times, subject_show_id, subject_id, deal_price, coins_pay, create_time, status, user_uuid,payment_no, expire_time, tele, order_uuid, pay_type, pay_time, pay_fee, discount_fee, mch_id, order_type, number,recommend_reward, recommend_type,  gym_id, sale_coach_id, sale_coach_status, new_order_status )  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

     args = (
         id1, 'private', '0', '3', '0', price, '0', create_time, '1', user_uuid, payment,
         create_time1,
         '15234118888', uuid2, '1', create_time, price1, '0', '1', '0', '1', '0', '0', '0', '0', '0', '0')
     cursor.execute(sql, args)
     con.commit()
     sql='insert into `user_coins` ( `uuid`,`user_uuid`, `coins`, `create_time`, `expire_time`, `type`, `order_uuid`, `sub_type`) values(%s,%s,%s,%s,%s,%s,%s,%s)'
     args=(uuid4,user_uuid,price1,create_time, create_time2,0,uuid2,0)
     cursor.execute(sql,args)
     con.commit()
     sql='insert into `user_coins_consume_log` ( `uuid`, `user_uuid`, `coins`, `create_time`, `type`, `sub_type`, `classes_id`) values(%s,%s,%s,%s,%s,%s,%s)'
     args=(uuid5,user_uuid,price1,create_time,0,0,0)
     cursor.execute(sql,args)
     con.commit()



 def addclass_private(self,coachId,user_uuid1):
    gym_id=self.get_gymid(coachId)
    #subject_id=self.get_subjectId(gym_id)

    course_code = self.get_course_code(user_uuid1)#相当于加了一节同类型的私教课
    n2 = str(self.get_course_code_private_num(user_uuid1)+1)
    course_code = course_code + n2
    id1=self.get_classesId()

    start_time1 = time.localtime(time.time())
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_time1)
     # print(start_time)
    end_time1 = time.localtime(time.time()+3600)
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_time1)
    n1 = int(input('拼课的人数:'))
    if n1 <= 2:
    # print(end_time)
      sql = " INSERT INTO classes(id, subject_show_id, subject_id, course_code, gym_id, room_id, coach_id, start_time, end_time, status, type, capacity, enroll_number, bind_coach, has_cancel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # SQL语句只能放在同一行
    # gym_id=re.compile(r'-?[1-9]\d*　').findall(id)
      args = (id1, 3, 0,course_code, gym_id, 0, 0, start_time, end_time, 0, 1, 3, 0, 0, 0)
      cursor.execute(sql, args)
      con.commit()
    #classesadd = cursor.fetchall()  # 加课

      useruuid=self.useruuid_private()




      useruuid1=useruuid[0:n1]
      user_uuid1=user_uuid1.split()
      useruuid1=user_uuid1+useruuid1
    #print(useruuid1)
      for user_uuid in useruuid1:
        course_code = self.get_course_code(user_uuid)

        sql = 'select max(id)+1 from user_classes'
        cursor.execute(sql)
        id = cursor.fetchall()
        id = id[0][0]
        classes_id = id1
        usetimes=self.get_course_code_usetimes(user_uuid)+1
        usetimes=str(usetimes)
        sql = 'update user_personal_subject set circle_times=\'' + usetimes + '\' where user_uuid=\'' + user_uuid + '\''  # 加完课后跟新user_subject里面use_times字段
        cursor.execute(sql)
        con.commit()

        n3=str(self.get_course_code_private_num(user_uuid)) #转化成字符型 不用管之前是啥类型
        course_code1=course_code+n3



      #cursor.execute(sql)

  # id=str()
      #print(uuid5)
        creata_time1 = time.localtime(time.time() - 3600 * 24)
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", creata_time1)

        sql = "insert into user_classes (id, subject_id, user_uuid, classes_id, classes_type, status, create_time, leave_type, user_subject_uuid, classes_times, course_code, has_checkin) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        args1 = (
        id, 0, user_uuid, classes_id, 1, 0, create_time, 0,0, usetimes, course_code1,0)
        cursor.execute(sql, args1)
        con.commit()

      #cursor.close()
      n=input('需要签到的人数：')
      n=int(n)
      if n <=len(useruuid1):
        for user_uuid in useruuid1[0:n]:






#print(classsupdate1)

         sql='select max(id)+1 from user_classes_checkin'
         cursor.execute(sql)
         id=cursor.fetchall()
         id=id[0][0]
         creata_time1=time.localtime(time.time()-1200)
         create_time=time.strftime("%Y-%m-%d %H:%M:%S",creata_time1)
         sql='insert into user_classes_checkin (id,user_uuid,classes_id,create_time,status,type,coach_id) values (%s,%s,%s,%s,%s,%s,%s)'
         args2=(id,user_uuid,id1,create_time,1,0,0)
         cursor.execute(sql,args2)
         con.commit()


      else :
        print('签到人数多于上课人数，该节课为空')
    else:
        print('最多只允许俩人拼课')




    cursor.close()
    con.close()
 def course_code(self):
     self

 def addclass(self, coachId):
     gym_id = self.get_gymid(coachId)
     subject_id = self.get_subjectId(gym_id)
     id1 = self.get_classesId()
     print(id1)

     start_time1 = time.localtime(time.time()+3600*24*0)
     start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_time1)
     # print(start_time)
     end_time1 = time.localtime(time.time()+3600*24*0 + 3600)
     end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_time1)
     # print(end_time)
     sql = " INSERT INTO classes(id, subject_show_id, subject_id, course_code, gym_id, room_id, coach_id, start_time, end_time, status, type, capacity, enroll_number, bind_coach, has_cancel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
     # SQL语句只能放在同一行
     # gym_id=re.compile(r'-?[1-9]\d*　').findall(id)
     args = (id1,9, subject_id,'JXSXBJ1.0.1.1', gym_id, 0, 0, start_time, end_time, 0, 1, 12, 0, 0, 0)
     cursor.execute(sql, args)
     con.commit()
     # classesadd = cursor.fetchall()  # 加课

     useruuid = self.useruuid()
     n1 = int(input('上课人数:'))
     useruuid1 = useruuid[0:n1]
     # print(useruuid1)
     for user_uuid in useruuid1:
         sql = 'select max(id)+1 from user_classes'
         cursor.execute(sql)
         id = cursor.fetchall()
         id = id[0][0]
         classes_id = id1

         time1 = str(time.time())
         # name = user_uuid
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
         '''
         uuid2 = str(uuid.uuid1())
         uuid2 = uuid2.replace('-', '')

         time.sleep(1)
         uuid3 = uuid.uuid1()
         uuid3 = str(uuid3)
         time.sleep(2)
         uuid4 = uuid.uuid1()
         uuid4 = str(uuid4)
         '''
         uuid5 = self.get_subject(uuid2, uuid3, uuid4, user_uuid)

         # cursor.execute(sql)

         # id=str()
         # print(uuid5)
         creata_time1 = time.localtime(time.time() - 3600 * 24)
         create_time = time.strftime("%Y-%m-%d %H:%M:%S", creata_time1)
         sql = 'select use_times from user_subject where uuid=%s'
         cursor.execute(sql, uuid5)
         con.commit()
         usetimes = cursor.fetchone()
         usetimes = usetimes[0] + 1
         sql = "insert into user_classes (id, subject_id, user_uuid, classes_id, classes_type, status, create_time, leave_type, user_subject_uuid, classes_times, course_code, has_checkin) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
         args1 = (
             id, subject_id, user_uuid, classes_id, 1, 0, create_time, 0, uuid5, usetimes, 'JZX2.0.4.1', 0)
         cursor.execute(sql, args1)
         con.commit()
         usetimes = str(usetimes)
         uuid5 = str(uuid5)
         sql = 'update user_subject set use_times=\'' + usetimes + '\' where uuid=\'' + uuid5 + '\''  # 加完课后跟新user_subject里面use_times字段
         cursor.execute(sql)
         con.commit()
         # cursor.close()
     n = input('需要签到的人数：')
     n = int(n)
     if n <= len(useruuid1):
         for user_uuid in useruuid1[0:n]:
             # print(classsupdate1)

             sql = 'select max(id)+1 from user_classes_checkin'
             cursor.execute(sql)
             id = cursor.fetchall()
             id = id[0][0]
             creata_time1 = time.localtime(time.time() - 1200)
             create_time = time.strftime("%Y-%m-%d %H:%M:%S", creata_time1)
             sql = 'insert into user_classes_checkin (id,user_uuid,classes_id,create_time,status,type,coach_id) values (%s,%s,%s,%s,%s,%s,%s)'
             args2 = (id, user_uuid, id1, create_time, 1, 0, 0)
             cursor.execute(sql, args2)
             con.commit()


     else:
         print('签到人数多于上课人数，该节课为空')

     cursor.close()
     con.close()
 def add_classes_more(self,coachId,n,cn,subject_show_id):
   gym_id = self.get_gymid(coachId)
   subject_id = self.get_subjectId(gym_id)
   id = []
   for n1 in range(0,n):

     id1 = self.get_classesId()
     start_time1 = time.localtime(time.time()-n1*1500)
     start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_time1)
     # print(start_time)
     end_time1 = time.localtime(time.time()-n1*1500+ 3600)
     end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_time1)
     # print(end_time)
     if subject_show_id==4 and cn<37 and cn>0:
       cn1=str(cn)
       course_code='FB.1.0.1.'
       coursecode=course_code+cn1


       sql = " INSERT INTO classes(id, subject_show_id, subject_id, course_code, gym_id, room_id, coach_id, start_time, end_time, status, type, capacity, enroll_number, bind_coach, has_cancel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
     # SQL语句只能放在同一行
     # gym_id=re.compile(r'-?[1-9]\d*　').findall(id)
       args = (id1, subject_show_id, subject_id, coursecode, gym_id, 0, 0, start_time, end_time, 0, 1, 12, 0, 0, 0)
       cursor.execute(sql, args)
       con.commit()
       id.append(id1)
     elif subject_show_id==1 and cn<13 and cn>0:
         cn1 = str(cn)
         course_code = 'JZX2.0.4.'
         coursecode = course_code+cn1

         sql = " INSERT INTO classes(id, subject_show_id, subject_id, course_code, gym_id, room_id, coach_id, start_time, end_time, status, type, capacity, enroll_number, bind_coach, has_cancel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
         # SQL语句只能放在同一行
         # gym_id=re.compile(r'-?[1-9]\d*　').findall(id)
         args = (id1, subject_show_id, subject_id, coursecode, gym_id, 0, 0, start_time, end_time, 0, 1, 12, 0, 0, 0)
         cursor.execute(sql, args)
         con.commit()
         id.append(id1)


     else:
         print('课程节数不存在')
   return id

     # classesadd = cursor.fetchall()  # 加课
 def add_add_classes_more1(self,coachId,n,cn,subject_show_id):
   classes_id=self.add_classes_more(coachId,n,cn,subject_show_id)
   gym_id = self.get_gymid(coachId)
   subject_id = self.get_subjectId(gym_id)
   useruuid = self.useruuid()
   n1 = int(input('上课人数:'))
   n2 = input('需要签到的人数：')
   for classes_id in classes_id:
     useruuid1 = useruuid[0:n1]
     # print(useruuid1)
     for user_uuid in useruuid1:
         sql = 'select max(id)+1 from user_classes'
         cursor.execute(sql)
         id = cursor.fetchall()
         id = id[0][0]
         #classes_id = id1

         time1 = str(time.time())
         # name = user_uuid
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
         '''
         uuid2 = str(uuid.uuid1())
         uuid2 = uuid2.replace('-', '')

         time.sleep(1)
         uuid3 = uuid.uuid1()
         uuid3 = str(uuid3)
         time.sleep(2)
         uuid4 = uuid.uuid1()
         uuid4 = str(uuid4)
         '''
         uuid5 = self.get_subject(uuid2, uuid3, uuid4, user_uuid)

         # cursor.execute(sql)

         # id=str()
         #print(uuid5)
         creata_time1 = time.localtime(time.time() - 3600 * 24)
         create_time = time.strftime("%Y-%m-%d %H:%M:%S", creata_time1)
         sql = 'select use_times from user_subject where uuid=%s'
         cursor.execute(sql, uuid5)
         con.commit()
         usetimes = cursor.fetchone()
         usetimes = usetimes[0] + 1
         sql = "insert into user_classes (id, subject_id, user_uuid, classes_id, classes_type, status, create_time, leave_type, user_subject_uuid, classes_times, course_code, has_checkin) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
         args1 = (
             id, subject_id, user_uuid, classes_id, 1, 0, create_time, 0, uuid5, usetimes, 'JZX2.0.4.1', 0)
         cursor.execute(sql, args1)
         con.commit()
         usetimes = str(usetimes)
         uuid5 = str(uuid5)
         sql = 'update user_subject set use_times=\'' + usetimes + '\' where uuid=\'' + uuid5 + '\''  # 加完课后跟新user_subject里面use_times字段
         cursor.execute(sql)
         con.commit()
         # cursor.close()

     n2 = int(n2)
     if n2 <= len(useruuid1):
         for user_uuid in useruuid1[0:n2]:
             # print(classsupdate1)

             sql = 'select max(id)+1 from user_classes_checkin'
             cursor.execute(sql)
             id = cursor.fetchall()
             id = id[0][0]
             creata_time1 = time.localtime(time.time() - 1200)
             create_time = time.strftime("%Y-%m-%d %H:%M:%S", creata_time1)
             sql = 'insert into user_classes_checkin (id,user_uuid,classes_id,create_time,status,type,coach_id) values (%s,%s,%s,%s,%s,%s,%s)'
             args2 = (id, user_uuid,classes_id, create_time, 1, 0, 0)
             cursor.execute(sql, args2)
             con.commit()


     else:
         print('签到人数多于上课人数，该节课为空')

   cursor.close()
   con.close()




 def addclass1(self, coachId,n,course_code):
         con.ping(reconnect=True)
         gym_id = self.get_gymid(coachId)
        # print('haha')
        # print(course_code)

         subject_show_id=kk_buz.subject_show_id_course(course_code)#根据现网classid获取该节课的subject_show_id  跳转到现网sql查询语句里
        # print(subject_show_id)


         #print(subject_show_id)
         subject_id = self.get_subjectId(gym_id)
         id1 = self.get_classesId()


         start_time1 = time.localtime(time.time()-300)#开课时间
         start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_time1)
         # print(start_time)
         end_time1 = time.localtime(time.time()-300+ 3600)#课程结束时间
         end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_time1)
         # print(end_time)
         sql = " INSERT  INTO classes(id,subject_show_id, subject_id, course_code, gym_id, room_id, coach_id, start_time, end_time, status, type, capacity, enroll_number, bind_coach, has_cancel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
         # SQL语句只能放在同一行
         # gym_id=re.compile(r'-?[1-9]\d*　').findall(id)
         args = (id1,subject_show_id, subject_id,course_code, gym_id, 0, 0, start_time, end_time, 0, 1, 12, 0, 0, 0)

         cursor.execute(sql, args)
         con.commit()

         # classesadd = cursor.fetchall()  # 加课
         #print('nongshane')
         useruuid = self.useruuid()
         #n1 = int(input('上课人数:'))
         useruuid1 = useruuid[0:n]
         #print(useruuid1)
         for user_uuid in useruuid1:
             #sql = 'select max(id)+1 from user_classes'
            # cursor.execute(sql)
             #id = cursor.fetchall()
           # id = id[0][0]
             classes_id = id1

             time1 = str(time.time())
             # name = user_uuid
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

             # cursor.execute(sql)
             uuid5 = self.get_subject(uuid2, uuid3, uuid4, user_uuid)
             # id=str()
             #print(uuid5)
             con.ping(reconnect=True)
             creata_time1 = time.localtime(time.time() - 3600 * 24)
             create_time = time.strftime("%Y-%m-%d %H:%M:%S", creata_time1)
             '''
             sql = 'select use_times from user_subject where uuid=%s'
             cursor.execute(sql, uuid5)
             con.commit()
             usetimes = cursor.fetchone()
             usetimes = usetimes[0] + 1
              '''
             con.ping(reconnect=True)
             sql = "insert into  user_classes (subject_id, user_uuid, classes_id, classes_type, status, create_time, leave_type, user_subject_uuid, classes_times, course_code, has_checkin) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
             args1 = (
                subject_id, user_uuid, classes_id, 1, 0, create_time, 0, uuid5, 9, course_code, 0)#usetimes
             cursor.execute(sql, args1)
             con.commit()
             con.ping(reconnect=True)
             '''
             usetimes = str(usetimes)

             uuid5 = str(uuid5)

             sql = 'update user_subject set use_times=\'' + usetimes + '\' where uuid=\'' + uuid5 + '\''  # 加完课后跟新user_subject里面use_times字段
             cursor.execute(sql)
             con.commit()
             '''
            # print('nongshane1')
             # cursor.close()
         #n = input('需要签到的人数：')
         #n = int(n)





                 # print(classsupdate1)
             #print('nongshane2')

               #  sql = 'select max(id)+1 from user_classes_checkin'
                # cursor.execute(sql)
                # id = cursor.fetchall()
                 #id = id[0][0]
             con.ping(reconnect=True)
             creata_time1 = time.localtime(time.time() - 1200)
             create_time = time.strftime("%Y-%m-%d %H:%M:%S", creata_time1)
             sql = 'insert  into user_classes_checkin (user_uuid,classes_id,create_time,status,type,coach_id) values (%s,%s,%s,%s,%s,%s)'
             args2 = ( user_uuid, id1, create_time, 1, 0, 0)
             cursor.execute(sql, args2)
             con.commit()
            # print('nongshane3')




         return  id1
         cursor.close()
         con.close()


 def get_everyday_classesId(self,gym_id):
     start_time=str(input('上课时间格式2017-12-15'))



     sql='select id from classes where gym_id= \''+gym_id+'\' and start_time like \'%' + start_time+ '%\''
     cursor.execute(sql)
     _class_id=cursor.fetchall()
     return _class_id
 def isdelete(self,_class_id):#按classid进行删除课程
    if isinstance(_class_id,str):#判断是否是字符串
         self.delete(_class_id)
         #print(1)
    else:
      for _class_id in _class_id:
          self.delete(_class_id)
         # print(2)

 def get_time_classesId(self, gym_id):
     start_time = str(input('开始时间格式2017-12-15 11:00:00'))
     end_time= str(input('结束时间格式2017-12-15 11:00:00'))

     sql = 'select id from classes where gym_id= \'' + gym_id + '\' and start_time>\'' + start_time + '\' and end_time<\'' + end_time + '\''
     cursor.execute(sql)
     _class_id = cursor.fetchall()
     return _class_id

 def get_user_uuid_classesId(self, user_uuid):
     start_time = str(input('创建课程时间格式2017-12-15 '))#造课的时间比本地时间小一天

     sql = 'select classes_id from user_classes where user_uuid= \'' + user_uuid + '\' and create_time>\'' + start_time + '\' '#like \'%' + start_time+ '%\'
     cursor.execute(sql)
     _class_id = cursor.fetchall()
     return _class_id


 def delete(self, _class_id):
     #self.get_classesId()
    sql = 'delete from classes where id=%s'
    cursor.execute(sql, (_class_id))
    sql = 'delete from user_classes where classes_id=%s'
    cursor.execute(sql, (_class_id))
    sql = 'delete from user_classes_checkin where classes_id=%s'
    cursor.execute(sql, (_class_id))
    sql='delete from user_class_data where class_id=%s'
    cursor.execute(sql,_class_id)
    sql='delete from user_report where classes_id=%s'
    cursor.execute(sql, _class_id)
    sql = 'delete from user_report_plus where classes_id=%s'
    cursor.execute(sql, _class_id)
    sql='delete from coach_teach_report where classes_id=%s'
    cursor.execute(sql, _class_id)

    con.commit()


 def select_classesId(self):

     sql = "select id from classes"

     cursor.execute(sql)
     id = cursor.fetchall()
     return  id
     #id1 = id[0][0]
class B():
    def deleteclass1(self,nn):


        if nn == 1:
          try:
            classesId1 = int(input('需要删除的课程id:'))
            classesId = int(input('输入课程id:'))
            a1 = A(3)
            id1 = a1.select_classesId()
            if (classesId,) in id1:
                if (classesId1,) in id1:
                    if classesId1 == classesId:
                        print('删除课程所有信息：')
                        # a1 = fff.A(2)  # 实例化类方法
                        classesId=str(classesId)
                        a1.isdelete(classesId)  # 调用需要执行的方法
                        print('删除成功')
                    else:
                        print('删除失败')
                else:
                    print("课程id不存在1")
            else:
                print('课程id不存在2')
          except Exception:
              print('不出现错误信息')
        else:
            print('不想删除怪我咯')

class C():
    def __init__(self,id):
        self.id=id
    def get_id(self):
        sql='select max(id)+1 from user_daily_weight '
        cursor.execute(sql)
        id=cursor.fetchall()
        id=id[0][0]
        con.commit()

        return id
    def insert_weight(self,user_uuid,weight,fat_rate,subject_id,water_rate, user_bmr,  skeleton_rate, classes_id,  resistance, mac_address,memo):
        create_time1 = time.localtime(time.time()+3600)
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", create_time1)
        id=self.get_id()
        sql='insert into user_daily_weight (id, user_uuid,create_time, weight, fat_rate, subject_id, water_rate, entrails_fat, type, user_bmr, musle_rate, pad_weight_source_type, skeleton_rate, classes_id, user_subject_uuid, resistance, mac_address, gym_id, memo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        args=(id,user_uuid,create_time,weight,fat_rate,subject_id,water_rate, 30, 1, user_bmr, 60, 1, skeleton_rate, classes_id, '21277ccc-beff-46bb-ae88-67bf86a5b92d', resistance, mac_address,0,memo)
        cursor.execute(sql,args)

        con.commit()
    def insert_weight_simple(self,user_uuid,weight,fat_rate,water_rate, user_bmr,  skeleton_rate, resistance, mac_address,create_time,memo):
        sql='insert into user_daily_weight (id, user_uuid,create_time, weight, fat_rate, subject_id, water_rate, entrails_fat, type, user_bmr, musle_rate, pad_weight_source_type, skeleton_rate, classes_id, user_subject_uuid, resistance, mac_address, gym_id,memo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        id = self.get_id()
        args = (id, user_uuid, create_time, weight, fat_rate,0, water_rate, 30, 1, user_bmr, 60, 1, skeleton_rate,
            0,0, resistance, mac_address, 0,memo)
        cursor.execute(sql, args)
        con.commit()
    def delete_weight_daily_weight(self,useruuid):
        sql='delete  from user_daily_weight where user_uuid=%s '
        cursor.execute(sql,useruuid)
        con.commit()
    def select_user_daily_weight(self,useruuid):
        create_time1 = time.localtime(time.time() + 3600)
        create_time2 = time.strftime("%Y-%m-%d ", create_time1)#当日称重时间
        #print("string=%s" % create_time2  )
        #print(create_time2)
       # a1=A(2) #调用其他类都需要实例化类方法
       # user_uuid1=a1.useruuid()
        #print(user_uuid1)

        #for useruuid in user_uuid1:
          # useruuid=str(useruuid)

        sql='select max(id) from user_daily_weight where  user_uuid=\''+useruuid+'\' and create_time like \'%' + create_time2+ '%\''
           #args=(useruuid)

        cursor.execute(sql)
        id=cursor.fetchall()
        id=id[0][0]

        return  id
       # con.commit()
    def get_userweightid(self,id11):
        sql='select user_uuid from user_daily_weight where id=%s '
        cursor.execute(sql,id11)
        user_uuid=cursor.fetchall()
        user_uuid=user_uuid[0][0]
        return user_uuid
        #con.commit()
class D():
    def name1_make(self):
        a1 = ['张', '金', '李', '王', '孙','赵','钱','黄','卫','石']
        a2 = ['玉', '明', '龙', '芳', '天', '玲','凯','开','燕','文']
        a3 = ['', '立', '玲', '山', '国', '珊','原','远','神','天']
        name=[]
        for i in range(10):
            name1= random.choice(a1) + random.choice(a2) + random.choice(a3)
            name.append(name1)
        name=name
        return name

    def get_user_code(self):
        sql='select user_code from user'
        cursor.execute(sql)
        user_code=cursor.fetchall()
        return user_code
    def user_id(self):
        sql='select max(id) from user '
        cursor.execute(sql)
        id=cursor.fetchone()
        id1=id[0]+1
        return  id1
    def user_uuid_make(self,name1):
        namespace = uuid.NAMESPACE_DNS
        user_uuid1=uuid.uuid3(namespace,name1)
        return user_uuid1

    def user_code_make(self):
        sql='select max(user_code) from user '
        cursor.execute(sql)
        user_code=cursor.fetchone()
        user_code=user_code[0]+3
        return user_code
    def tel_make(self):
        num_start = ['111', '222', '333', '123', '456', '777', '666', '302', '101', '221', '021', '011', '001']
        tele=[]
        for i in range(10):
          start = random.choice(num_start)
          end = ''.join(random.sample(string.digits, 8))  # 把多个字符合成一个字符

          tel= start + end
          tele.append(tel)
        tele=tele
        return tele
    def id_useraccount(self):
        sql='select max(id) from user_account'
        cursor.execute(sql)
        id_useraccount=cursor.fetchone()
        id_useraccount=id_useraccount[0]+1
        return id_useraccount


    def user_name(self):
        sql='select name from user '
        cursor.execute(sql)
        name =cursor.fetchall()
        return name
    def user_tel(self):
        sql='select uid from user_account'

        cursor.execute(sql)
        tel = cursor.fetchall()
        return tel




    def set_user(self):
        global create_time
        name1=self.name1_make()
        tel1=self.tel_make()
        name_exist=self.user_name()
        for i in range(len(name1)):

          create_time2 = time.localtime(time.time())

          login_time = time.strftime("%Y-%m-%d %H:%M:%S", create_time2)

          create_time = self.create_time()
          name=name1[i]
          tel = tel1[i]
          if (name,) in name_exist:
              pass
          else:
              if(tel,) in  tel1:
                  pass
              else:
                  user_code=str(self.user_code_make())
          #name1=self.name1_make()
                  id1=str(self.user_id())
                 # id_useraccount=str(self.id_useraccount())
                  user_uuid=str(self.user_uuid_make(name))
          #print(name)
         # print(login_time)
         # print(create_time)
          #print(user_code)
          #print(tel)
          #print(1)
                  print(user_uuid)
                  sql='insert into user (id, uuid,user_code,name, birthday, sex, psd, headimgurl,weight, init_weight, phase_init_weight , height, tele,avatarthumb, creat_time, points, target_weight, target_days, pulse, has_kk_report, is_topic_history_open, is_coachstar_popup, subscribe_article_id, kk_report_score, kk_report_id, kk_report_read, online_subject_id, online_subject_days,user_agent, login_time, reward, user_type,user_update_profile,circle_user_type, target_type, video_voice, has_watch_breath_light, has_watch_keep_light,status, frozen_coins, ip_address, incharge_coach_id, incharge_sale_id, incharge_trace_id, classes_interval) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                  args=(id1,user_uuid,user_code,name,'1985-01-01',1,'e10adc3949ba59abbe56e057f20f883e','http://kuaikuai.oss-cn-beijing.aliyuncs.com/avatar/avatar_56c4acc0-bff3-4ca1-b399-4de254c19a35_1516174115044',63,0,63,170,12200958352,'http://kuaikuai.oss-cn-beijing.aliyuncs.com/avatar/avatar_thumb_56c4acc0-bff3-4ca1-b399-4de254c19a35_1516174115044',create_time,115,63,0,65,0,1,1,0,0,0,1,0,0,'kkuser-4.1-test-19421/android/7.0/honor/pra-al00',login_time,0,0,1,2,3,0,0,0,0,0,'36.110.31.130, 100.97.126.145',0,0,0,0)
                  cursor.execute(sql,args)
                  con.commit()




                  #sql='insert into user_account (`id`,`uuid`,`uid`,`creat_time`,`type`) value (%s,%s,%s,%s,%s)'
                 # args=(id_useraccount,user_uuid,tel,create_time,3)
                  #cursor.execute(sql,args)

    def number(self):
        number=1000000
        return number
    def payment(self):
        no = str(random.randint(0, 9)) + str(random.randint(0, 9))
        create_time2 = time.localtime(time.time())
        no1=random.randint(0,10000)
        login_time = str(time.strftime("%Y%m%d%H%M%S", create_time2))
        while 1:
            if len(str(no1)) < 4:
                no1 = str(0) + str(no1)
                if len(str(no1)) == 4:
                    no1=str(no1)
                    break
            else:
                no1=str(no1)
                break
        pay1=self.pay1()
        pay_ment=pay1+no+login_time+no1
        return pay_ment
    def pay1(self):#payment字段前8位数字
         return str(42000000)

    def pay2(self):#payment字段前8位数字
        return  str(40012820)
    def coupon_user(self,coupon_uuid,user_uuid):
        namespace = uuid.NAMESPACE_OID
        time1=str(time.time())
        # print(namespace)
        # print(namespace1)
        uuid2 = str(uuid.uuid3(namespace, user_uuid + time1))
        create_time=self.create_time()
        expire_time=self.expire_time()
        sql='insert into `user_coupon` ( `coupon_uuid`, `user_uuid`, `has_used`, `create_time`,  `source`,  `user_coupon_uuid`, `expire_time`) values(%s,%s,%s,%s,%s,%s,%s)'
        args=(coupon_uuid,user_uuid,0,create_time,'ftyhq',uuid2,expire_time)
        cursor.execute(sql,args)

        con.commit()
        return uuid2
    def coupon(self):

        create_time = self.create_time()
        expire_time=self.expire_time()

        coupon_key=self.coupon_key()
        title=self.title()
        price=self.price()#满多少
        usable_price=self.usable_price()#减的价钱
        type=self.type()
        condition=self.condintion()
        uuid4=str(uuid.uuid1())
        sql='insert into `coupon` ( `coupon_uuid`, `coupon_key`, `title`, `price`, `usable_price`, `type`, `condition`, `all_num`, `use_num`, `subject_show_id`, `expire_time`, `create_time`, `expire_type`, `expire_days`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        args=(uuid4,coupon_key,title,price,usable_price,type,condition,1000,0,13,expire_time,create_time,0,0)
        cursor.execute(sql,args)
        con.commit()
    def coupon_key(self):
        return 'csyhqqc05'#手动修改
    def title(self):
        return '测试优惠券-全场'
    def price(self):
        return '7200'
    def usable_price(self):
        return '7200'
    def type(self):
        return '4'#0正式课券 1体验课券 4私教课券 9999全场券
    def condintion(self):
        return '[\"全场优惠券\",\"随意使用\"]'
    def create_time(self):
        create_time1 = time.localtime(time.time() - 300)
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", create_time1)
        return create_time
    def expire_time(self):
        expire_time1 = time.localtime(time.time() + 10 * 24 * 3600)
        expire_time = time.strftime("%Y-%m-%d %H:%M:%S", expire_time1)
        return expire_time
    def beijingshijian(self):
        create_time1 = time.localtime(time.time())
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", create_time1)
        return create_time
    def add_user_subject_free(self,user_uuid):
        _create_time = time.localtime(time.time() - 3600)
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", _create_time)
        start_data = time.strftime("%Y-%m-%d", _create_time)
        # end_data = time.strftime("%Y-%m-%d", _create_time)
        _create_time1 = time.localtime(time.time() - 3600 + 600)
        create_time1 = time.strftime("%Y-%m-%d %H:%M:%S", _create_time1)
        _create_time2 = time.localtime(time.time() - 3600 + 365 * 24 * 3600)
        create_time2 = time.strftime("%Y-%m-%d %H:%M:%S", _create_time2)

        end_data = time.strftime("%Y-%m-%d", _create_time2)
        uuid3=str(uuid.uuid1())
        sql = 'insert into user_subject ( subject_show_id, user_uuid, subject_id, create_time, type, leave_times, start_date, end_date, checkin_times, uuid,all_times, use_times, expire_time, adjust_times, adjust_use_times, expire_type, is_charging,  free_type, is_expire, update_time, source_type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        args1 = (4, user_uuid, 0, create_time, 0, 0, start_data, end_data, 0, uuid3, 1, 0,
                 create_time2, 1, 0, 0, 1, 0, 0, create_time, 0)
        cursor.execute(sql,args1)
        con.commit()

    def set_user1(self):
            global create_time
            name1 = self.name1_make()
            # tel1=self.tel_make()
            name_exist = self.user_name()
            b = A(2)
            user_uuid = b.useruuid()
            for i in range(len(name1)):

                create_time2 = time.localtime(time.time())

                login_time = time.strftime("%Y-%m-%d %H:%M:%S", create_time2)

                create_time = self.create_time()
                name = name1[i]
                user_uuid1=user_uuid[i]

                # tel = tel1[i]
                if (name,) in name_exist:
                    pass
                else:
                    # if(tel,) in  tel1:
                    # pass
                    # else:
                    user_code = str(self.user_code_make())
                    # name1=self.name1_make()
                    id1 = str(self.user_id())
                    # id_useraccount=str(self.id_useraccount())
                    #user_uuid = str(self.user_uuid_make(name))
                    # print(name)
                    # print(login_time)
                    # print(create_time)
                    # print(user_code)
                    # print(tel)
                    # print(1)
                    #print(user_uuid)
                    sql = 'insert into user (id, uuid, user_code, name, birthday, sex, psd, headimgurl,weight, init_weight, phase_init_weight , height, tele,avatarthumb, creat_time, points, target_weight, target_days, pulse, has_kk_report, is_topic_history_open, is_coachstar_popup, subscribe_article_id, kk_report_score, kk_report_id, kk_report_read, online_subject_id, online_subject_days,user_agent, login_time, reward, user_type,user_update_profile,circle_user_type, target_type, video_voice, has_watch_breath_light, has_watch_keep_light,status, frozen_coins, ip_address, incharge_coach_id, incharge_sale_id, incharge_trace_id, classes_interval) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    args = (id1, user_uuid1, user_code, name, '1985-01-01', 1, 'e10adc3949ba59abbe56e057f20f883e',
                            'http://kuaikuai.oss-cn-beijing.aliyuncs.com/avatar/avatar_56c4acc0-bff3-4ca1-b399-4de254c19a35_1516174115044',
                            63, 0, 63, 170, 12200958352,
                            'http://kuaikuai.oss-cn-beijing.aliyuncs.com/avatar/avatar_thumb_56c4acc0-bff3-4ca1-b399-4de254c19a35_1516174115044',
                            create_time, 115, 63, 0, 65, 0, 1, 1, 0, 0, 0, 1, 0, 0,
                            'kkuser-4.1-test-19421/android/7.0/honor/pra-al00', login_time, 0, 0, 1, 2, 3, 0, 0, 0, 0,
                            0, '36.110.31.130, 100.97.126.145', 0, 0, 0, 0)
                    cursor.execute(sql, args)
                    con.commit()
    def user_share_recomend(self,user_uuid,recomend_user_uuid):
        create_time=self.create_time()
        ticket_time=self.beijingshijian()
        sql='insert into `user_share_recommend` (`user_uuid`, `recommend_user_uuid`, `shareName`, `recommend_user_ticket`, `create_time`, `ticket_time`) values(%s,%s,%s,%s,%s,%s)'
        args=(user_uuid,recomend_user_uuid,'share_recommend',1,create_time,ticket_time)

        cursor.execute(sql, args)
        con.commit()
    def user_share_info(self):
        user_uuid={'c785d5a6-b8e6-3f2f-9193-06c39c5ccffe'
}
        return user_uuid

    def user_share(self,recommend_user_uuid):
        user_uuid=self.user_share_info()
        for user_uuid1 in user_uuid:
            self.user_share_recomend(user_uuid1,recommend_user_uuid)
    def delete_user_share(self,user_uuid):
        sql='delete from user_share_recommend where recommend_user_uuid=%s'
        cursor.execute(sql,user_uuid)
        con.commit()
if __name__ == '__main__':

  #  a=D()
   # a.coupon()
    #a.set_user()
    #user_uuid='4574227b-a286-47d2-a1c2-9cd8af17784b'
    #a.delete_user_share(user_uuid)
   #a.user_share(user_uuid)


    #a.add_user_subject_free('f928f6d6-7f23-459c-88e5-7f3e7fc483d2')
    a=A(1)
    data=a.user_name_pwd()
    gym_id1=a.get_gymid('2647546864650240')
    print(a.get_gymid('2647546864650240'))
    subject_id = a.get_subjectId(gym_id1)
    print(subject_id)
    subject_show_id=kk_buz.subject_show_id('380150')
    get_classesId=a.get_classesId()
    print(subject_show_id,get_classesId)











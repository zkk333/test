import pymysql
import webbrowser
import requests
import pad_app.主要接口.interface as f
'''
a=int(input('连接现网数据库a按2，连接测试数据库按随意:'))
if a==2:
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
else :
   try:

      con = pymysql.connect(host="192.168.41.20",
                          user="kms",
                          password="kuaikuaikms",
                          db="kk_test",
                          port=33061,
                          charset='utf8')  # 连接数据库utf-8放进去报错，找了半天原因  ，只是在数据库中用utf8而已，就是指代一种编码
      cursor = con.cursor()
   except:
      print('连接失败')'''
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
def select_data():
    sql='select data_uuid from user_class_data where class_id=383548'#57319  329837   331487 340153
    cursor.execute(sql)
    data=cursor.fetchone()
    print(data)
    data=data[0]
    return  data
#if __name__ == '__main__':
def data1():

    data=select_data()
    #print(data)

    #a.txt
    url=(f.获取上课数据+data)
    url=url+'.txt'
    #webbrowser.open(url)
    q=requests.get(url)
    #with open ('11.txt','r') as code:
    data1=q.json()
    return data1
def user_name(user_uuid):
    sql='select name from user where uuid=%s'
    cursor.execute(sql,user_uuid)
    name=cursor.fetchall()
    name=name[0][0]
    return  name
def course_type(description):
    description='%'+description+'%'
    sql = 'select id from subject_show where description like %s'
    cursor.execute(sql, description)
    id = cursor.fetchall()
    id = id[0][0]
    return id
def user_subject(description,user_uuid):
    id=course_type(description)
    sql='select uuid from user_subject where subject_show_id=%s and all_times-use_times>0 and user_uuid=%s'
    cursor.execute(sql,(id,user_uuid))
    uuid=cursor.fetchall()
    uuid=uuid[0][0]
    return uuid
def gym_id(name):
    name='%'+name+'%'
    sql='select id from gym where name like%s'
    cursor.execute(sql,name)
    name=cursor.fetchall()
    name=name[0][0]
    return name
if __name__ == '__main__':
    data2=data1()

    #description='SHOW腰课'
   # id=course_type(description)
    #user_uuid='747f161c-1580-485e-9084-3e9468bc0091'
    #uuid=user_subject(description,user_uuid)
  #  print(id)
  #  print(uuid)


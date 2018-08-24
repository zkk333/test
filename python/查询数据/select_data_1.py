import pymysql
import webbrowser
import requests
import pad_app.主要接口.interface as f
import time


try:

    con = pymysql.connect(host="47.93.118.213",
                          user="look",
                          password="LookForDev",
                          db="kk_buz",
                          port=33061,
                          charset='utf8')  # 连接数据库utf-8放进去报错，找了半天原因  ，只是在数据库中用utf8而已，就是指代一种编码
    cursor = con.cursor()
except:
    print('连接失败')

def select_data1():
    #class_id=303037
    creata_time1 = time.localtime(time.time()-24*60*60)
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", creata_time1)
    sql='SELECT DISTINCT(data_uuid) FROM user_class_data WHERE create_time >%s'#create_time >%s
    cursor.execute(sql,create_time)
    data=cursor.fetchall()
   # print(data)
    #i=len(data)
    #print(i)
    return data
def select_data():
    #class_id=303037
   # creata_time1 = time.localtime(time.time()-60*60)
    #create_time = time.strftime("%Y-%m-%d %H:%M:%S", creata_time1)
    sql='SELECT DISTINCT(data_uuid) FROM user_class_data WHERE class_id=378868'#create_time >%s
    cursor.execute(sql)
    data=cursor.fetchall()
   # print(data)
    #i=len(data)
    #print(i)
    return data
#if __name__ == '__main__':
def data1():

    data=select_data()
    #print(data)
    for data in data:
        data=data[0]
    #a.txt
        url=(f.获取上课数据+data)
        url=url+'.txt'
    #webbrowser.open(url)
        q=requests.get(url)
    #with open ('11.txt','r') as code:
        data1=q.json()
       # print(url)
    return  url
    #return url

if __name__ == '__main__':
    url=select_data()

    #for i in range(15):
     #   data1 = url[i][0]
   #     print(data1)
    print(url)
   # data2=data1()
   # print(data2)
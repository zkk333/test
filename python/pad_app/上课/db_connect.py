import pymysql
'''
廊坊环境
'''
def db_langfang():
    try:

        con = pymysql.connect(host="47.93.124.146",
                              user="kas",
                              password="kuaikuaikas",
                              db="kk_test",
                              port=33061,
                              charset='utf8')  # 连接数据库utf-8放进去报错，找了半天原因  ，只是在数据库中用utf8而已，就是指代一种编码   廊坊环境
        return con
    except:
        print('连接失败')#47.93.124.146 ：33061   kas/kuaikuaikas
'''
测试环境
'''
def db_test(a):
    if a==1:

          try:

              con = pymysql.connect(host="192.168.41.20",
                                  user="kms",
                                  password="kuaikuaikms",
                                  db="kk_test",
                                  port=33061,
                                  charset='utf8')  # 连接数据库utf-8放进去报错，找了半天原因  ，只是在数据库中用utf8而已，就是指代一种编码
            #ursor = con.cursor()
              return con
          except:
              print('连接失败')  # 测试环境
    elif a==2:
          try:

            con = pymysql.connect(host="47.93.124.146",
                                  user="kas",
                                  password="kuaikuaikas",
                                  db="kk_test",
                                  port=33061,
                                  charset='utf8')  # 连接数据库utf-8放进去报错，找了半天原因  ，只是在数据库中用utf8而已，就是指代一种编码   廊坊环境
            return con
          except:
             print('连接失败')  # 47.93.124.146 ：33061   kas/kuaikuaikas
    else:
        print('别再输其他数字了，求求你了')


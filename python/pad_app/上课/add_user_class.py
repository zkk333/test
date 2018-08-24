import  pymysql
import requests
import re
import time
import uuid
import pad_app.上课.function as ff
a = ff.A(2)
b=ff.D()
def tel():
 #tel=input('上课教练账号:')
# tel='15828640467'

 #tel = '13691421359'
 tel= '17600958351'

 coachId = a.get_coachId(tel)
 return  coachId
#uuid=uuid.uuid1()
def add_class(coachId):
  a.addclass(coachId)
#  print('添加成功')
def add_class_private(coachId,user_uuid):
    a.addclass_private(coachId, user_uuid)
def add_class_more1(coachId):
    n=int(input('请输入课程节数'))
    cn=int(input('请输入需要上课的节数,1-36最大'))
    subject_show_id=int(input('请输入上课的种类,1代表燃脂循环课,4代表防爆课'))

    a.add_add_classes_more1( coachId, n,cn,subject_show_id)
    #print(id)
    #print('添加成功')

def add_class1(coachId,coursecode,n):

      classes_id=a.addclass1(coachId,n,coursecode)
      return  classes_id

def add_user():

    user_uuid = b.set_user()
    print(user_uuid)
# coding: UTF-8


if __name__ == '__main__':
   # add_user()

    coachid=tel()
    addclass=int(input('请输入1或者2,3,4 1代表单节燃脂循环课 2代表加多节燃脂或者防爆课,3代表私教课,4代表添加用户'))
    if addclass==1:
      while True :
        add_class(coachid)
        break
    elif addclass==2:
       add_class_more1(coachid)
       print(id)
    elif add_class==3:
        add_user()
   # elif add_class==4:
    else:
        user_uuid='62cd95fe854f4491a9ce0eaa9658d3bc'

        add_class_private(coachid, user_uuid)
    #else:
        #print('操作不存在')



#单次课程





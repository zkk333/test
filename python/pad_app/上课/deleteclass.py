import pad_app.上课.function as ddd
#import pad_app.上课.addclass as d1
def _delect():
  nn =int( input('删除课程请输入1:'))#int类型
  b1=ddd.B()
  b1.deleteclass1(nn)
def __delect():
    #gym_id =
    a =ddd.A(2)
    # _class_id='214096'
    # print(isinstance(_class_id,str))#判断是否是字符串
    #name1=str(input('门店名称'))
    tel = input('上课教练账号:')
    gym_id =str(a.get_tel_gymId(tel))
    #print(gym_id)
    _class_id=a.get_time_classesId(gym_id)
    a.isdelete(_class_id)

def _delect1():
    a = ddd.A(2)
    # _class_id='214096'
    # print(isinstance(_class_id,str))#判断是否是字符串
    # name1=str(input('门店名称'))
    user_uuid='62cd95fe854f4491a9ce0eaa9658d3bc'
    # print(gym_id)
    #
    _class_id = a.get_user_uuid_classesId(user_uuid)
    a.isdelete(_class_id)
if __name__ == '__main__':
    delect_class=int(input('课程删除方式1.跟据课程id、2.跟据上课时间'))#2018-08-22 00:00:00  2018-08-23 00:00:00
    if delect_class==1:
        _delect()
    elif delect_class==2:
        __delect()
    else:
        _delect1()




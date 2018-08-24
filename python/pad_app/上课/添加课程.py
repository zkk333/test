import pad_app.上课.function as ff
import uuid
import  time
def add_course():
  a=ff.A(2)


  user_uuid='492a685f-16a4-40c0-a0a3-17dec392c9bd'
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

  a.get_subjectFB(uuid2, uuid3, uuid4, user_uuid)
def add_chengwei():
    a = ff.A(2)

    #user_code = str(input('输入学员user_code：'))
   # user_uuid = a.get_uuid_code(user_code)#根据user_code获取学员user_uuid
    user_code=str(input('请输入用户的code'))
    user_uuid =a.get_uuid_code(user_code)
    namespace = uuid.NAMESPACE_DNS
    namespace1=uuid.NAMESPACE_URL
    namespace2=uuid.NAMESPACE_OID
    price=2000000
    price1=str(price)
    price2=str(price*100)
    time1 = str(time.time())
    uuid2 = uuid.uuid3(namespace, user_uuid + time1)
    uuid5=str(uuid.uuid3(namespace2,user_uuid+time1))
    uuid4=str(uuid.uuid3(namespace1,user_uuid+time1))
    uuid2 = str(uuid2)
    uuid2 = uuid2.replace('-', '')

    a.get_chengwei(uuid2,uuid4,uuid5,user_uuid,price1,price2)

if __name__ == '__main__':
   add_chengwei()










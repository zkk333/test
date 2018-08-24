import  user_app1.user_app.weight_process as fff
import requests
def test():
  username='15234171516'
  password='123456'
  res_session=requests.session()
  headers=fff.log(username,password,res_session)
  uuid_make=fff.uuid_make()#主要是生成的uuid唯一标识码 ，即二维码生成
#print(uuid_make)
  fff.imitate_weight(res_session,uuid_make)#可有可无，操作是自助称重手机获取二维码的操作
  fff.log_succes(headers,uuid_make,res_session)#登录并打开二维码扫描器
  fff.weight(headers,res_session,uuid_make)#扫码成功，称重完成，上传数据
if __name__ == '__main__':
    test()


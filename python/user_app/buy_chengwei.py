import user_app.user_app_login as f1
import pad_app.主要接口.interface as f2
import pad_app.上课.function as f3
# pad_app.上课.login import log
import urllib3
import urllib
import requests
#mport requests
# 禁用安全请求警告
from urllib import parse
#urllib3.disable_warnings()
username='15234171516'
password='123456'
resssion=requests.session()
a=f1.log(username,password,resssion).status_code
headers = {'Cache-Control': 'no-cache',
            'User-Agent': 'KKUSER-4.4.1-test-19727/Android/4.4.4/vivo/vivo X5F',
            'Content-Type': 'application/x-www-form-urlencoded',
          #  'Content-Length': 84,
             'Host':'ts.kuaikuaikeji.com',#
             'Connection': 'Keep-Alive',
             'Accept-Encoding': 'gzip'
      }
city='上海'

name='石燕国'

user_code=3013375

user_coupon_uuid=f3.D().coupon_user('8dcd76a8-917d-11e8-bf15-448a5bad1c04','bd02b354-2355-3251-a066-e64e05ce93b6')
print(user_coupon_uuid)
data1=('tele=15234171516&private_flag=2&ele_agreement_flag=1&pay_type=1&real_name={name}&user_code={user_code}&card_face_value=720000&order_subject_number=1&user_coupon_uuid={user_coupon_uuid}&price_code=private&coins_pay=0&order_type=0&city={city}'.format(name=parse.quote(name),user_code=user_code,user_coupon_uuid=user_coupon_uuid,city=parse.quote(city)))
#data1=('tele=17600958351&ele_agreement_flag=1&pay_type=1&real_name=%E5%BF%AB%E5%BF%AB&user_code=3008370&gym_id=2648597473593346&coins_pay_count=362800&order_subject_number=1&price_code=3showyao36_60&coins_pay=1&order_type=0&city=%E5%8C%97%E4%BA%AC')
r=resssion.post(url=f2.kk_user_app_url3+f2.购买课程, headers=headers,data=data1)
print(r.status_code)
order_uuid=r.json()['order_uuid']

r=resssion.get(url=f2.kk_user_app_url3+f2.购课成功2(order_uuid), headers=headers)
print(r.status_code)
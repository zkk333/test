import user_app.user_app_login as f1
import pad_app.主要接口.interface as f2
# pad_app.上课.login import log
import urllib3
import urllib
import requests
#mport requests
# 禁用安全请求警告
from urllib import parse
urllib3.disable_warnings()
username='17600958351'
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
id=11
name='快快'
gym_id=2133621056702465
user_code=3008370
coins=362800
price_code='3showyao36_70'
data1=('city={name}&subject_show_id={id}&lat=39.90598&lon=116.640735&subject_code='.format(name=parse.quote(city),id=id))
#data1=('city=%E5%8C%97%E4%BA%AC&subject_show_id=12&lat=39.90598&lon=116.640735&subject_code=')
r=resssion.post(url=f2.kk_user_app_url3+f2.商城购买1, headers=headers,data=data1)
print(r.json())
data1=('city={name}&gym_id={gym_id}&subject_show_id={id}&lat=39.90598&lon=116.640735&subject_code='.format(name=parse.quote(city),gym_id=gym_id,id=id))
r=resssion.post(url=f2.kk_user_app_url3+f2.商城购买, headers=headers,data=data1)
print(r.json())

r=resssion.get(url=f2.kk_user_app_url3+f2.订单详情页, headers=headers)
print(r.json())
r=resssion.get(url=f2.kk_user_app_url3+f2.购课信息1(price_code), headers=headers)
print(r.json())
r=resssion.get(url=f2.kk_user_app_url3+f2.隐私协议, headers=headers)
print(r.status_code)
data1=('tele=17600958351&ele_agreement_flag=1&pay_type=1&real_name={name}&user_code={user_code}&gym_id={gym_id}&coins_pay_count={coins}&order_subject_number=1&price_code={price_code}&coins_pay=1&order_type=0&city={city}'.format(name=parse.quote(name),user_code=user_code,gym_id=gym_id,coins=coins,price_code=price_code,city=parse.quote(city)))
#data1=('tele=17600958351&ele_agreement_flag=1&pay_type=1&real_name=%E5%BF%AB%E5%BF%AB&user_code=3008370&gym_id=2648597473593346&coins_pay_count=362800&order_subject_number=1&price_code=3showyao36_60&coins_pay=1&order_type=0&city=%E5%8C%97%E4%BA%AC')
r=resssion.post(url=f2.kk_user_app_url3+f2.购买课程, headers=headers,data=data1)
print(r.status_code)
order_uuid=r.json()['order_uuid']
r=resssion.get(url=f2.kk_user_app_url3+f2.购课成功1(order_uuid), headers=headers,data=data1)
print(r.status_code)

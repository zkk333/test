import pad_app.主要接口.interface as f1
import 智运.login as f2
import pad_app.上课.function  as f6
import 智运.kk_storefront_sql as f3
import 智运.student.yuqiresult as f5
import requests
import smpt.youjian as f7
import time
import assertpy.assertpy.assertpy as f4
uname='13910211681'
pwd='123456'
f=f6.D()
#number=f.number()
res_session=requests.session()
login_log=f2.log(uname,pwd,res_session)
headers = {'user_Agent': 'KKCoach/Android',
           'connection': 'Keep-Alive',
           'Accept-Encoding': 'gzip',
           'Host': 'test.kuaikuaikeji.com',
           'Cache-Control': 'no-cache',
           }
data={"userUuid":"451ddfe4-b911-4105-b778-87552a6cb508"}
url1=f1.智运获取学员详细信息接口
ss = res_session.post(url=f1.kk_zhiyun_url3 +url1 , json=data, headers=headers)
#f4.assert_warn(ss.status_code).is_equal_to(200)
f7.is_email(ss,url1,None)
url1=f1.智运跟进记录接口
ss1= res_session.post(url=f1.kk_zhiyun_url3 +url1 , json=data, headers=headers)
f7.is_email(ss1,url1,None)
gym_id=str(1827944532281344)
data1={"coachId": '1976755360827392',
       "nextTime":'',#下次跟进时间
       "traceMemo": '',#跟进记录内容
       "traceResult": '1',#跟进的结果0,持续跟进 1，确认上课，2明确拒绝
       "traceResultReason": '',#持续跟进的理由：出差、身体不适等等
       "traceType": '1',#联系方式必填参数不能超长，测试用例书写时再考虑吧
       "userUuid": "451ddfe4-b911-4105-b778-87552a6cb508"#非必须字段，可为空
       }
url1=f1.智运上传跟进记录接口
ss2=res_session.request('post',url=f1.kk_zhiyun_url3+url1,json=data1,headers=headers)#当传的参数有非数字的字符，则会报500,coachId,traceResult,traceType是必要参数,不能传空值
f7.is_email(ss2,url1,None)
url1=f1.智运跟进记录接口
ss3=res_session.request('post',url=f1.kk_zhiyun_url3+url1,json=data1,headers=headers)
f7.is_email(ss3,url1,None)
data2={"gymId":"1827944532281344"}
url1=f1.获取教练信息
ss4=res_session.request('post',url=f1.kk_zhiyun_url3+url1,json=data2,headers=headers)
a=(ss4.elapsed.microseconds)/f.number()#单位是微秒  微秒，毫秒，秒,响应时间
role = str(3)  # 教练
f7.is_email_coach_list(ss4,url1,role,gym_id)

data1={"gymId":"1827944532281344"}
url1=f1.获取销售人员信息
ss5=res_session.request('post',url=f1.kk_zhiyun_url3+url1,json=data1,headers=headers)
#try:
role = str('')#销售人员属于全体员工
f7.is_email_coach_list(ss5,url1,role,gym_id)
#except AssertionError:
data3={"userUuid":"a819311c-e92e-47a1-8565-c7790e48b738"}
url1=f1.正式课购课时间
ss6=res_session.request('post',url=f1.kk_zhiyun_url3+url1,json=data3,headers=headers)
f7.is_email(ss6,url1,None)
buy_order=ss6.json()['buyClassItemList']
url1=f1.智运设置有效期
for buy_order in buy_order:


  if buy_order['isExpire']==1:
    orderuuid=buy_order['orderUuid']
    data4={"isExpire": 0,"orderUuid": orderuuid}
    ss7=res_session.request('post',url=f1.kk_zhiyun_url3+url1,json=data4,headers=headers)
    f7.is_email(ss7,url1,None)
  else:
      pass
url1= f1.正式课预约时间
ss7 = res_session.request('post', url=f1.kk_zhiyun_url3 +url1, json=data3, headers=headers)
f7.is_email(ss7,url1,None)
url1=f1.正式课上课时间
ss8 = res_session.request('post', url=f1.kk_zhiyun_url3 +url1 , json=data3, headers=headers)
f7.is_email(ss8,url1,None)
url1=f1.称重记录
ss9 = res_session.request('post', url=f1.kk_zhiyun_url3 +url1, json=data3, headers=headers)
f7.is_email(ss9,url1,None)
url1=f1.运动评估报告
ss10 = res_session.request('post', url=f1.kk_zhiyun_url3 +url1 , json=data3, headers=headers)
f7.is_email(ss10,url1,None)
url1=f1.运动健康档案
ss11 = res_session.request('post', url=f1.kk_zhiyun_url3 +url1 , json=data3, headers=headers)
f7.is_email(ss11,url1,None)
url1=f1.学员备注
ss12 = res_session.request('post', url=f1.kk_zhiyun_url3 +url1 , json=data3, headers=headers)
f7.is_email(ss12,url1,None)
data5={"coachId":1577346724136960,
       "classesId":0,
       "userUuid":"a819311c-e92e-47a1-8565-c7790e48b738",
       "comment":"日日日"}#基本没做限制，这个需要单独写测试用例
url1=f1.写备注
ss13 = res_session.request('post', url=f1.kk_zhiyun_url3 + f1.写备注, json=data5, headers=headers)
f7.is_email(ss13,url1,None)
url1= f1.备注录入成功
ss14 = res_session.request('post', url=f1.kk_zhiyun_url3 +url1, json=data3, headers=headers)
f7.is_email(ss14,url1,None)
url1=f1.运动规划报告接口
ss15 = res_session.request('post', url=f1.kk_zhiyun_url3 +url1, json=data3, headers=headers)
f7.is_email(ss15,url1,None)
data6={"currClassesId": -1,
       "subjectShowId": 3,
       "userUuid": "a819311c-e92e-47a1-8565-c7790e48b738"}
url1=f1.私教课历史接口
ss16= res_session.request('post', url=f1.kk_zhiyun_url3 +url1 , json=data6, headers=headers)
f7.is_email(ss16,url1,None)
#f7.erro_sendemail('执行完成')








   # print('出错的接口:',f1.获取销售人员信息)



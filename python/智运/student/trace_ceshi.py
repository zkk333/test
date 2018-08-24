import pad_app.主要接口.interface as f1
import 智运.login as f2
import pad_app.上课.function  as f6
import 智运.kk_storefront_sql as f3
import 智运.student.yuqiresult as f5
import requests
import smpt.youjian as f7
import time
import assertpy.assertpy.assertpy as f4
import excle11 as f9

uname='13910211681'
pwd='123456'
f=f6.D()
#number=f.number()
res_session=requests.session()
login_log=f2.log(uname,pwd,res_session)
def trace():
    headers = {'user_Agent': 'KKCoach/Android',
               'connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'Host': 'test.kuaikuaikeji.com',
               'Cache-Control': 'no-cache',
               }
    data1=f9.main_trace()
    trace1=f9.yongli_trace(data1)
    for trace11 in trace1:
        coachId=trace11[0]
        nextTime=trace11[1]
        if nextTime:
            nextTime1=time.strptime(nextTime, "%Y-%m-%d %H:%M:%S")#string类型转成struct_time类型
            #print(nextTime1)
            nextTime=int(time.mktime(nextTime1)*1000)
        else:
            nextTime=0
        traceMemo=trace11[2]
        traceResult=trace11[3]
        traceResultReason=trace11[4]
        traceType=trace11[5]
        userUuid=trace11[6]

        data={"userUuid":userUuid}


        data1={"coachId":coachId,
               "nextTime":nextTime,#下次跟进时间
               "traceMemo": traceMemo,#跟进记录内容
               "traceResult": traceResult,#跟进的结果0,持续跟进 1，确认上课，2明确拒绝
               "traceResultReason": traceResultReason,#持续跟进的理由：出差、身体不适等等
               "traceType": traceType,#联系方式必填参数不能超长，测试用例书写时再考虑吧
               "userUuid":userUuid#非必须字段，可为空
               }
        print(data1)
        url1 = f1.智运上传跟进记录接口
        ss2 = res_session.request('post', url=f1.kk_zhiyun_url3 + url1, json=data1,
                                  headers=headers)  # 当传的参数有非数字的字符，则会报500,coachId,traceResult,traceType是必要参数,不能传空值
        f7.is_email(ss2, url1, None)
        url1 = f1.智运跟进记录接口
        ss3 = res_session.request('post', url=f1.kk_zhiyun_url3 + url1, json=data, headers=headers)
        f7.is_email(ss3, url1, None)
if __name__ == '__main__':
    trace()
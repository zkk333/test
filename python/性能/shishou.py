from locust import HttpLocust,TaskSet,task  #性能测试必备类HttpLocust,TaskSet,task
import pad_app.上课.function as f1
import queue
import 查询数据.select_data_1 as f3
import pad_app.上课.add_user_class as ff2
import hashlib
import time
import base64
import requests
import subprocess
import pad_app.主要接口.interface as f4

#HttpLocust :每一个模拟的用户可以看做一个 HttpLocust 类的实例
''' TaskSet类定义了每个用户的任务集合，测试任务开始后，
每个 Locust 用户会从 TaskSet 中随机挑选一个任务执行，
然后随机等待 HttpLocust 类中定义的 min_wait和 max_wait 之间的一段时间，执行下一个任务'''
class UserBahavior(TaskSet):#指向一个 TaskSet 类，TaskSet 类定义了每个用户的行为


    @task
    def login(self):
        try:
            data__2=self.locust.user_data_queue.get()
        except queue.Empty:
            print('no data')


            exit()

        data_1=data__2

        username ='17600958351'
        password ='e10adc3949ba59abbe56e057f20f883e'
        headers = {'user_Agent': 'KKTabletUDP/Android',
                   'connection': 'Keep - Alive',
                   'Accept - Encoding': 'gzip',
                   'Host': 'test.kuaikuaikeji.com',
                   'Cache - Control': 'no-cache',
                   }
        r = self.client.post("/kcas/PadCoachLoginV2", headers=headers)
        auth = r.headers.get('WWW-Authenticate', '')
        m = hashlib.md5()  # 创建md5对象
        m1 = hashlib.md5()
        password1 = base64.encodebytes(password.encode('utf-8'))[:-1]  # base64编码
        password1 = password1.decode('utf-8')
        up = (username + password1)
        strs2 = (auth + up).encode('utf-8')
        m1.update(strs2)  # 生成加密串
        resp = m1.hexdigest()  # 获取加密串`
        response = base64.encodebytes(resp.encode('utf-8'))[:-1]
        response = response.decode('utf-8')  # byte类型转换成string类型
        author = "user=\"" + username + "\",response=\"" + response + "\""
        headers={'user_Agent':'KKTabletUDP/Android',
         'connection': 'Keep - Alive',
         'Accept - Encoding': 'gzip',
         'Host': 'test.kuaikuaikeji.com',
         'Cache - Control': 'no-cache',
         'authorization': author,
       }
        r=self.client.post("/kcas/PadCoachLoginV2",headers=headers)
        if r.status_code==200:
            data_ = data_1.get('classDataList')
            coachId = r.json()['coachId']

            for y in data_:
                y = y

            coursecode = y.get('courseCode')
            if 'SJ' in coursecode:
                pass
            else:
                classesid = y.get('classesId')
                print(classesid)
                n = int(len(data_))
                classes_id = ff2.add_class1(coachId, classesid, coursecode, n)  # 加的课的id，不可缺少

                a = f1.A(2)
                gym_id = a.get_gymid(coachId)
                subjectid = a.get_subjectId(gym_id)
                data = {'coachId': coachId,
                        'listRange': 0,
                        'listSort': 0,
                        'pageIndex': 0,
                        'pageSize': 100}
                headers = {'user_Agent': 'KKTabletUDP/Android',
                           'connection': 'Keep - Alive',
                           'Accept - Encoding': 'gzip',
                           'Host': 'test.kuaikuaikeji.com',
                           'Cache - Control': 'no-cache'
                           }
                r = self.client.post('/kcas/PadGetCoachClassListV2', json=data, headers=headers)
                data1 = {
                    'classesId': classes_id,
                }
                st =self.client.post('/kcas/PadStartClassV2', json=data1, headers=headers)
                # coursecode=st.json()
                data2 = {
                    'coachId ': coachId,
                    'classesId': classes_id,
                    'courseCode': coursecode

                }
                cek1 =self.client.post('/kcas/PadGetCourseDetailV2', json=data2, headers=headers)

                cek2 =self.client.post('/kcas/PadGetCoachClassCheckinV2', json=data2, headers=headers)
                numbers = cek2.json().get('userCheckinMap')
                t = []
                i1 = len(numbers)
                # classes_id=(classes_id)
                for y in numbers:
                    # b=numbers[y]

                    t.append(y)  # 把人数换成列表格式
                # print(t[0])
                # data1 = f2.data1()
                # data1 = data1.get('classDataList')
                start_time1 = (time.time()) * 1000
                print(start_time1)
                # start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_time1)
                # print(start_time)
                end_time1 = (time.time() + 3600) * 1000
                print(end_time1)
                # end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_time1)
                # print(len(data1))
                classDataList = []

                # print(1)
                # print(n)
                for i in range(n):
                    # print(data_)
                    # classesId = '218527'
                    # weight=data_[i]['weightData']
                    # print(weight)
                    # print(i)
                    if 'weightData' in data_[i]:
                        data_[i]['weightData'] = data_[i]['weightData']
                        data_[i]['baseData'] = data_[i]['baseData']

                    else:
                        pass

                    data_[i]['endTime'] = end_time1
                    data_[i]['startTime'] = start_time1
                    # data1[i]['subjectId'] = subjectid
                    data_[i]['userUuid'] = t[i]
                    data_[i]['classesId'] = classes_id
                    data_[i]['subjectId'] = subjectid

                    # data1[i]['courseCode'] = coursecode
                    classDataList.append(data_[i])
                    # print(3)

                    # print(classDataList)


                    # cek3 =.post(url='http://test.kuaikuaikeji.com/kcas/PadGetCoachClassInfoV2', json=data,headers=headers)  # 刷新后的页面，获取课程详情
                # print(2)
                data3 = {'classDataList': classDataList,
                         "uploadType": 1,
                         'uploadVersion': 3

                         }
                # print(coursecode )

                report1 =self.client.post('/kcas/PadUploadAllClassDataV2', json=data3, headers=headers)
                # print(report1.json())
                # print(report1.status_code)
                # print(classesId)


                # tmeout = (report1.elapsed.microseconds)/number#发送请求到服务器端响应的时间大于1秒，只会截取后面的小数部分
                tmeout1 = report1.elapsed.total_seconds()  # 这个才是正确的 获取响应时间，发送请求到收到相应的时间差
                # report1.elapsed.
                print('上传报告所需时间', tmeout1)
                # print('上传报告所需时间', tmeout)
                if report1.status_code == 200:
                    data4 = {'classesId': classes_id,
                             'subjectId': subjectid}
                    getreport1 =self.client.post('/kcas/PadGetClassReportListV2', json=data4, headers=headers)
                    # print(getreport1.json())
                    classReportList = getreport1.json().get('classReportList')
                    for x in range(len(classReportList)):
                        cl = classReportList[x]
                        reurl = cl.get('reportUrl')
                        print(reurl)

                        # if getreport1.status_code!=200:
                        # print(classes_id)
                        # exit()

                        # else:
                        #  print('success')
                        # classReportList = getreport1.json().get('classReportList')
                        print(classes_id)

                else:
                    print('上传失败 ', report1.status_code)



        else:
            print('用户名或密码错误')


class  WebsiteUser(HttpLocust):
    task_set = UserBahavior

   # a=f1.A(1)
   # data__1=a.user_name_pwd()
    data=f3.select_data()
    user_data_queue=queue.Queue()
    for i in range(18):
        data1 = data[i][0]

        url = (f4.获取上课数据 + data1)
        url = url + '.txt'
        # print(data)

        # webbrowser.open(url)
        p = requests.get(url)
        data1 = p.json()
        user_data_queue.put_nowait(data1)
    weight =60

    host='http://test.kuaikuaikeji.com'

    min_wait = 3000
    max_wait = 6000


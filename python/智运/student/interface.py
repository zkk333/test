import pad_app.主要接口.interface as f1
import 智运.login as f2
import 智运.kk_storefront_sql as f3
import requests
import assertpy.assertpy.assertpy as f4
import smpt.youjian as f7



userchar=['134','1 3 4','1@','@#','中zz','中文$%','zz','1111111111111','"11','"无语接"','无语接','🍅🍅','🍅🍅']

uname='13910211681'
pwd='123456'
res_session=requests.session()
login_log=f2.log(uname,pwd,res_session)
for userchar1 in userchar:
 # userchar2=userchar1.encode("utf-8").decode('')
  #userchar=int(userchar)
  headers = {'user_Agent': 'KKCoach/Android',
           'connection': 'Keep-Alive',
           'Accept-Encoding': 'gzip',
           'Host': 'test.kuaikuaikeji.com',
           'Cache-Control': 'no-cache',
           }
  data1 = {"gymId": 1827944532281344,
           "userChar": userchar1,
         "pageControl":
             {"listSort": 0,
              "pageCount": -1,
              "pageIndex": 0,
              "pageSize": 40,
              "recordCount": -1},

      }
  url1=f1.智运查询燃脂循环课学员信息接口
  ss = res_session.post(url=f1.kk_zhiyun_url3 + url1, json=data1, headers=headers)
  url2=f1.智运查询体验课学员接口
  ss1=res_session.post(url=f1.kk_zhiyun_url3 + url2, json=data1, headers=headers)
  #print('-------------------------------')
  #print('测试用例执行：', userchar1)
  f7.is_email(ss,url1,userchar1)
 # print('第二个接口')
  f7.is_email(ss1,url2,userchar1)
  #print('-------------------------------')




import 智运.login as f1
import 智运.kk_storefront_sql as f2
import requests
import json
uname='13910211681'
pwd='123456'
res_session=requests.session()
login_log=f1.log(uname,pwd,res_session)
print(login_log.status_code)
id=f2.coachId(uname)
if login_log.json()['coachId']==id:
    print('success')
else:
    print('登录账号与coach_id不符')



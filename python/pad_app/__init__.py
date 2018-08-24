'''
import pad_app.上课.login as f1
import requests
uname = '15600905550'
pwd = '123456'
res_session = requests.session()
a=f1.log(uname, pwd,res_session)
print(a.json())
'''
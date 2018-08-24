import sys
sys.path.append('..')
import pad_app.主要接口.interface as f1
import requests
import pad_app.上课.function as f2
import pad_app.体测.photo as f3
import pad_app.体测.coursecode as f4

a=f2.D()
user_code=a.get_user_code()
res_session=requests.session()
photodata1=f3.photo1()
photodata2=f3.photo2()

courseCodeName=f4.型男减脂型例子
courseCodeType=f4.型男减脂code

while True: # 无限循环
 gender = input('请输入男或者女')
 if gender=='男'or gender=='女':

    try :
        usercode = int(input('请输入用户id'))
        if (usercode,) in user_code:
            usercode=str(usercode)
            data = {'userCode': usercode}
            user_info = res_session.post(url=f1.kkweight_app_url2 + f1.体侧用户信息, json=data)
            print(user_info.json())
            name=user_info.json().get('userName')
            data ={
            "report": {
              "courseCodeName": courseCodeName,
               "courseCodeType": courseCodeType,
               "courseType": "1",
               "frontUserPhotoInfo": {
                'photoData':photodata1,
                'photoMemo':123
               },
              "physicalType":1,
               "sideUserPhotoInfo": {
                    'photoData': photodata1,
                    'photoMemo': 123
                },
                "physicalType": 1,
               "submitReport": 1,
               "userBaseInfo": {
              "age": 33,
              "armLeft": 33,
              "armRight": 33,
              "chestCircumference": 33,
              "gender":gender,
              "height": 174,
              "hipCircumference": 33,
              "legLeft": 33,
              "legRight": 33,
              "name": name,
              "personType": "普通人",
              "waistCircumference": 33
        },
                "userInjureInfo": {
                    "userHurtInfoList": [],
                    "userInjureHistoryList": []
                },

        "userWeightInfo": {
            "bmi": 21.5,
            "bmr": 1740.3,
            "bones": 2.7,
            "bonesRatio": 4.2,
            "entrailsFat": 7,
            "fat": 12,
            "fatRatio": 18.4,
            "muscle": 50.4,
            "muscleRatio": 77.3,
            "sjDeepSquatAbility": 5,
            "sjPushUpAbility": 5,
            "sjSitBeforeBendsAbility": 5,
            "sjSitUpAbility": 5,
            "water": 35.5,
            "waterRatio": 54.5,
            "weight": 59
        }
    },
    "userCode": 148
   }
            data['userCode']=usercode
            upload_data=res_session.post(url=f1.kkweight_app_url2+f1.上传体侧数据接口,json=data)
            print(upload_data.json().get('reportUrl'))

            break
        else:
            print('查不到该用户')
    except ValueError:
           print('请输入整数')
 else:
    print('请输入提示的性别')
#print(user_code)
  # data={'userCode':usercode}
#user_info=requests.post(url=f1.kkweight_app_url2+f1.体侧用户信息,json=data)
import pad_app.主要接口.interface as f1
import requests
import pad_app.上课.function as f2
import pad_app.体测.photo as f3
def physical_pro_test():
 a=f2.D()
 user_code=a.get_user_code()
 res_session=requests.session()
 photodata1=f3.photo1()
 photodata2=f3.photo2()
 while True:#无限循环
    try :
        usercode = int(input('请输入用户id'))
        if (usercode,) in user_code:
            usercode=str(usercode)
            data = {'userCode': usercode}
            user_info = res_session.post(url=f1.kkweight_app_url2 + f1.体侧用户信息, json=data)
            #print(user_info.json())
            data={'report':{
       "frontUserPhotoInfo": {
        "photoMemo": "666",
        "photoData": photodata1,
         'photoUrl': ''
       },
       "physicalType": 0,
       "sideUserPhotoInfo": {
         "photoMemo": "666",
         "photoData": photodata2,
         'photoUrl':''
       },
       "submitReport": 0,
       "userBaseInfo": {
        "age": 23,
        "armLeft": 33,
        "armRight": 33,
        "chestCircumference": 33,
        "gender": "男",
        "height": 174,
        "hipCircumference": 33,
        "legLeft": 33,
        "legRight": 33,
        "name": "小号",
        "personType": "普通人",
        "waistCircumference": 33
      },
       "userInjureInfo": {
          "userHurtInfoList": [],
          "userInjureHistoryList": []
      },
       "userWeightInfo": {
          "bmi": 21.1,
          "bmr": 1796.3,
          "bones": 2.8,
          "bonesRatio": 4.4,
          "entrailsFat": 5,
          "fat": 10,
          "fatRatio": 15.6,
          "muscle": 51.2,
          "muscleRatio": 80,
          "squatCount": 33,
          "water": 35.8,
          "waterRatio": 56,
          "weight": 64
      }
      },
          "userCode":3008370
      }
            data['userCode']=usercode
            upload_data=res_session.post(url=f1.kkweight_app_url2+f1.上传体侧数据接口,json=data)
            print(upload_data.json().get('reportUrl'))

            break
        else:
            print('查不到该用户')
    except ValueError:
           print('请输入整数')
#print(user_code)
  # data={'userCode':usercode}
#user_info=requests.post(url=f1.kkweight_app_url2+f1.体侧用户信息,json=data)
if __name__ == '__main__':
    physical_pro_test()
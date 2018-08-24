
import json
import requests

import time
import pad_app.上课.function as  qqq
import copy
import pad_app.主要接口.interface as q

def _weight_get(useruuid):
  data ={
        "initWeightData": {
          "dataSourceType": 1,
          "entrailsFat": 5,#内脏脂肪
          "fatRate": 18, # 脂肪率
          "macAddress": "F9:15:01:D8:AD:5A",
          "musleRate": 68.5, # 肌肉率
          "resistance": 463.29998779296875, # 电阻
          "skeletonRate": 4.6,  # 骨骼率
          "userBmr": 1547,   # 用户bmr
          "waterRate": 51.1, # 水分率
          "weight": 64.2      # 体重
        },
         "userUuid":"492a685f-16a4-40c0-a0a3-17dec392c9bd"

}
  headers = {'user_Agent': 'KKTabletUDP/Android',
           'connection': 'Keep - Alive',
           'Accept - Encoding': 'gzip',
           'Host': 'test.kuaikuaikeji.com',
           'Cache - Control': 'no-cache'
           }

  #print(user_uuid1)
  #user_uuid = a2.useruuid()

  data['userUuid']=useruuid
    #print(data)
   # time1=time.time()
  checkdata1 = requests.post(url=q.kkweight_app_url2+q.三次校验接口, json=data,
                               headers=headers)

  weightData = checkdata1.json()['corrWeightData']
  weight=data["initWeightData"]['weight']
  fat_rate=weightData.get('fatRate')
  mac_address=weightData.get('macAddress')
  resistance=weightData.get('resistance')
  skeleton_rate=weightData.get('skeletonRate')
  user_bmr=weightData.get('userBmr')
  water_rate=weightData.get('waterRate')
  memo=checkdata1.json()['modifiedMemo']
  WeightData= {
       "dataSourceType": 1,
       "entrailsFat": 5,  # 内脏脂肪
       "fatRate": fat_rate,  # 脂肪率
       "macAddress": mac_address,
       "musleRate": 68.5,  # 肌肉率
       "resistance": resistance,  # 电阻
       "skeletonRate": skeleton_rate,  # 骨骼率
       "userBmr": user_bmr,  # 用户bmr
       "waterRate":  water_rate,  # 水分率
       "weight": weight  # 体重
   }
  return WeightData
def weight_get(subject_id,classes_id):
  data ={
        "initWeightData": {
          "dataSourceType": 1,
          "entrailsFat": 5,#内脏脂肪
          "fatRate": 18, # 脂肪率
          "macAddress": "F9:15:01:D8:AD:5A",
          "musleRate": 68.5, # 肌肉率
          "resistance": 463.29998779296875, # 电阻
          "skeletonRate": 4.6,  # 骨骼率
          "userBmr": 1547,   # 用户bmr
          "waterRate": 51.1, # 水分率
          "weight": 64.2      # 体重
        },
         "userUuid":"492a685f-16a4-40c0-a0a3-17dec392c9bd"

}
  headers = {'user_Agent': 'KKTabletUDP/Android',
           'connection': 'Keep - Alive',
           'Accept - Encoding': 'gzip',
           'Host': 'test.kuaikuaikeji.com',
           'Cache - Control': 'no-cache'
           }

  a1= qqq.A(2)

  #import 上课.addclass1 as f


  #a1 = f.A(2)  # 调用其他类都需要实例化类方法
  user_uuid1 = a1.useruuid()
  #user_uuidlist = []
  # print(user_uuid1)
  #user_uuid1=['8472006b-caa2-4414-8a58-3c4bdb7cc72f']
  for useruuid in user_uuid1:
      #print(useruuid)
      a = qqq.C(4)

      id = a.select_user_daily_weight(useruuid)
      #print(id)
      if id == None:
          pass
          #print('shangke')
      else:
          # print(id)
          user_uuid2 = a.get_userweightid(id)
          user_uuid1 = copy.deepcopy(user_uuid1)
          # print(user_uuid2)
          # for user_uuid2 in user_uuid1:
          user_uuid1.remove(user_uuid2)#当天称过重的话就删除该称重用户
  #print(user_uuid1)
  #user_uuid = a2.useruuid()
  for useruuid in user_uuid1:
   data['userUuid']=useruuid
    #print(data)
   # time1=time.time()
   checkdata1 = requests.post(url=q.kkweight_app_url2+q.三次校验接口, json=data,
                               headers=headers)

   weightData = checkdata1.json()['corrWeightData']
   weight=data["initWeightData"]['weight']
   fat_rate=weightData.get('fatRate')
   mac_address=weightData.get('macAddress')
   resistance=weightData.get('resistance')
   skeleton_rate=weightData.get('skeletonRate')
   user_bmr=weightData.get('userBmr')
   water_rate=weightData.get('waterRate')
   memo=checkdata1.json()['modifiedMemo']
   WeightData= {
       "dataSourceType": 1,
       "entrailsFat": 5,  # 内脏脂肪
       "fatRate": fat_rate,  # 脂肪率
       "macAddress": mac_address,
       "musleRate": 68.5,  # 肌肉率
       "resistance": resistance,  # 电阻
       "skeletonRate": skeleton_rate,  # 骨骼率
       "userBmr": user_bmr,  # 用户bmr
       "waterRate":  water_rate,  # 水分率
       "weight": weight  # 体重
   }
     #print(weightData)
   #return WeightData
   useruuid=useruuid
   classes_id=classes_id
   subject_id=subject_id
   b4 = qqq.C(2)
   b4.insert_weight(useruuid, weight, fat_rate,subject_id, water_rate, user_bmr, skeleton_rate,classes_id, resistance, mac_address, memo)

def weight_get_curweight(create_time,_fat_rate):#仅限验证三次校验
    data = {
        "initWeightData": {
            "dataSourceType": 1,
            "entrailsFat": 5,  # 内脏脂肪
            "fatRate": _fat_rate,  # 脂肪率
            "macAddress": "F9:15:01:D8:AD:5A",
            "musleRate": 68.5,  # 肌肉率
            "resistance": 463.29998779296875,  # 电阻
            "skeletonRate": 4.6,  # 骨骼率
            "userBmr": 1547,  # 用户bmr
            "waterRate": 51.1,  # 水分率
            "weight": 64.2  # 体重
        },
        "userUuid": "492a685f-16a4-40c0-a0a3-17dec392c9bd"

    }


    headers = {'user_Agent': 'KKTabletUDP/Android',
           'connection': 'Keep - Alive',
           'Accept - Encoding': 'gzip',
           'Host': 'test.kuaikuaikeji.com',
           'Cache - Control': 'no-cache'
           }

   # a1 = qqq.A(2)

# import 上课.addclass1 as f


# a1 = f.A(2)  # 调用其他类都需要实例化类方法
    #user_uuid1 = a1.useruuid()
# user_uuidlist = []
# print(user_uuid1)
    user_uuid1 = ['8472006b-caa2-4414-8a58-3c4bdb7cc72f']



    for useruuid in user_uuid1:
       data['userUuid'] = useruuid
    # print(data)
    # time1=time.time()
       checkdata1 = requests.post(url=q.kkweight_app_url2 + q.三次校验接口, json=data,
                               headers=headers)

       weightData = checkdata1.json()['corrWeightData']
       weight = data["initWeightData"]['weight']
       fat_rate = weightData.get('fatRate')
       mac_address = weightData.get('macAddress')
       resistance = weightData.get('resistance')
       skeleton_rate = weightData.get('skeletonRate')
       user_bmr = weightData.get('userBmr')
       water_rate = weightData.get('waterRate')
       memo = checkdata1.json()['modifiedMemo']
    # print(weightData)
       #useruuid = useruuid
     # classes_id = classes_id
      #subject_id = subject_id
       b4 = qqq.C(2)
       b4.insert_weight_simple(useruuid,weight,fat_rate,water_rate, user_bmr,  skeleton_rate, resistance, mac_address,create_time,memo)
       return memo
if __name__ == '__main__':
    subjectId='1629679193753615'
    classesId='243692'
    weight_get(subjectId, classesId)





'''
data2=data1
data2['dataSourceType']=3
data2['userUuid']='492a685f-16a4-40c0-a0a3-17dec392c9bd'
print(data2)

updata1=res_session .post(url='http://test.kuaikuaikeji.com/kcas/PadUserWeighingUploadWeightDataV2 ', json=data2, headers=headers)
print(updata1.status_code)'''
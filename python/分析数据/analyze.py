import matplotlib.pyplot as plt  #plt 是pyplot的别名
import 查询数据.select_data as t1
import re

plt.rcParams['font.sans-serif'] = ['SimHei']#绘图设置中文字体,修改参数

data=t1.data1()['classDataList']
#print(len(data))


for i in range(len(data)):
  unitdataList1=data[i]['unitDataList']
  print(unitdataList1)
  user_uuid=data[i]['userUuid']
  heartbeats = []
  scopex = []
  scopey = []
  scopez = []
  _heartbeats = []
  _scopex = []
  _scopey = []
  _scopez = []
  print(len(unitdataList1))
  for y in range(len(unitdataList1)):

      heartbeats1=list(eval(unitdataList1[y]['heartbeats']))#一个学员的单元心率,字符串格式，变成列表格式。'1,2,3'变成[1,2,3]
      heartbeats2=str(heartbeats1)
      #print(h)
      heartbeats2= re.findall(r'\d+', heartbeats2)
      #print(222)
      print(len(heartbeats2))
      if 'scopeX'  in unitdataList1[y].keys():#确保字段存在
        if unitdataList1[y]['scopeX']=='':
          scopex1=[]
          scopey1=[]
          scopez1=[]

        else:
          scopex1=list(eval(unitdataList1[y]['scopeX']))
          scopey1=list(eval(unitdataList1[y]['scopeY']))
          scopez1=list(eval(unitdataList1[y]['scopeZ']))
      else:
          scopex1 = []
          scopey1 = []
          scopez1 = []
      _heartbeats.append(heartbeats1)
      _scopex.append(scopex1)
      _scopey.append(scopey1)
      _scopez.append(scopez1)
  _heartbeats=str(_heartbeats)
  _heartbeats= re.findall(r'\d+', _heartbeats)#z正则提取字符串中的数字并以列表形式展示
  for k in _heartbeats:
      heartbeats.append(int(k))
  heartbeats=heartbeats
  _scopex=str(_scopex)
  _scopex = re.findall(r'\d+', _scopex)
  for k in _scopex:
      scopex.append(int(k))
  scopex=scopex
 # heartbeats=heartbeats
  _scopey = str(_scopey)
  _scopey = re.findall(r'\d+',_scopey)
  for k in _scopey:
      scopey.append(int(k))
  scopey = scopey
  _scopez = str(_scopez)
  _scopez = re.findall(r'\d+', _scopez )
  for k in _scopez:
      scopez.append(int(k))
  scopez = scopez
  print('心率点数',len(_heartbeats))
  print('scopex长度', len(_scopex))
  print('scopey长度', len(_scopey))
  print('scopez长度', len(_scopez))
  x0=[]
  x3 = []
  x2 = []
  x1 = []
  for z in range(len(_heartbeats)):
      x0.append(z+1)
  x0=x0
  for z in range(len(_scopex)):
      x1.append(z+1)
  x1=x1
  for z in range(len(_scopey)):
      x2.append(z+1)
  x2=x2
  for z in range(len(_scopez)):
      x3.append(z+1)
  x3=x3
  user_name=str(t1.user_name(user_uuid))
  #print(user_name)
  plt.figure('心率图')
  plt.title(user_name)
  plt.axis([0,len(_heartbeats)+500, 0, 200])#坐标范围
  plt.plot(x0, heartbeats, color="r", linestyle="-", linewidth=1)
  plt.grid(color="k", linestyle=":")

  plt.savefig('心率图.png')
  #img.save('d:/心率图.png')

  plt.figure('scopex数据图')
  plt.title(user_name)
  plt.axis([0, len(_scopex)+1000, 0, 60000])  # 坐标范围
  plt.plot(x1, scopex, color="r", linestyle="-", linewidth=1)
  plt.grid(color="k", linestyle=":")
  plt.figure('scopey数据图')
  plt.title(user_name)
  plt.axis([0, len(_scopey) + 1000, 0, 60000])  # 坐标范围
  plt.plot(x2, scopey, color="r", linestyle="-", linewidth=1)
  plt.grid(color="k", linestyle=":")
  plt.figure('scopez数据图')
  plt.title(user_name)
  plt.axis([0, len(_scopez) + 1000, 0, 60000])  # 坐标范围
  plt.plot(x3, scopez, color="r", linestyle="-", linewidth=1)
  plt.grid(color="k", linestyle=":")

  plt.show()
  #print('----------------------')


  #print(len(heartbeats1))


#a=list(eval(a))  #字符串类型转换成列表或者可以用 a=a.split()



#data['classDataList']
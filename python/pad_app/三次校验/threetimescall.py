import pad_app.上课.function as  qqq
import pad_app.weight_weighing.weight as ff
import time
import pad_app.上课.function as f2
class curweight():
 def insert_three_times_weight(self,user_uuid,_fat_ratelist,_create_time1):

   weight='64.2'
   fat_ratelist=_fat_ratelist
   water_rate='54'
   user_bmr='1568'
   skeleton_rate='4.6'
   resistance='456'
   mac_address='F9:15:01:D8:AD:5A'
   create_time1 =_create_time1
#print(time.time())
 #global  create_time
   for i in range(len(create_time1)):
     create_time1[i]=time.localtime(create_time1[i])
     create_time= time.strftime("%Y-%m-%d %H:%M:%S", create_time1[i])
   #print(create_time)
 #print(create_time)
     fat_rate=fat_ratelist[i]
     a=qqq.C(2)
     a.insert_weight_simple(user_uuid,weight,fat_rate,water_rate, user_bmr,  skeleton_rate, resistance, mac_address,create_time,'(NULL)')
 def threetimes_weight(self,_fat_rate):#_fat_rate假设这是称重数据

   create_time1 = time.localtime(time.time() )
   create_time = time.strftime("%Y-%m-%d %H:%M:%S", create_time1)

  #ff.weight_get_curweight(create_time,_fat_rate)#本次称重
   memo= ff.weight_get_curweight(create_time,_fat_rate)
   return  memo
 def create_time_make(self,n):#创建的是不同日，但是具体时分秒与当日时分秒几乎一致，除了日子不一致


    create_time1 = time.time()-3600*25*n
     #create_time1.append(create_time1)
    return create_time1
 def create_day_time_make(self,n):#创建的是当天不同时间点,这个n值尽量小点


    create_time1 = time.time()-3600*n
     #create_time1.append(create_time1)
    return create_time1
 def create_time_make_(self,n,m):#创建今天之前同日不同时间  n的值尽量写小
     create_time1 = time.time()-(3600*24*n)+m*60
     return create_time1
 def memo1(self):
    memo1='历史称重次数3次\r\n第4次或以上称重\r\n进入稳定纠正算法'#\r换行。\n 回车
    return memo1
 def curweightprocess(self,user_uuid,_fat_ratelist,_create_time1,_fat_rate):
   a=f2.C(2)
   a.delete_weight_daily_weight(user_uuid)
   self.insert_three_times_weight(user_uuid,_fat_ratelist,_create_time1)#假装前两次数据是称重好的，所以直接插到库中
#f1.threetimes_weight(_fat_rate)#会调用到三次校验的接口
   memo=self.threetimes_weight(_fat_rate)#校验后
   #a=memo.get('fatRate1')
   #print(a)
   print(memo)
   memo1=self.memo1()
   if memo1 in  memo :
  #if memo
      if '执行稳定' in memo and '纠正' in memo:
        print('校验了')
      else:
          print('没有校验1')

   else:
      if '执行纠正' in memo:
        print('校验了')
      else:
        print('不会校验')
  #print(fat_rate)
  #if fat_rate ==_fat_rate:
      #print('校验了')
 #else:
    #  print('校验了')
#if __name__ == '__main__':
   # insert_three_times_weight()
   # print('ok')
   # threetimes_weight()


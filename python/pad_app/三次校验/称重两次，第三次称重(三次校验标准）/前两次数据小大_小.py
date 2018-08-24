import pad_app.三次校验.threetimescall as f1
import pad_app.上课.function as f2
a=f1.curweight()
user_uuid='8472006b-caa2-4414-8a58-3c4bdb7cc72f'
_fat_rate=11 #假设是称重数据
_fat_ratelist=[10,12]  #称重校验，小小差距小于2
create_time1=a.create_time_make(2)#称重前两天
create_time2=a.create_time_make(1)#称重前一天
_create_time1=[create_time1,create_time2]
a.curweightprocess(user_uuid,_fat_ratelist,_create_time1,_fat_rate)
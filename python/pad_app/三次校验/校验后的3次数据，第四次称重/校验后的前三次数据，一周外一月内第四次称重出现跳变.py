import pad_app.三次校验.threetimescall as f1
import pad_app.上课.function as f2
a=f1.curweight()
user_uuid='8472006b-caa2-4414-8a58-3c4bdb7cc72f'
_fat_rate=13.7 #假设是称重数据
_fat_ratelist=[11,12,10]  #称重校验，小小差距小于2
create_time1=a.create_time_make(17)#称重前10天16
create_time2=a.create_time_make(15)#称重前9天15
create_time3=a.create_time_make(8)#最新一次称重30天以内8
_create_time1=[create_time1,create_time2,create_time3]
a.curweightprocess(user_uuid,_fat_ratelist,_create_time1,_fat_rate)
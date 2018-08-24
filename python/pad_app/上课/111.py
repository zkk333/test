'''import pad_app.上课.function as f
a=f.D()
user_uuid=a.set_user()
name1='张振'
tel1='15234171516'
name=a.user_name()
tel=a.user_tel()
if (name1,) in name:
    print(1)
    if (tel1,) in tel:
        print(2)
    else:
        print(3)
else:
    pass
'''
import pad_app.上课.function as f
from pad_app.上课.function import D

#a=f.D()
#D().coupon_user('8dcd76a8-917d-11e8-bf15-448a5bad1c04','0959353b-e23e-4e1f-b22d-8f3a2a88f846')
D().coupon_user('8dcd76a8-917d-11e8-bf15-448a5bad1c04','bd02b354-2355-3251-a066-e64e05ce93b6')

#a.coupon()


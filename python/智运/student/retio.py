''''''
import 智运.kk_storefront_sql as f1
def sale_retio(sale):
    if sale<30000:
        return 0.09
    elif sale<50000:
        return 0.1
    elif sale < 60000:
        return 0.11
    elif sale < 70000:
        return 0.12
    elif sale < 80000:
        return 0.13
    elif sale < 90000:
        return 0.14
    elif sale <100000:
        return 0.15
    else:
        return 0.16
def private_sale_retio():
    return 0.7*0.1
def coins_pay_retio():
    return 0.3*0.1
def private_sale():
    return 0.7
def coins_pay():
    return 0.3
def manger_retio(gym_money):
    if gym_money<50000:
        return 0.01
    elif gym_money<80000:
        return 0.012
    elif gym_money < 100000:
        return 0.014
    elif gym_money < 120000:
        return 0.016
    elif gym_money < 150000:
        return 0.018
    elif gym_money < 180000:
        return 0.02
    elif gym_money < 200000:
        return 0.025
    elif gym_money < 220000:
        return 0.03
    elif gym_money < 250000:
        return 0.035
class Dianzhang():
    def gym_new_user_retio(self,gym_new_user):
        if gym_new_user<=30:
           # print
            return gym_new_user*0.01
        else:
            return 0.3
    def gym_class_retio(self,gym_class):
        if gym_class<0.1:
            return 0.0
        elif 0.1<=gym_class<=0.4:
            return (gym_class-0.1)
        else:
            return 0.3

    def gym_user_lc_retio(self,lc):
        if lc<=0.6:
            return 0
        elif 0.6<lc<0.8:
            return (lc-0.6)
        elif lc>=0.8:
            return 0.2
    def money_retio(self,sale) :
        if sale<15000:
            return 0
        if 15000<=sale<30000:
            money_retio=(sale//5000-2)*0.05
            return money_retio
        else:
            return 0.2
class Zhujiaolian():
    def gym_user_lc_retio_zjl(self,lc):
        if lc <= 0.6:
            return 0
        elif 0.6 < lc < 0.8:
            return (lc - 0.6)
        elif lc > 0.8:
            return 0.2
    def gym_class_retio_zjl(self,gym_class):
        if gym_class<=0.2:
            return 0
        elif 0.2<gym_class<=0.4:
            return (gym_class-0.2)
        else:
            return 0.2

def teach_retio(teach):
    if teach<=50:
        return 0
    elif 50<teach<=80:
        return (teach-50)*0.01
    else:
        return 0.3
def user_teach_effect(teach):
    if teach <= 50:
        return 0
    elif 50<teach <= 80:
        return (teach - 50) * 0.01
    else:
        return 0.3
class Jiaolian():
    def ty_num_jl(self,num):
        if num<=15:
            return num*0.01
        else:
            return 0.15
    def geren_new_user_jl(self,num):
        if num <=5:
            return num*0.08
        else:
            return 0.4

    def money_retio_jl(self,sale):
        if sale < 20000:
            money_retio = (sale // 5000) * 0.04
            return money_retio
        else:
            return 0.15

class Xiaoshou():
    def ty_num_xs(self,num):
        if num <= 25:
            return num * 0.01
        else:
            return 0.25
    def gym_user_lc_retio_xs(self,lc):
        if lc<=0.5:
            return 0
        elif 0.5<lc<0.8:
            return (lc-0.5)*0.5
        elif lc>=0.8:
            return 0.15
    def geren_new_user_xs(self,num):
        if num <=8:
            return num*0.05
        else:
            return 0.4
    def money_retio_xs(self,sale):
        if sale <10000:
            return 0
        if sale < 20000:
            money_retio = ((sale // 5000)-1) * 0.05
            return money_retio
        else:
            return 0.2


class Prize():
    def ty_prize_xs(self,num):
        return num*10
    def geren_new_user_prize_xs(self,num):
        if num>5:
            return num*20

    def gym_new_user_prize(self,gym_new_user):
        if gym_new_user>30:
            #sale_user=(gym_new_user-30)*20
            return (gym_new_user-30)*20
    def gym_user_lc_prize(self,lc):
        if lc>0.8:
            return  ((lc-0.8)//0.05)*100
        elif lc==1:
            return 300
        else:
            return 0
    def  gym_class_prize(self,gym_class):
        if gym_class>0.4:
            return ((gym_class-0.4)//0.1)*100
        elif gym_class==1:
            return 500
        else:
            return 0
    def tech_prize(self,teach):#个人授课能力绩效与学员锻炼效果绩效
        if teach>80:
            return ((teach-80)//5)*100
        elif teach==100:
            return 300
        else:
            return 0












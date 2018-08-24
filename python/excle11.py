# -*- coding: utf-8 -*-
import xlrd
import datetime
import time
import re
from xlrd import xldate_as_tuple
def open_excl(file):
    try:
          excle1=xlrd.open_workbook(file)#打开excle文件
          return excle1
    except Exception as e:
        print(e)#打印报错信息
def read_excle1(data1):
    ncols = data1.ncols   # 行
    #name = data1.name
    #print(name)
    #print(ncols)
    gym_name1=[]
    cell2=[]
    for x in range(0,ncols):
        #x1=x
        cell1=str(data1.cell(0,x))
        cell3=(cell1.strip('text:')).strip("'")
        cell2.append((cell3,x))
    cell3=cell2
    return cell3
    #print(cell2)
def aa(cell3,kk):
    global n
    for a in cell3:
            #print(a)
            a1 = a[0]
            a2 = a[1]
            #print(a1)
           # print(a2)
            if a1==kk:
                n=a2
            else:
                continue

                #print(n)
            return n


def read_excle(file,index1):
    data=open_excl(file)
    data1=data.sheets()[index1]#打开第一个工作表

    nrows = data1.nrows  # 行nrows
    #print(nrows)
    name=data1.name
    return data1
    #read_excle1(data1)
    #print(name)
    #print(nrows)
def yongli(data1):
    nrows = data1.nrows
    print(nrows )
    order = []

    # print(cell1)
    cell3 = read_excle1(data1)
    print(cell3)
    n1 = aa(cell3, 'price_code')
    n2 = aa(cell3, 'all_times')
    # print(n2)
    n3 = aa(cell3, 'subject_show_id')
    # print(n3)
    n4 = aa(cell3, 'deal_price')
    n5 = aa(cell3, 'coins_pay')
    n6 = aa(cell3, 'pay_fee')
    n7 = aa(cell3, 'create_time')
    n8 = aa(cell3, 'create_time1')
    n9 = aa(cell3, 'user_uuid')
    n10 = aa(cell3, 'sale_coach_id')
    n11=aa(cell3, 'gym_id')

    for y in range(1,nrows ):
        price_code = data1.cell(y, n1).value
        all_times = data1.cell(y, n2).value
        ctype1 = data1.cell(y, n2).ctype
        # create_time2 = data1.cell(y, 7).value
        all_times = ctypen(ctype1, all_times)
        subject_show_id = data1.cell(y, n3).value
        ctype1 = data1.cell(y, n3).ctype
        # create_time2 = data1.cell(y, 7).value
        subject_show_id = ctypen(ctype1, subject_show_id)

        deal_price = data1.cell(y, n4).value
        ctype1 = data1.cell(y, n4).ctype
        # create_time2 = data1.cell(y, 7).value
        deal_price = ctypen(ctype1, deal_price)
        coins_pay = data1.cell(y, n5).value
        ctype1 = data1.cell(y, n5).ctype
        # create_time2 = data1.cell(y, 7).value
        coins_pay = ctypen(ctype1, coins_pay)
        pay_fee = data1.cell(y, n6).value
        ctype1 = data1.cell(y, n6).ctype
        # create_time2 = data1.cell(y, 7).value
        pay_fee = ctypen(ctype1, pay_fee)
        ctype = data1.cell(y, n7).ctype
        create_time = data1.cell(y, n7).value
        create_time1 = ctypen(ctype, create_time)
        ctype1 = data1.cell(y, n8).ctype
        create_time2 = data1.cell(y, n8).value
        create_time3 = ctypen(ctype1, create_time2)

        user_uuid = data1.cell(y, n9).value
        sale_coach_id = data1.cell(y, n10).value
        gym_id=data1.cell(y,n11).value
        # print(sale_coach_id)
        # ctype1 = data1.cell(y, 9).ctype
        #  print(ctype1)
        # sale_coach_id1 = ctypen(sale_coach_id, ctype1)
        # print(sale_coach_id1)
        xinxi = (price_code, all_times, subject_show_id, deal_price, coins_pay, pay_fee, create_time1, create_time3, user_uuid,sale_coach_id,gym_id)
        if xinxi[0]:
            order.append(xinxi)
        else:
            pass
    return order

def yongli_trace(data1):
    nrows = data1.nrows
   # print(nrows )
    order = []

    # print(cell1)
    cell3 = read_excle1(data1)
    # print(cell3)
    n1 = aa(cell3, 'coachId')
    n2 = aa(cell3, 'nextTime')
    # print(n2)
    n3 = aa(cell3, 'traceMemo')
    # print(n3)
    n4 = aa(cell3, 'traceResult')
    n5 = aa(cell3, 'traceResultReason')
    n6 = aa(cell3, 'traceType')
    n7 = aa(cell3, 'userUuid')


    for y in range(1,nrows ):
        #coachId= data1.cell(y, n1).value
        coachId = data1.cell(y, n1).value
        ctype1 = data1.cell(y, n1).ctype
        # create_time2 = data1.cell(y, 7).value
        coachId = ctypen(ctype1, coachId)
        nextTime= data1.cell(y, n2).value
        ctype1 = data1.cell(y, n2).ctype
        # create_time2 = data1.cell(y, 7).value
        nextTime = ctypen(ctype1, nextTime)

        traceMemo = data1.cell(y, n3).value
        ctype1 = data1.cell(y, n3).ctype
        # create_time2 = data1.cell(y, 7).value
        traceMemo = ctypen(ctype1, traceMemo)
        traceResult = data1.cell(y, n4).value
        ctype1 = data1.cell(y, n4).ctype
        # create_time2 = data1.cell(y, 7).value
        traceResult = ctypen(ctype1, traceResult)
        traceResultReason = data1.cell(y, n5).value
        ctype1 = data1.cell(y, n5).ctype
        # create_time2 = data1.cell(y, 7).value
        traceResultReason = ctypen(ctype1, traceResultReason)
        ctype = data1.cell(y, n6).ctype
        traceType = data1.cell(y, n6).value
        traceType = ctypen(ctype,traceType)
        ctype = data1.cell(y, n7).ctype
        userUuid = data1.cell(y, n7).value
        userUuid= ctypen(ctype, userUuid)

        # print(sale_coach_id)
        # ctype1 = data1.cell(y, 9).ctype
        #  print(ctype1)
        # sale_coach_id1 = ctypen(sale_coach_id, ctype1)
        # print(sale_coach_id1)
        xinxi = (coachId,nextTime,traceMemo,traceResult, traceResultReason, traceType, userUuid )
        if xinxi[0]:
            order.append(xinxi)
        else:
            pass
    return order
def main():
     return  read_excle(r'D:\zaoshuju.xlsx', 0)
def main_trace():
    return read_excle(r'D:\trace.xlsx',0)

def ctypen(ctype1,cell):#测试用例类型判断，时间类型，长整形，整形
    if ctype1==3:
        #print(*xldate_as_tuple(cell, 0))
        #print(cell)
        date1= datetime.datetime(*xldate_as_tuple(cell, 0))
        #print(isinstance(data1,(int, str, list)))
        #print(date1)
       # print(date1.timetuple())
        create_time1 = time.mktime(date1.timetuple())
        #print(create_time1)
        create_time1 = time.localtime(create_time1)
        cell = time.strftime('%Y-%m-%d  %H:%M:%S', create_time1)


    elif ctype1 == 2 and cell % 1 == 0:  # 如果是整形
       #print(cell)
       cell = int(cell)
    else:
        cell=cell
      # print(cell)

    return cell


if __name__ == '__main__':
    data1=main_trace()
    print(yongli_trace(data1))




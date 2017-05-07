#coding=utf-8


from datetime import timedelta, date
import httplib
import time
import os
import datetime
from conf import config
import  calendar


#收益第二天生效
def profit_start_time():
    return str(date.today()+timedelta(days=1))+' 00:00:00'

def profit_end_time(day=0):
    return str(date.today()+timedelta(days=int(day)+1))+' 00:00:00'

#根据指定计息起始时间以及投资时间周期计算可赎回时间
def profitCalcDate_refundDate(profitCalcDate, day):
    return str(datetime.datetime.strptime(profitCalcDate,"%Y-%m-%d %H:%M:%S")+timedelta(days=int(day)))


#收益当天生效
def profit_start_time_same_day():
    return str(date.today()+timedelta(days=0))+' 00:00:00'

def profit_end_time_same_day(day):
    return str(date.today()+timedelta(days=int(day)))+' 00:00:00'
#可赎回时间
def refundDate():
    return str(date.today()+timedelta(days=1))+' 00:00:00'


def expire_date(days):
    now_time = datetime.datetime.now()
    expire_time = str(now_time + datetime.timedelta(days=int(days)))
    return expire_time[0:19]

'''
获取当前服务器时间，并同步本地时间
'''
def get_webservertime(host):
    try:
        conn=httplib.HTTPConnection(host)
        conn.request("GET", "/")
        r=conn.getresponse()
        #r.getheaders() #获取所有的http头
        ts=  r.getheader('date') #获取http头date部分
        # print '============================'
        # print ts
        # print '============================'
        #将GMT时间转换成北京时间
        ltime= time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
        ttime=time.localtime(time.mktime(ltime)+8*60*60)
        dat="date %u-%02u-%02u"%(ttime.tm_year,ttime.tm_mon,ttime.tm_mday)
        tm="time %02u:%02u:%02u"%(ttime.tm_hour,ttime.tm_min,ttime.tm_sec)
        currenttime="%u-%02u-%02u %02u:%02u:%02u"%(ttime.tm_year,ttime.tm_mon,ttime.tm_mday,ttime.tm_hour,ttime.tm_min,ttime.tm_sec)
        os.system(dat)
        os.system(tm)
        return currenttime

    except:
        return False


'''
获取当前时间和前一天的时间
'''
def now_yes_time():
    #将服务器时间同步到本地
    #get_webservertime(config.host)
    now_time = datetime.datetime.now()
    now_time = now_time + datetime.timedelta(seconds=120)

    now_time_format = now_time.strftime('%Y-%m-%d %H:%M:%S')
    yes_time = now_time + datetime.timedelta(days=-1)
    yes_time_format = yes_time.strftime('%Y-%m-%d %H:%M:%S')

    return str(now_time_format),str(yes_time_format)


'''
分割时间
daytime = '2016-03-30 09:37:25'
'''
def split_time(daytime):
    t1 = daytime.split(' ')[0].split('-')
    t2 = daytime.split(' ')[1].split(':')
    year = t1[0]
    month = t1[1]
    day = t1[2]
    hour = t2[0]
    minute = t2[1]
    second = t2[0]

    return [year,month,day,hour,minute,second]


'''
比较l_time 是否在时间区间[start_t, end_t]中
'''
def compare_time(l_time, start_t, end_t):

    s_time = time.mktime(time.strptime(start_t,'%Y-%m-%d %H:%M:%S')) # get the seconds for specify date
    e_time = time.mktime(time.strptime(end_t,'%Y-%m-%d %H:%M:%S'))
    log_time = time.mktime(time.strptime(l_time,'%Y-%m-%d %H:%M:%S'))

    if (float(log_time) >= float(s_time)) and (float(log_time) <= float(e_time)):
        return True

    return False



'''
计算两个日期相差几天
'''
def Caltime(now_time, end_time):
    date1=time.strptime(now_time,"%Y-%m-%d %H:%M:%S")
    date2=time.strptime(end_time,"%Y-%m-%d %H:%M:%S")
    date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
    date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
    if (date2-date1).days<0:
        return 0
    else:
        return (date2-date1).days+1

'''
计算两个日期相差多少秒
'''

def Caltime_second(date1,date2):

    date1 = time.mktime(time.strptime(date1,'%Y-%m-%d %H:%M:%S'))
    date2 = time.mktime(time.strptime(date2,'%Y-%m-%d %H:%M:%S'))

    return abs(date2-date1)


'''
计算下个月的当前天
'''

def get_nextmonth_of_day(current_date):
    t1 = current_date.split(' ')[0].split('-')
    year = int(t1[0])
    month = int(t1[1])
    day = int(t1[2])

    if month == 1:
        if calendar.isleap(year):
            days = 29
        else:
            days = 28
        if day>days:
            next_day=days
        else:
            next_day = day
        next_month=2
        return next_month,next_day

    if month in (3,5,7,8,10,12):
        if day==31:
            next_day=30
        else:
            next_day=day

        if month == 12:
            next_month=1
            if day==31:
                next_day=31
        else:
            next_month=month+1
        return next_month,next_day

    if month in (2,4,6,9,11):
        next_day=day
        next_month=month+1
        return next_month,next_day


'''
获取当前月的第一天开始时间和最后一天结束时间
'''
def get_current_month_start_end_time():
    day_now = time.localtime()
    day_begin = '%d-%02d-01 00:00:00' % (day_now.tm_year, day_now.tm_mon)  # 月初肯定是1号
    wday, monthRange = calendar.monthrange(day_now.tm_year, day_now.tm_mon)  # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
    day_end = '%d-%02d-%02d 23:59:59' % (day_now.tm_year, day_now.tm_mon, monthRange)
    return day_begin,day_end



if __name__ == '__main__':
    # print profitCalcDate_refundDate("2016-03-31 00:00:00","8")
    # print Caltime('2016-03-31 00:00:00', '2016-04-09 23:59:59')
    # print get_nextmonth_of_day("2016-04-08")
    #
    # print '%d月%d日增涨至6.0%%'%get_nextmonth_of_day("2016-11-30")
    #
    # get_webservertime("mappx.xiaoniuapp.com")


    day = Caltime('2016-04-18 23:00:00', '2016-04-22 00:00:00')
    print day

    # a = int(30*(6.5+0+0)*int(1000000)/100/360+\
    #                         9*0.6*int(1000000)/100/360)

    # print a
    # print (9*0.6*1000000)/100/360
    # print int((9*0.6*1000000)/100/360)
    print expire_date(365)
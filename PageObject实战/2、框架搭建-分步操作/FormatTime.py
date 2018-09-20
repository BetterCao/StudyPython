import time
from datetime import timedelta,date

def date_time_chinese():
    #return(time.strftime("%Y年%m月%d日 %H时%M分%S秒",time.localtime()))
    #直接这样写会报错
    return(time.strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒'))

def date_chinese():
    #return time.strftime("%Y年%m月%d日",time.localtime())
    #直接这样写会报错
    return (time.strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日'))

def time_chinese():
    #return time.strftime("%H时%M分%S秒",time.localtime())
    #直接这样写或报错
    return (time.strftime('%H{h}%M{m}%S{s}').format(h='时',m='分',s='秒'))

def date_time():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

def date_time_slash():
    return time.strftime("%Y/%m/%d %H:%M:%S",time.localtime())

def dates():
    return time.strftime("%Y-%m-%d",time.localtime())

def date_slash():
    return time.strftime("%Y/%m/%d",time.localtime())

def times():
    return time.strftime("%H:%M:%S",time.localtime())

def year():
    return time.strftime("%Y",time.localtime())

def month():
    return time.strftime("%m",time.localtime())

def day():
    return time.strftime("%d",time.localtime())

def hour():
    return time.strftime("%H",time.localtime())

def minute():
    return time.strftime("%M",time.localtime())

def seconds():
    return time.strftime("%S",time.localtime())

def str_to_tuple(stime):
    return time.strptime(stime,"%Y-%m-%d %H:%M:%S")

def add_date(day_num):
    today = date.today()
    times = today+timedelta(days=day_num)
    return times

def sub_date(day_num):
    today = date.today()
    times = today-timedelta(days=day_num)
    return times

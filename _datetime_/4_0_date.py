import datetime
import time



1. 时间，时间赋值，零点

d = datetime.datetime.now()
zero_date = datetime.datetime(d.year, d.month, d.day)
print(zero_date)



2. 时间操作，前几天，后几天
datetime.datetime.now() - datetime.timedelta(days=3)

datetime.datetime.now() + datetime.timedelta(days=3)

datetime.datetime.now() - datetime.timedelta(hours=3)
datetime.datetime.now() + datetime.timedelta(hours=3)


是否是周末
now = datetime.datetime.now()
0   1   2   3   4   5   6
周日                    周六
now.weekday() in (0, 6)
now.weekday() not in (0, 6)

3.时间格式格式化

时间转化为字符串 strftime(format)
now = datetime.datetime.now()
字符串格式
%Y:year
%m:month
%d:day
%h:hour
%M:minute
%S:seconds

now.strftime("%Y-%m-%d %H:%M:%S")

字符串转化为时间 strptime(string[, format])
s = '2019-12-19 11:12:10'
d = datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
print(d)
print(type(d))


4. time 时间戳
时间戳是指：格林威治时间
自1970年1月1日(00:00:00 GMT)至当前时间的总秒数

now = int(time.time())


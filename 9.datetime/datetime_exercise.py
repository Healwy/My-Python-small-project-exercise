#coding:utf-8

import time
import datetime

print(time.time())
print(datetime.datetime.fromtimestamp(time.time()))
print(datetime.datetime.fromtimestamp(10000000))

#datetime可以将unix时间戳转换成实际的日期
dn = datetime.datetime.now()
print(dn)
print('year:{},month:{},day:{},hour{}'
      '.minute{}.second{}'.format(dn.year,dn.month,dn.day,dn.hour,dn.minute,dn.second))

#datetime可以创建实例
dt = datetime.datetime(2018, 3, 28, 22, 57, 10)
print('year:{},month:{},day:{},hour{}'
      '.minute{}.second{}'.format(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second))

#datetime可以比较大小，时间大的大
dt = datetime.datetime(2018, 3, 28, 22, 57, 10)
dn = datetime.datetime(2019, 3, 28, 22, 57, 10)
print(dt> dn)

#一段时间
delta = datetime.timedelta(days=5, hours=10, minutes=50)
print(delta.days, delta.microseconds)
print(delta.total_seconds())

dt = datetime.datetime.now()
hundreddays = datetime.timedelta(days=100)

print(dt + hundreddays)
print(dt - hundreddays)

#转换成格式化字符串
dt = datetime.datetime(2018, 3, 28, 22, 57, 10)
print(dt.strftime('%Y/%m/%d %H:%M:%S'))

#字符串转成时间
print(datetime.datetime.strptime('2018','%Y'))


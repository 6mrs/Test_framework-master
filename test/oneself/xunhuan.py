#!/usr/bin/env python3
import calendar
import time

# 计算1到100的总和
# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
#     print("1 到 %d 之和为: %d" % (100, sum))
# 无限循环
# var = 1
# while var == 1:
#     num = int(input('输入数字'))
#     print("输入的数字是：", num)
# 计算三角形面积


# a, b, c = (input("请输入三角形三边的长：").split())
# a = int(a)
# b = int(b)
# c = int(c)
# p = (a + b + c) / 2
# s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print("三角形面积为：", format(s, '.2f'))

# 时间模块

localtime = time.asctime(time.localtime(time.time()))  # 获取可读的时间模式的函数是asctime()，strftime 方法来格式化日期
print(localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# 日历
cal = calendar.month(2021, 1)
print("以下为日历", cal)

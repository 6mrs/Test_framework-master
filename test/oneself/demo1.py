#!/usr/bin/env python3

# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i != j) and (i != k) and (j != k):
#                 print(i, j, k)

# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

# for i in range(1, 85):
#     if 168 % i == 0:
#         j = 168 / i
#         if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
#             m = (i + j) / 2
#             n = (i - j) / 2
#             x = n * n - 100
#             print(x)

# 获取100以内的质数
# num = [];
# i = 2
# for i in range(2, 100):
#     j = 2
#     for j in range(2, i):
#         if (i % j == 0):
#             break
#     else:
#         num.append(i)   # append方法在列表末尾增加新的对象
# print(num)


# extend()和append()方法


# def chengeextend(str):
#     mylist.extend([40, 50, 60]);
#     print(mylist)
#     return
# def chengeappend(str):
#     mylist.append([1, 2, 3])
#     print(mylist)
#     return
# mylist = [10, 20, 30]
# chengeappend(mylist)
# print(mylist)
# chengeextend(mylist)
# [print(mylist)]

#  类对象

# class myclass:
#     i = 12345
#
#     def f(self):
#         return 'helloword'
#
#
# s = myclass()
# print("MyClass 类的属性 i 为：", s.i)
# print("MyClass 类的方法 f 输出为：", s.f())
# 类的方法

# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
#
# # 实例化类
# # p = people('runoob', 10, 30)
# # p.speak()
# # 类的继承
# class student(people):
#     grade = ''
#
#     def __init__(self, n, a, w, g):
#         people.__init__(self, n, a, w)
#         self.grade = g
#
#     def speak(self):
#         print("%s 说: 我 %d 岁,我在读%d年级" % (self.name, self.age, self.grade))x
#
#
# s = student('runoob', 10, 3)
# s.speak()
#  列表、元组
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'q']
list3 = ["python", "java", "html"]
list1.append(6)
list2.extend('qiu')
list2.append('qiu')

print(list1)
print(list2.count('q'))


#1##########################################
# class St:
#     def __init__(self, gets):
#         self.gets = string.upper()
#     def prnt(self):
#         print(self.gets)
# string = input("String:")
# print1 = St(string)
# print1.prnt()
#2##########################################
# class Circle():
#     def __init__(self, r):
#         self.radius = r
#     def area(self):
#         return 3.1416*(self.radius**2)
# R = int(input("Radius:"))
# circle = Circle(R)
# print(circle.area())
#3##########################################
# class Shape():
#     def __init__(self):
#         pass
#     def area(self):
#         return 0
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
#
# Area = Rectangle(int(input("Lenth: ")),int(input("with: ")))
# print("Area: " + str(Area.area()))
#4##########################################
#5##########################################
# class Account:
#     def __int__(self, owner, put, balance, witte):
#         self.owner = owner
#         self.balance = balance
#         self.put = put
#         self.witte = witte
#
#         def deposite(self):
#             print(f"Hello {self.owner}, you put {self.put}$ and with {self.witte}$, now you has {self.balance}$")
#
# owner = "NAE"#input("Name:")
# put = 555 #int(input("Sum:"))
# witte = 5 #int(input("Sum to with:"))
# balance = put - witte
# pp = Account(owner, put, balance, witte)
# pp.deposite()
#6##########################################
# class prime:
#     def __int__(self, nums1):
#         self.nums1 = nums
#         self.list = []
#     def check(self, nums1):
#         for i in nums1:
#             a = 0
#             for j in range(2, i):
#                 if i // j == i / j:
#                     a += 1
#             if a < 1:
#                 list.append(i)
#             return list
# nums = list(map(int,input().split()))
# print = prime(nums)
# print.check(nums)
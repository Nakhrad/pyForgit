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
# import math
# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def show(self):
#         return f"First point: ({self.x}, {self.y})"
#     def move(self, x1, y1):
#         self.x += x1
#         self.y += y1
#         return f"Second point: ({self.x}, {self.y})"
#     def dist(self, x2, y2):
#         xd = abs(self.x - x2)
#         yd = abs(self.y - y2)
#         return "Distance between points: " + str(math.sqrt(xd**2 + yd**2))
# point = Point(int(input("X coordinate: ")), int(input("Y coordinate: ")))
# print(point.show())
# print(point.move(int(input("Second X-point: ")), int(input("Second Y-point: "))))
# print(point.dist(int(input("Coordinates of the next point on the X-axis: ")), int(input("Coordinates of the next point on the Y-axis: "))))
#5##########################################
# class Account():
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, dep):
#         self.balance += dep
#         print(f"{self.owner}, the operation was successful!\nYour balance is {self.balance}")
#     def withdraw(self, wit):
#         self.balance -= wit
#         print(f"{self.owner}, the operation was successful!\nYour balance is {self.balance}")
# print("Please, write your name and balance. Press 'enter' to continue...")
# owner1 = Account(input("Account owner's name: "), int(input("Balance: ")))
# str1 = input("Write Withdraw or Deposit: ")
# if str1 == "Withdraw":
#     owner1.withdraw(int(input("Write the amount: ")))
# if str1 == "Deposit":
#     owner1.deposit(int(input("Write the amount: ")))
#6##########################################
# class Prime():
#     def __init__(self, list1):
#         self.list1 = list1
#     def is_prime(self):
#         list12 = []
#         for i in self.list1:
#             x = 0
#             for j in range(2, (i // 2) + 1):
#                 if i % j == 0:
#                     x += 1
#             if x == 0:
#                 list12.append(i)
#         return list12
#
# list11 = list(map(int, input().split()))
# fun = Prime(list11)
# print(fun.is_prime())
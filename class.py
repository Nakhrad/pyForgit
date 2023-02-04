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
class prime:
    def __int__(self, nums1):
        self.nums1 = nums1
        self.list1 = []
    def check(self):
        for i in nums1:
            a = 0
            for j in range(2, i):
                if i // j == i / j:
                    a += 1
            if a < 1:
                list1.append(i)
            print(list1)
nums1 = list(map(int,int(input().split())))
print1 = prime(nums1)
print1.check()
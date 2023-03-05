#1#################################################################
# def myp(*n):
#     a = 1
#     for i in n:
#         a *=i
#     return a
# print(myp(1, 2, 3, 4))
#2################################################################
# def ma(n):
#     u = 0
#     l = 0
#     for i in n:
#         if i.isupper()== True:
#             u += 1
#         else:
#             l +=1
#     print("uppercas:", u, "lower:", l)
# ma("sadAS")
#3####################################################################
# def isPali(s):
#     return s == s[::-1]
# ans = isPali("polilop")
# if ans:
#     print("Yes")
# else:
#     print("No")
#4#####################################################################
# import math
# def sqt(n, s):
#     sq = math.sqrt(n)
#     return f"Square root of {n} after {s} miliseconds is {sq}"
# print(sqt(12, 1254))
#5######################################################################
# t = [True, True, True]
# x = all(t)
# print(x)
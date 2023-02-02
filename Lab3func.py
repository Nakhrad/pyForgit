#1########################################
# def ounc(gramm):
#     ounces = gramm * 28.3495231
#     print(ounces)
# ounc(10)
#2#######################################
# def cel(f):
#     cels = (5 / 9) * (f - 32)
#     print(cels)
# cel(10)
#3########################################
# def puz(heads, legs):
#     rab = ((legs - (heads * 2))*2)/4
#     ch = heads - rab
#     str1 = "Number of rabbits: " + str(rab) + "\nNumber of chickens: " + str(ch)
#     return str1
# heads = 35
# legs = 94
# print(puz(heads, legs))
#4###########################################
# def filter_prime(nums):
#     list = []
#     for i in nums:
#         a = 0
#         for j in range(2, i):
#             if i // j == i / j:
#                 a += 1
#         if a < 1:
#             list.append(i)
#
#     if nums.index(i) == len(nums)-1:
#         return list
# nums = list(map(int,input().split()))
# print(filter_prime(nums))
#5###################################################

#6##################################################
# def reverse(str1):
#     list1 = list(map(str,str1.split()))
#     list1.reverse()
#     str2 = ""
#     for i in list1:
#         str2 += i + " "
#     return str2
#
# str1 = input()
# print(reverse(str1))
#7###################################################
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

# def has33(num):
#     for i in range(1,len(num)):
#         if num[i-1] == 3 and num[i] == 3:
#             return True
#     else:
#         return False
# num = list(map(int,input().split()))
# print(has33(num))
#8###################################################

#9###################################################

#10###################################################

#11###################################################

#12###################################################

#13-14###################################################
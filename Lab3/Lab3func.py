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

# import itertools
#
# s = input("String:")
# nums = list(s)
# permutations = list(itertools.permutations(nums))
# print([''.join(permutation) for permutation in permutations])
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
# spy_game([1, 2, 4, 0, 0, 7, 5]) --> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) --> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) --> False

# def spygame(num):
#     for i in range(0, len(num)):
#         if num[i] == 0:
#             for j in range(i + 1, len(num)):
#                 if num[j] == 0:
#                     for k in range(j + 1, len(num)):
#                         if num[k] == 7:
#                             return True
#     else:
#         return False
# num = list(map(int, input().split(',')))
# print(spygame(nums))
#9###################################################
# import math
# def volume(r):
#     return (4/3) * (math.pi) * (r**3)
# rad = float(input())
# print(volume(rad))
#10###################################################
# def unique(list):
#     unique_list = []
#
#     for i in list:
#         if i not in unique_list:
#             unique_list.append(i)
#     print(unique_list)
#
#
# list = list(map(str, input().split()))
# unique(list)
#11###################################################
# def palindrome(str):
#     return str == str[::-1]
#
#
# str = input()
# a = palindrome(str)
#
# if a:
#     print("Yes, palindrome")
# else:
#     print("Not polindrome")
#12###################################################
# def histogram(list):
#     for i in list:
#         print("*" * i)
#
# list = list(map(int, input().split(', ')))
# histogram(list)
#13-14###################################################
# def f_guess(num, guess):
#     if guess < num:
#         print('Your guess is too low.')
#         return False
#     if guess > num:
#         print('Your guess is too high.')
#         return False
#     if guess == num:
#         return True
#
# import random
# t = 0
# print('Hello! What is your name?')
# name = input()
# num = random.randint(1, 20)
# print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
# while True:
#     print('Take a guess.')
#     guess = input()
#     guess = int(guess)
#     t += 1
#     b = f_guess(num, guess)
#     if b == True:
#         print('Good job, ' + name + '! You guessed my number in ' + str(t) + ' guesses!')
#         break
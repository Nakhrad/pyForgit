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
def filter_prime(nums):
    list = []
    for i in nums:
        a = 0
        for j in range(2, i):
            if i // j == i / j:
                a += 1
        if a < 1:
            list.append(i)

    if nums.index(i) == len(nums)-1:
        return list
nums = list(map(int,input().split()))
print(filter_prime(nums))
#5###################################################
#6##################################################

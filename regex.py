import unicodedata
import re
#1########################################################
# f = open("rox.txt", "r", encoding='utf-8')
# pattern = r'a.b*'
#
# for x in f:
#     match = re.findall(pattern, x)
#     if match:
#         print(f"{x} matches the pattern '{pattern}'")
#2#########################################################
# f = open("rox.txt", "r", encoding='utf-8')
# pattern = r'abb'
# for x in f:
#     match = re.findall(pattern, x)
#     if match:
#         print(f"{x} matches the pattern '{pattern}'")
# pa2 = r'abbb'
# for x in f:
#     match = re.findall(pa2, x)
#     if match:
#         print(f"{x} matches the patter '{pa2}'")
#3#####################################################
# f = open("rox.txt", "r", encoding='utf-8')
# p = r'[a-n]+_'
# for x in f:
#     m = re.findall(p, x)
#     if m:
#         print(x, m)
#4####################################################
# f = open("rox.txt", "r", encoding='utf-8')
# p = r'[A-N]+[a-n]'
# for x in f:
#     m = re.findall(p, x)
#     if m:
#         print(x, m)
#5#####################################################
# f = open("rox.txt", "r", encoding='utf-8')
# p = r'a+([a-zA-Z]|[0-9])+b'
# for x in f:
#     m = re.findall(p, x)
#     if m:
#         print(x, m)
#6######################################################
f = open("rox.txt", "r", encoding='utf-8')
for x in f:
    d = re.sub(" ", "|", x)
    if d:
        print(d)
    a = re.sub(".", "|", x)
    if a:
        print(a)
    e = re.sub(",", "|", x)
    if e:
        print(e)
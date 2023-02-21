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
# f = open("rox.txt", "r", encoding='utf-8')
# for x in f:
#     print(re.sub("[ ,.]", ":", x))
#7####################################################
# f = open("rox.txt", "r", encoding='utf-8')
# for x in f:
#     print(re.sub("[_]", "", x))
#8####################################################
# f = open("rox.txt", "r", encoding='utf-8')
# for x in f:
#     print(re.split("[A-Z]", x))
#9###################################################
# f = open("rox.txt", "r", encoding='utf-8')
# for x in f:
#     xa = re.sub(r"(\w)([A-Z])", r"\1 \2", x)
#     print(xa)
#10####################################################
d = open("rox.txt", "r", encoding = 'utf-8')
for i in d:
    def camel_to_snake(text):
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
    print(camel_to_snake(i))
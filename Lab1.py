
print("Hello Teacher")

#syntax
print("This is a syntax:")
if 6 < 2 :
    print("Six greater than two")
else:
    print("No, two less than six")
#-------------------------------
#This is my comment
#-----------------------------
#variebles
print("There are variables")
a = 5
b = "Apples"
print(a*b)
print("we have", a, b)
#--------------------------------
#global variables
print("There are global variables")
x = "The subject"
def myf():
    x = "PP2"
    print(x, "is great")
myf()
print(x, "is great")
#-------------------------------
#Data types
print("There are some Data types")
x = 5
print(type(x))

x = memoryview(bytes(785487451))
print(x)
print(type(x))

x = {"name" : "John", "age" : 36}
print(x)
print(type(x))

x = bytearray(8)
print(x)
print(type(x))
#---------------------------
#Number
print("There are numbers")
#random number
import random
x = random.randrange(1, 10)
print("Random number:", x)
x = 2.54
print("Float:", x)
x = 6
print("int:", x)
x= 5+98j
print("complex:", x)
#---------------------------------
#casting
print("There are casting")
x = 2.654
print("2.654 to int:", int(x))
x = "5"
print("5 str to int:", int(x))
#--------------------------------
#Strings
x = "abcdefg"
print("There are some strings")
print("lenth of abcdefg:", len(x))
txt = """One day i what to go New York, but I couldn't.
        I was not going anywhere. Not even to the moon,
        which was the only place I knew of that was safe from these monsters.
        So, I stayed in the house. My father was still in prison, though he"""
#This text genarated by AI from internet
if "monster" in txt:
  print("Yes, 'free' is present.")
#slising stings
b = "My name is Darkhan"
print(b[-5:-2])
#modify strings
print(b.upper())
#concatenat strings
a = "Darkhan"
b = "Tastanov"
c = a + " " + b
print(c)
#format string
quantity = 300
itemno = "Petrol"
price = 49.95
myorder = "I want to pay {2} dollars for {0} liters of item {1}."
print(myorder.format(quantity, itemno, price))
#Escape strings
txt = "\x44\x61\x72\x6B\x68\x61\x6E\x20\x54\x61\x73\x74\x61\x6E\x6F\x76" #HEX
print("Hello,",txt)
#string methods
txt = "banana"
x = txt.center(30)
print(x)

txt = "2bit"
x = txt.isalnum()
print("isalnum ? :",x)

myTuple = ("Darkhan", "Tastanov")
x = " ".join(myTuple)
print("Join:",x)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#------------------------------
#booleans
x = True
if x is True:
    print("Is True, WOW")

#-----------------------------------------
#Operators
print("while + +=:")
n = 3
i=0
while i < n:
    print(i)
    i += 1

#-----------------------------------------------
#lists
list1 = ["apple", "banana", "cherry"]
list1.append("melon")
print("We have",list1)
list1.pop(1)
print("We have", list1)

#list loop
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(i)

#Comprehension
newlist = [x for x in range(10) if x < 5]
print("newlist:",newlist)
#sort
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#


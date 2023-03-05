#While loops
#break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#-------------------
print("--------------------------------------")
#else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print(f"{i} is no longer less than 6")
#---------------------------------
print("------------------------------------")
#------------------------------------------
#list
#append
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)
#_______________________________
print("-9999989---------------")
#copy
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)
#-------------------------------
print("--------------------------------------------------")
#extend
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)
#---------------------------
print("----------------------------------------------")
#insert
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)
#==========================================]
print("====================================================")
#pop
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)
#-----------------------------------------------------
print("----------------------------------------")
#revers
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
#------------------------------------------------
print("--------------------------------------------------")
#sort revers, key
def myFunc(e):
  return e['year']
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(reverse=True, key=myFunc)
print(cars)
#------------------------------
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)
#---------------------------------------------------------------------
print("-------------------------------------------------------")
#rmove
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
#-----------------------------------------------------
print("---------------------------------------------------------------")
#for
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#-------------------------
print("----------------------------------------------")
#range

for x in range(2, 30, 3):
  print(x)
#----------------------------------
print("----------------------------------------------------------")
#else
for x in range(6):
  if x == 7: break
  print(x)
else:
  print("Finally finished!")
#n*m
print("-----------------------------------")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
#-----------------------------------
print("------------------------------------------------------------")
#tuples
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#---------------------------------------
print("-------------------------------------------------------")
#list and append (update tuple)
#---------------------------------------
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#-----------------------------------------------------
print("-------------------------------------------------------")
#tuple and key
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
#-----------------------------------------------------
print("-------------------------------------------------------")
#tuple and loops
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#-----------------------------------------------------
print("-------------------------------------------------------")
#set
#set and difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)
#-----------------------------------------------------
print("-------------------------------------------------------")
#dictionaries
#dic and direct element
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#-----------------------------------------------------
print("-------------------------------------------------------")
#dic more than 1 par
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
#-----------------------------------------------------
print("-------------------------------------------------------")
#dic and loop
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
for x in thisdict.keys():
  print(x)
for x, y in thisdict.items():
  print(x, y)
#-----------------------------------------------------
print("-------------------------------------------------------")
#dic and set
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
x = car.setdefault("color", "Brown")
print(x)
#-----------------------------------------------------
print("-------------------------------------------------------")
#dic and get
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }
print(car.get("model"))
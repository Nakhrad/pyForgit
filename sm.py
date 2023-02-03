x=1
months = {"Jan": [x while x in range(32) if x <= 31
                    x=x+1],
          "Feb": [x for x in range(32) if x <= 30],
        }
print(months)
a = int(input("Day:"))
v = months.find(a)
print(v)
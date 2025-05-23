son = int(input("Son kiriting: "))
y = 0
y1 = son % 10
while son != 0:
   y = son %10
   son = son // 10
   if y1 < y:
    y1 = y
print(y1)
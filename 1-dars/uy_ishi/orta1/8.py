son = int(input("Son kiriting: "))
h = 0
y = 0
while son != 0:
    y = son%10
    son = son // 10
    h+=1
print(h) 
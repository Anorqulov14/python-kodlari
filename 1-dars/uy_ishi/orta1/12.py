son = int(input("Son kiriting: "))
y = 0
y1 = 0
while son != 0:
    y = son%10
    if y == y1:
        print("bor")
    y1 = y
    son = son // 10
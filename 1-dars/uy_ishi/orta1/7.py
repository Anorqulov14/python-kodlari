a = int(input("Son kiriting: "))
b = int(input("Son kiriting: "))

for i in range(a,b+1):
    if i %2 == 0:
        print(i*(-1))
    else:
        print(i)
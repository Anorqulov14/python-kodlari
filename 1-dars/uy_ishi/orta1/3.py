son = int(input("Son kiriting: "))
y = son
teskari = 0 
while son > 0:
    qoldiq = son % 10
    teskari = teskari * 10 + qoldiq
    son //= 10

print(y - teskari)

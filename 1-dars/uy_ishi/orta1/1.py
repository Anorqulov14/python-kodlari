
y = 0

for i in range(1,501):
    if i %2 == 1:
        y += i

son = y
teskari = 0

while y > 0:
    qoldiq = y % 10
    teskari = teskari * 10 + qoldiq
    y //= 10

if son == teskari:
    print("Bu son palindrom.")
else:
    print("Bu son palindrom emas.")
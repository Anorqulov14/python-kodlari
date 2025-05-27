import random

sonlar = []
for i in range(20):
    son = random.randint(1,100)
    sonlar.append(son)


print(sum(sonlar) / len(sonlar))
# lst = [2,3,4,5,6,7,8,9,10,11,12]
lst = [0] * 11

for i in range(10_000):
    a = random.randint(1,6)
    b = random.randint(1,6)
    y = a + b
    lst[y-2] += 1

y = 0

for i in range(len(lst)):
    print(f"{i+2} sonni {lst[i]} martta uchradi")
    y += lst[i]
print(y)


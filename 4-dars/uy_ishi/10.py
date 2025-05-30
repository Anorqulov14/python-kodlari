set1 = {100, 20, 45, 80, 70, 50}
set2 = {30, 55, 70, 60, 32, 100}

for i in set1.copy():
    if i < 61:
        set1.remove(i)

for k in set2.copy():
    if k < 61:
        set2.remove(k)
y = 0

for l in set1.intersection(set2):
    y += l
print(y//2)

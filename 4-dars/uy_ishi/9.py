set1={2,3,4,5,6}
set2={4,5,6,7,8,9}

y = 0
for i in set1.difference(set2):
    y += i
for j in set2.difference(set1):
    y+=j
print(y)
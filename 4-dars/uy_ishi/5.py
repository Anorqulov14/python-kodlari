set1={4,5,6,7,8,9}	
set2={5,6,7,10,11}

y = 0

for i in set1.difference(set2):
    y += i
for j in set2.difference(set1):
    y += j

y1 = 0

for k in set1.intersection(set2):
    y1 += k
print(y - y1)
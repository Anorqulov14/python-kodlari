set1 = {1,2,3,4,5,6}	
set2 = {4,5,6,7,8,9}

y = 0
for i in set1.difference(set2):
    y += i
y1 = 0
for j in set1.intersection(set2):
    y1 += j

print(y1 - y)
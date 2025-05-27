son = [1,2,3,4,5]

y = 0
k = son[0]
soni = 0
for i in range(0,len(son)):
    y += son[i]
    if k < son[i]:
        k = son[i]
    if son[i] %2 == 1:
        soni +=1

print(f"{k} kattasi")
print(f"{y} yigindi")
print(f"{soni} toqlar soni")
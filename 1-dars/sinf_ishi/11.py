son = int(input("son kiriting: "))
y = 0
j=0
for i in range(1,1000000000000):
    if i*i > son:
        y = i*i
        j = i
        break

print(y // j)

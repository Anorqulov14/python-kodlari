a = 10 #int(input("son kiriting: "))
b = 20   #int(input("son kiriting: "))

sonlar = []

for i in range(a,b+1):
    if i %2 == 0:
        sonlar.append(i)

print(sonlar)
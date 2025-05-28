a = 10 #int(input("son kiriting: "))
b = 20   #int(input("son kiriting: "))

sonlar = []

for i in range(a,b+1):
    if i %2 == 1:
        sonlar.insert(0,i)

print(sonlar)
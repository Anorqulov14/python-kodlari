son = int(input("son kiriting: "))
y = 0
for i in range(1,son):
    if son % i == 0:
        y += i
if y == son :
    print("mukammal son")
else:
        print("mukammal son emas")

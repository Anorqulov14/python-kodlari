son = int(input("son kiriting: "))
son1 = int(input("son kiriting: "))
count = 0
for i in range(son1,son,-1):
    if i %2 == 1:
        print(i)
        count +=1
    if count == 3:
        break
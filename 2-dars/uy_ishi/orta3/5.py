son = int(input("son kiriting: "))
count = 0
while True :
    if son %2 == 0:
        son = son // 2
        count +=1
    else:
        break
print(count)
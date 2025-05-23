n = int(input("1 - son kiriting:  "))
m = int(input("2 - son kiriting:  "))
k = int(input("3 - son kiriting:  "))
y = 0
count = 0
for i in range(n,m+1):
    
    if i %2 == 0:
        y += i
        count += 1
        if count == k:
            break


print(y)
            
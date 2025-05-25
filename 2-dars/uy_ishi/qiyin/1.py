son = int(input("son kiriting: "))

for i in range(1,son+1):
    if son %i == 0:
        if i %2 == 1:
            print(i,end = " ")
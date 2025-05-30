lst = [1, 2, 33, 5, 6, 7, 7]
son = int(input("son kiriting: "))

for j in range(len(lst)):
    for i in range(j+1,len(lst)):
        if lst[j] + lst[i] == son:
            print(j,i)

    
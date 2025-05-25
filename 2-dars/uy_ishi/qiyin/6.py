son = int(input("son kiriting: "))

for i in range(1,son+1):
    for j in range(1,son+1):
       if i == 1 or j == 1 or  j >= son - i+1:
            print("*", end=" ")
       else:
            print(" ", end=" ")
    print()
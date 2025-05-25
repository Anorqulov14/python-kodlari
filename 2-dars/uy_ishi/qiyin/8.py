son = 10  #int(input("son kiriting: "))

for i in range(1,son+1):
    for j in range(1,son+1):
       if i == 1 or j == 1 or   i == son or j == son or i == son//2 or i == 4 or i == 3 or i == 2:
            print("*", end=" ")
       else:
            print(" ", end=" ")
    print() 
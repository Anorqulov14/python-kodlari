son = int(input("son kiriting: "))

for i in range(1, son + 1):
    print(" " * (son - i), end="")
    print("*" * (2 * i - 1))
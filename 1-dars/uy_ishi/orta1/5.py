
N = int(input("N: "))
M = int(input("M: "))
K = int(input("K: "))

a = 1
b = 0
count = 0 

print(f"{N} va {M} orasidagi {K} ta Fibonachchi sonlari:")

while count < K and a <= M:
    if N <= a <= M:
        print(a)
        count += 1
    a, b = b, a + b

import math

def binom(n, k):
    if 0 <= k <= n:
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    else:
        return 0 
print(binom(5,2))

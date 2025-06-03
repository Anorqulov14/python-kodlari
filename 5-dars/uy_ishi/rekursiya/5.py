def funk(n):
    if n == 0:
        return
    y = n%10
    funk(n//10)
    return y

print(funk(1234))


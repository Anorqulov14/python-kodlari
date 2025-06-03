def funk(n):
    if n == 0:
        return
    y = n%10
    funk(n//10)
    print(y,end=" ")

funk(123)
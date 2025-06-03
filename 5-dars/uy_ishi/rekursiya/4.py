def funk(n):
    if n == 0:
        return
    print(n%10,end=" ")
    funk(n//10)

funk(1234)
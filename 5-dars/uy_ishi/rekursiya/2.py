def funk(n):
    if n == 0:
        return
    funk(n-1)
    if n %2 == 1:
        print(n,end=" ")

funk(5)
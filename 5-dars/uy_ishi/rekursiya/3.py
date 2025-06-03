def funk(n):
    if n == 0:
        return
   
    if n %2 == 0:
        print(n,end=" ")
    funk(n-1)

funk(6)
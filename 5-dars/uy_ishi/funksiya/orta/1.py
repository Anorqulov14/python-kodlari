def raqamli_ildizi(son):
    if son >= 9:
        y = sum(int(i) for i in str(son))
    else:
        print(son)
    while y >= 9:
         y = sum(int(j) for j in str(y))
    return y
    

print(raqamli_ildizi(45893))
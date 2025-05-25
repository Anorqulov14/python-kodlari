n = int(input("son kiriting: "))

y = 0
h = n

while h > 0:
    raqam = h % 10        
    y += raqam  
    h //= 10                
print(n%y)
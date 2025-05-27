import random
y =0
sonlar = []
for i in range(5):
    son = random.randint(1,100)
    sonlar.append(son)
    y += sonlar[i]
print(sonlar)
print(y//5)

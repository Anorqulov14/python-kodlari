list1=['salom',123,True,'Hayr','world',3.14,'7214']

text = []
other = []

for i in list1:
    if isinstance(i, str):
        text.append(i)
    else:
        other.append(i)
text.sort()
print(f"Stringlar: {text}")
print(f"Boshqalar: {other}")
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d = {}

for key in set(d1) | set(d2):
    d[key] = d1.get(key, 0) + d2.get(key, 0)

print(d)

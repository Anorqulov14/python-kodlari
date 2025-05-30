nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
son2 = set()
for son in nums:
    if son%2==0:
        son2.add(son)

print(son2)
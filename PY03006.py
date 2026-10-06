import re
a = {}
n = int(input())
for i in range(n):
    for s in re.split("[^a-z]", input().lower()):
        if s != '':
            if a.get(s) is None: a[s] = 1
            else: a[s] += 1
ans = sorted(a, key=lambda x: (-a[x], x))
for i in ans: print(i, a[i])
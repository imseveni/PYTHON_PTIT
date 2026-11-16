import math

limit = math.isqrt(1000) + 1
f = [1] * 1001

f[0] = f[1] = 0
for i in range(2, limit):
    for j in range(i * i, 1001, i):
        if f[i] == 1:
            f[j] = 0

n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(f[a[i][j]], end = " ")
    print()
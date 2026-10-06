from math import *

N = 11000

f = [0] * N
f[0] = f[1] = 1
for i in range(2, int(sqrt(N))):
    if f[i] == 0:
        for j in range(i * i, N, i):
            f[j] = 1

primes = []
for i in range(N):
    if f[i] == 0:
        primes.append(i)

n = int(input())
arr = map(int, input().split())

ans = 0
for x in arr:
    if f[x] == 0:
        continue

    l, r, pos = 0, len(primes) - 1, 0
    while l <= r:
        mid = (l + r) // 2
        if primes[mid] < x:
            pos = mid
            l = mid + 1
        else:
            r = mid - 1

    ans = max(ans, min(x - primes[pos], primes[pos + 1] - x))

print(ans)
            
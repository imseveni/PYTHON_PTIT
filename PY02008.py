from math import *

N = 10000
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

n, x = map(int, input().split())

print(x, end = " ")
for i in range(n):
    print(x + primes[i], end = " ")
    x += primes[i]
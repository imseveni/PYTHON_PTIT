import math

n = int(input())

limit = math.isqrt(n)

prime = [True] * (limit + 1)

if limit >= 0:
    prime[0] = False
if limit >= 1:
    prime[1] = False

for i in range(2, math.isqrt(limit) + 1):
    if prime[i]:
        for j in range(i * i, limit + 1, i):
            prime[j] = False

primes = []

for i in range(2, limit + 1):
    if prime[i]:
        primes.append(i)

ans = 0

for p in primes:
    if p ** 8 <= n:
        ans += 1
    else:
        break

left = 0
right = len(primes) - 1

while left < right:
    if primes[left] * primes[right] <= limit:
        ans += right - left
        left += 1
    else:
        right -= 1

print(ans)
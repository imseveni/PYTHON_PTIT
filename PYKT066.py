import sys
from math import gcd

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)

T = next(it)

for _ in range(T):
    n = next(it)
    k = next(it)

    a = [next(it) for _ in range(n)]

    ans = n + 1

    for i in range(n):
        g = 0

        for j in range(i, n):
            g = gcd(g, a[j])

            if g == k:
                ans = min(ans, j - i + 1)
                break

            if g % k != 0:
                break

    if ans == n + 1:
        print(-1)
    else:
        print(ans)
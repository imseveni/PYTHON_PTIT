import sys
from math import isqrt, log, lcm

input = sys.stdin.readline

T = int(input())


def sang():
    N = 1000005

    isPrime = [True] * N
    isPrime[0] = isPrime[1] = False

    for i in range(2, isqrt(N)):
        if (isPrime[i]):
            for j in range(i * i, N, i):
                isPrime[j] = False
    Prime = []
    for i in range(2, N):
        if isPrime[i]:
            Prime += [i]

    return Prime


Prime = sang()
for _ in range(T):
    N = int(input())
    res = 1

    ans = []

    for x in Prime:
        if x > N:
            break
        k = 1
        cnt = 0
        while k <= N:
            k *= x
            cnt += 1
        k //= x

        cnt -= 1
        res *= k
    # print(ans)
    for c in str(res)[::-1]:
        if (c != "0"):
            print(c)
            break


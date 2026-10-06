from math import *

MOD = 10**9 + 7

n, m = map(int, input().split())

arr = list(map(int, input().split()))

k = m - sum(arr)

if(k < 0):
     print(0)
else:
    print(comb(n + k - 1, k) % MOD)




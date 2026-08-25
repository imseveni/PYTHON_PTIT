from math import *

def solve():
    n = int(input())

    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    dp = {0: 0}
    for i in range(n):
        new_dp = dict(dp)
        for cur_gcd, cur_cost in dp.items():
            next_gcd = gcd(cur_gcd, a[i])
            next_cost = cur_cost + c[i]

            if(next_gcd not in new_dp or next_cost < new_dp[next_gcd]):
                new_dp[next_gcd] = next_cost

        dp = new_dp

    if 1 in dp:
            print(dp[1])
    else:
        print(-1)

if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
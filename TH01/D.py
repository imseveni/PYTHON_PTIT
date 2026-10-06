from math import *

def solve():
    n = input()

    a = int(n)
    b = int(n[::-1])

    ucln = gcd(a, b)
    if(ucln == 1):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
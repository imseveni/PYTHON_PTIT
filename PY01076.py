from math import gcd

def solve():
    t = int(input())
    for _ in range(t):
        a = int(input())
        b = int(input())
        print(gcd(a, b))

if __name__ == '__main__':
    solve()
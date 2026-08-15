from math import *

def ngto(n):
    if n < 2:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10 

    return total

def solve():
    T = int(input())

    for _ in range(T):
        a, b = map(int, input().split())

        ucln = gcd(a, b)

        if ngto(sum_digits(ucln)):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
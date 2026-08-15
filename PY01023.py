from math import *

def calc(n):
    print(1, end = "")

    for i in range (2, int(sqrt(n)) + 1):
        if(n % i == 0):
            count = 0
            while(n % i == 0):
                count += 1
                n //= i

            print(" * ", i, '^', count, sep = "", end = "")

    if(n > 1):
        print(" * ", n, '^', 1, sep = "", end = "")

    print()

def solve():
    n = int(input())

    calc(n)

if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
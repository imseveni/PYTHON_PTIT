from math import *

def ngto(n):
    if(n < 2):
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if(n % i == 0):
            return False

    return True

def solve():
    n = input()

    x = int(n[-4::])
    if(ngto(x)):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
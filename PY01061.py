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

    front = int(n[:3:])
    end = int(n[-3::])

    if(ngto(front) and ngto(end)):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
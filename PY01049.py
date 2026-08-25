from math import *

def ngto(x):
    if(x < 2):
        return False
        
    for i in range(2, int(sqrt(x)) + 1):
        if(x % i == 0):
            return False

    return True

def solve():
    n = input()

    length = len(n)
    if(ngto(length) == False):
        print("NO")
        return

    count = 0
    for c in n:
        x = int(c)
        if(ngto(x)):
            count += 1

    if(count > length / 2):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
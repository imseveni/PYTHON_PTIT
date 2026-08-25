from math import *

def solve():
    n = input()

    x = int(n[-4::])

    if(x < 2):
        print("NO")
        return
    
    for i in range(2, int(sqrt(x)) + 1):
        if(x % i == 0):
            print("NO")
            return

    print("YES")

if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
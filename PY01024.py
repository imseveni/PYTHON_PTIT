from math import *

def solve():
    n = input()

    total = sum(int(c) for c in n)

    if(total % 10):
        print("NO")
        return

    for i in range(1, len(n)):
        if(abs(int(n[i]) - int(n[i - 1])) != 2):
           print("NO")
           return

    print("YES")

if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
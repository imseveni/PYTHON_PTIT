from math import *

def solve():
    n = input()

    total = 0
    for i in range(len(n)):
        x = int(n[i])
        if(i % 2 == 0 and x % 2 == 1):
            print("NO")
            return
        if(i % 2 == 1 and x % 2 == 0):
            print("NO")
            return

        total += int(x)

    if(total < 2):
        print("NO")
        return

    for i in range(2, int(sqrt(total)) + 1):
        if(total % i == 0):
            print("NO")
            return

    print("YES")


if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
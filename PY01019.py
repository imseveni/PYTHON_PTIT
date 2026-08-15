from math import *

def check(s1, s2):
    n = len(s1)
    for i in range(1, n):
        a = abs(ord(s1[i]) - ord(s1[i - 1]))
        b = abs(ord(s2[i]) - ord(s2[i - 1]))

        if(a != b):
            print("NO")
            return

    print("YES")

def solve():
    T = int(input())

    for _ in range(T):
        s1 = input()
        s2 = s1[::-1]

        check(s1, s2)

if __name__ == "__main__":
    solve()
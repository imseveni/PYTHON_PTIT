from math import *

def solve():
    n = input()

    count = 0
    while(True):
        total = sum(ord(c) - ord('0') for c in n)

        count += 1

        n = str(total)

        if(len(n) == 1):
            break
        
    print(count)

if __name__ == "__main__":
    T = 1
    #T = int(input())

    for _ in range(T):
        solve()
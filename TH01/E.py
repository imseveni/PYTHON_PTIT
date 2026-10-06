from math import *

def solve():
    n, k = map(int, input().split());

    start = int(pow(10, k - 1))
    end = int(pow(10, k))

    count = 0
    for i in range (start, end):
        if(gcd(i, n) == 1):
            if(count != 10):
                print(i, end = " ")
            else:
                print('\n', i, sep = "", end = " ")
                count = 0;
            count += 1

if __name__ == "__main__":
    T = 1
    # T = int(input())

    for _ in range(T):
        solve()
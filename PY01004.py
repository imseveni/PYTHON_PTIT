import sys
from math import *

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solve():
    input_data = sys.stdin.read().split()

    t = int(input_data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(input_data[i])

        cnt = 0
        for k in range(1, n):
            if gcd(n, k) == 1:
                cnt += 1

        if is_prime(cnt):
            results.append("YES")
        else:
            results.append("NO")
        
    print("\n".join(results))

if __name__ == "__main__":
    solve()
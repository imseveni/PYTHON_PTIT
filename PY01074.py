import sys
from math import *

MAX_VAL = 2000001
sum_prime = [0] * MAX_VAL

for i in range(2, int(MAX_VAL**0.5) + 1):
    if sum_prime[i] == 0:
        for j in range(i * i, MAX_VAL, i):
            if sum_prime[j] == 0:
                sum_prime[j] = i

for i in range(2, MAX_VAL):
    if sum_prime[i] == 0:
        sum_prime[i] = i
    else:
        p = sum_prime[i]
        sum_prime[i] = p + sum_prime[i // p]

input_data = sys.stdin.read().split()
T = int(input_data[0])

queries = [int(x) for x in input_data[1:T + 1]]

total = 0
for n in queries:
    total += sum_prime[n]

print(total)

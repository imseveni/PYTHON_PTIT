# Một số được gọi là đặc biệt nếu như tổng các chữ số của nó là một số nguyên tố. 
# Cho số tự nhiên N, hãy đếm số cặp (x, y) nguyên dương thỏa mãn 
# x, y là số đặc biệt và 
# x + 2y = N.
# 
# Input:
# Dữ liệu đầu vào chứa một số nguyên dương N (1<= N <= 10^15).
# 
# Output:
# In ra số cặp (x, y) thỏa mãn yêu cầu của đề bài.

from collections import defaultdict


def sieve(n):
    prime = [True] * (n + 1)

    prime[0] = False
    if n >= 1:
        prime[1] = False

    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return prime

N = int(input())

digits = list(map(int, str(N)[::-1]))

L = len(digits)

MAX_SUM = 9 * L

prime = sieve(MAX_SUM)

dp = {(0, 0, 0) : 1}

for digitN in digits:
    new_dp = defaultdict(int)

    for (carry, sumX, sumY), ways in dp.items():
        for digitY in range(10):
            digitX = (digitN - 2 * digitY - carry) % 10

            total = digitX + 2 * digitY + carry

            new_carry = total // 10

            new_dp[(new_carry, sumX + digitX, sumY + digitY)] += ways

    dp = new_dp

ans = 0

for (carry, sumX, sumY), ways in dp.items():
    if carry == 0 and prime[sumX] and prime[sumY]:
        ans += ways

print(ans)
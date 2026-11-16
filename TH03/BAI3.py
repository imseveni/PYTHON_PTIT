# Cho số nguyên N. 
# Nhiệm vụ của bạn là hãy xác định xem các số trong phạm vi từ 0 tới N
# có bao nhiêu số mà biểu diễn nhị phân của nó có đúng K chữ số 0.
# 
# Ví dụ N = 20, K = 3, ta có
# 8 = 10001
# 7 = 10001
# 18 = 10010
# 20 = 10100
# 
# Input:
# Dòng đầu tiên là số lượng bộ test T (T <= 20).
# Mỗi test gồm hai số nguyên N và K (0<= N < 2^31, 1 <= K <= 31).
# 
# Output:
# Với mỗi test, in ra số lượng các số thỏa mãn có K bit 0.

from functools import lru_cache


def solve(n, k):
    bits = bin(n)[2:]
    m = len(bits)

    @lru_cache(None)
    def dp(pos, zero, tight, started):
        if pos == m:
            if not started:
                return 1 if k == 1 else 0

            return 1 if zero == k else 0

        if zero > k:
            return 0

        limit = int(bits[pos]) if tight else 1

        ans = 0

        for bit in range(limit + 1):
            new_tight = tight and (bit == limit)

            if not started and bit == 0:
                ans += dp(pos + 1, zero, new_tight, False)

            else:
                new_zero = zero

                if bit == 0:
                    new_zero += 1

                ans += dp(pos + 1, new_zero, new_tight, True)

        return ans

    return dp(0, 0, True, False)

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(solve(n, k))
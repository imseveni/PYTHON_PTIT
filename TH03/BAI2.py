# Theo quan niệm Á Đông, số 6 và 8 đọc là lục, bát, 
# do vậy người ta hay liên tưởng tới lộc phát, là phát tài phát lộc.
# Nhiệm vụ của bạn là hãy xác định xem trong các số từ 1 -> N và 
# chia hết cho 8, tức dãy số 8, 16, 24, 32, … , tổng số lần xuất hiện chữ số 6 và 8 là bao nhiêu?
# 
# Input:
# Dòng đầu tiên là số lượng bộ test T (T <= 100 000).
# Mỗi test gồm một số nguyên dương N (1 <= N <= 10^18)
# 
# Output:
# Với mỗi test, in ra đáp án tìm được trên một dòng.

def cnt68(x):
    s = str(x)
    return s.count('6') + s.count('8')

pref = []

s = 0
for i in range(125):
    s += cnt68(i * 8)
    pref.append(s)

BLOCK = pref[-1]

def count_digit(n):
    if n < 0:
        return 0

    ans = 0
    p = 1

    while p <= n:
        high = n // (p * 10)
        cur = (n // p) % 10
        low = n % p

        for d in (6, 8):
            ans += high * p

            if cur > d:
                ans += p
            elif cur == d:
                ans += low + 1

        p *= 10

    return ans

for _ in range(int(input())):
    n = int(input())

    q = n // 1000
    r = n % 1000

    ans = 0

    ans += 125 * count_digit(q - 1)

    ans += q * BLOCK

    last = r // 8

    ans += (last + 1) * cnt68(q)

    ans += pref[last]

    print(ans)
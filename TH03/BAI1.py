# Cho 2 số nguyên dương N, M và xâu s. 
# Hãy đếm số lượng các xâu t có độ dài bằng N và xâu s là xâu con của t.
# 
# Input:
# Dòng đầu tiên là số lượng bộ test (T ≤ 20).
# Mỗi bộ test bắt đầu bởi 2 số N và M (N, M ≤ 10^12).
# Dòng tiếp theo là xâu s có độ dài không quá 50 kí tự, chỉ gồm các chữ cái thường.
# 
# Output:
# Với mỗi test, in ra đáp án tìm được theo modulo M.

def mul(a, b, c, mod):
    n = len(c)
    d = [0] * (2 * n - 1)

    for i in range(n):
        if a[i]:
            for j in range(n):
                d[i + j] = (d[i + j] + a[i] * b[j]) % mod

    for i in range(2 * n - 2, n - 1, -1):
        if d[i]:
            for j in range(n):
                d[i - 1 - j] = (d[i - 1 - j] + d[i] * c[j]) % mod

    return d[:n]


def calc(n, a, c, mod):
    k = len(c)
    if n < k:
        return a[n] % mod

    x = [0] * k
    if k == 1:
        x[0] = c[0]
    else:
        x[1] = 1

    res = [0] * k
    res[0] = 1 % mod

    while n:
        if n & 1:
            res = mul(res, x, c, mod)
        x = mul(x, x, c, mod)
        n >>= 1

    return sum(res[i] * a[i] for i in range(k)) % mod


def solve(N, M, s):
    m = len(s)

    if N < m:
        return 0

    C = [0] * m
    C[0] = 1

    for i in range(1, m):
        if s[i:] == s[:m-i]:
            C[i] = 1

    Q = [0] * (m + 2)

    for i in range(m):
        Q[i] += C[i]
        Q[i + 1] -= 26 * C[i]

    Q[m] += 1

    d = m + 1
    c = [(-Q[i]) % M for i in range(1, d + 1)]

    a = [0] * d
    a[0] = 1 % M

    for i in range(1, d):
        for j in range(26):
            k = 0
            ch = chr(ord('a') + j)
            while k < m and s[k] != ch:
                k += 1
            if k < m:
                pass

        dp = [0] * m
        if i == 1:
            dp[0] = 26 % M
            for j in range(m):
                pass

    dp = [0] * m
    dp[0] = 1 % M
    for i in range(1, d):
        ndp = [0] * m
        for j in range(m):
            if dp[j] == 0:
                continue
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                k = j
                while k and s[k] != ch:
                    k = 0
                if s[k] == ch:
                    k += 1
                if k < m:
                    ndp[k] = (ndp[k] + dp[j]) % M
        a[i] = sum(ndp) % M
        dp = ndp

    khong = calc(N, a, c, M)
    return (pow(26, N, M) - khong) % M


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    s = input().strip()
    print(solve(N, M, s))
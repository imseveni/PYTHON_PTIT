def is_palindromic(x, k):
    temp = x
    rev = 0
    while temp > 0:
        rev = rev * k + (temp % k)
        temp //= k
    return rev == x

a, b, m = map(int, input().split())

palindromes_base2 = []

for x in (0, 1):
    if a <= x <= b:
        palindromes_base2.append(x)

for length in range(1, 22):
    half_len = (length + 1) // 2
    start = 1 << (half_len - 1)
    end = 1 << half_len

    for prefix in range(start, end):
        s = bin(prefix)[2:]

        if length % 2 == 0:
            full_s = s + s[::-1]
        else:
            full_s = s + s[:-1][::-1]
        
        val = int(full_s, 2)
        if val > b:
            continue
        if val >= a and val > 1:
            palindromes_base2.append(val)

count = 0
for val in palindromes_base2:
    if val <= 1:
        count += 1
        continue

    limit_k = min(m, val)
    ok = True
    for k in range(3, limit_k + 1):
        if not is_palindromic(val, k):
            ok = False
            break
    if ok:
        count += 1

print(count)
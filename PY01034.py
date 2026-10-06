T = int(input())
for _ in range(T):
    s = list(input())
    n = len(s)

    i = n - 2
    while i >= 0 and s[i] <= s[i + 1]:
        i -= 1

    if i < 0:
        print(-1)
        continue

    best_j = -1
    for j in range(i + 1, n):
        if s[j] < s[i]:
            if best_j == -1 or s[j] > s[best_j]:
                best_j = j

    s[i], s[best_j] = s[best_j], s[i]

    if s[0] == '0':
        print(-1)
    else:
        print("".join(s))

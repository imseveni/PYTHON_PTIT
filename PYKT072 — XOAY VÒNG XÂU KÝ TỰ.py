n = int(input())

a = []
for _ in range(n):
    a.append(input().strip())

m = len(a[0])

ans = 10**9

for target in a:
    total = 0
    ok = True

    for s in a:
        cur = s
        found = False

        for cnt in range(m):
            if cur == target:
                total += cnt
                found = True
                break

            cur = cur[1:] + cur[0]

        if not found:
            ok = False
            break

    if ok:
        ans = min(ans, total)

if ans == 10**9:
    print(-1)
else:
    print(ans)
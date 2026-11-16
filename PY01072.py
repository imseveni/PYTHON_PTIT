n, k = map(int, input().split())

a = list(map(int, input().split()))

s = sorted(set(a))
m = len(s)
ans = [0] * k

def In():
    print(*ans)

def Try(i, start):
    if i == k:
        In()
        return

    for j in range(start, m):
        ans[i] = s[j]
        Try(i + 1, j + 1)

Try(0, 0)
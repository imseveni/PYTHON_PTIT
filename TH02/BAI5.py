n = int(input())
a = [0] * (n + 1)
for i in range(n - 1):
    u, v = map(int, input().split())
    a[u] += 1
    a[v] += 1
cnt = 0
for i in range(n + 1): cnt += 1 if a[i] == 1 else 0
print("Yes" if cnt == n - 1 else "No")
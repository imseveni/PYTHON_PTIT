import sys

n = int(input())
m = int(input())

a = [[0] * (n + 1) for i in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    a[u][v] = 1
    a[v][u] = 1

x = [0] * (n + 1)

for i in range(2, n + 1):
    x[i] = 1 ^ a[1][i]

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        edge = a[i][j] ^ x[i] ^ x[j]

        if edge == 0:
            print("NO")
            sys.exit()

print("YES")
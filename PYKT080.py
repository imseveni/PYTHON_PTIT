n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

mark = [[0] * m for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == -1:

            for dx in range(-1, 2):
                for dy in range(-1, 2):

                    if dx == 0 and dy == 0:
                        continue

                    x = i + dx
                    y = j + dy

                    if 0 <= x < n and 0 <= y < m and mark[x][y] == 0:
                            ans += a[x][y]
                            mark[x][y] = 1

print(ans)
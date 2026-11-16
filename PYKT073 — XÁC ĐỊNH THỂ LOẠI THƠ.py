n = int(input())

a = []
for _ in range(n):
    a.append(input().split())

ans = []

i = 0

while i < n:
    if len(a[i]) == 7:
        ans.append(2)
        i += 4

    else:
        ans.append(1)

        while i < n and len(a[i]) == 6:
            i += 2

print(len(ans))

for x in ans:
    print(x)
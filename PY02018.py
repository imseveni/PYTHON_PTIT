n = int(input())
arr = list(map(int, input().split()))

arr.sort()

ans = 1
for x in arr:
    if x > ans:
        break
    elif x == ans:
        ans += 1

print(ans)
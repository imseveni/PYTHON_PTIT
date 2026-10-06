n = int(input())

arr = list(map(int, input().split()))

ans = float('inf')
val = 0
for i  in range(n):
    total = 0
    for j in range(n):
        total += abs(arr[i] - arr[j])
    if ans > total:
        ans = total
        val = arr[i]

print(ans, val)
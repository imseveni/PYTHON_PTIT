T = int(input())
for _ in range(T):
    n = int(input())

    arr = list(map(int, input().split()))

    maxVal = max(x for x in arr)

    count = [0] * (maxVal + 1)
    maxCount, val = 0, 0
    for x in arr:
        count[x] += 1
        if count[x] > maxCount:
            maxCount = count[x]
            val = x
        elif count[x] == maxCount:
            if x < val:
                val = x

    if maxCount > (n // 2):
        print(val)
    else:
        print("NO")


T = int(input())
for _ in range(T):
    n = int(input())

    count = [0] * 1005
    maxCnt = 0
    val = 1001
    for i in range(n):
        x = int(input())
        count[x] += 1

        if count[x] > maxCnt:
            maxCnt = count[x]
            val = x
        elif count[x] == maxCnt:
            if(x < val):
                val = x

    print(val)
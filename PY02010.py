while True:
    n = int(input())
    if n == 0:
        break

    start = int(input())
    minVal = maxVal = start
    for _ in range(n - 1):
        x = int(input())

        if x > maxVal:
            maxVal = x

        if x < minVal:
            minVal = x

    if(minVal == maxVal):
        print("BANG NHAU")
    else:
        print(minVal, maxVal)
        
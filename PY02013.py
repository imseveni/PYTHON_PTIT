while True:
    n = int(input())
    if n == 0:
        break

    count = {n}
    while n != 1:
        if n % 2 == 0:
            n /= 2
            count.add(n)
        else:
            n = n * 3 + 1
            count.add(n)

    print(len(count))
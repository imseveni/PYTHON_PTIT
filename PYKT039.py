for t in range(int(input())):
    n = int(input())

    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))

    check = True
    for i in range(n):
        if a[i] > b[i]:
            check = False

    if check:
        print("YES")
    else:
        print("NO")
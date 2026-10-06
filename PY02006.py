T = int(input())
for _ in range(T):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    check = True
    for i in range(n):
        if a[i] > b[i]:
            check = False
            break

    if(check == True):
        print("YES")
    else:
        print("NO")
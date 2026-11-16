T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    i = j = p = 0
    ok = False
    while i < n and j < m and p < k:
        if a[i] == b[j] == c[p]:
            print(a[i], end = " ")
            ok = True
            i += 1
            j += 1
            p += 1
        else:
            mn = min(a[i], b[j], c[p])

            if(a[i] == mn):
                i += 1
            if(b[j] == mn):
                j += 1
            if(c[p] == mn):
                p += 1

    if(ok == False):
        print("NO")
    else:
        print()
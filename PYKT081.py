T = int(input())

for _ in range(T):
    s = input().split('.')

    check = True

    if len(s) != 4:
        check = False
    else:
        for x in s:
            if not x.isdigit():
                check = False
                break

            x = int(x)

            if x < 0 or x > 255:
                check = False
                break

    if check:
        print("YES")
    else:
        print("NO")
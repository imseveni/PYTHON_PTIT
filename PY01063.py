T = int(input())
for _ in range(T):
    s = list(input())
    n = list(input())

    ans = 0
    i = 0
    while i <= len(s) - len(n):
        if s[i] == n[0]:
            exist = False
            j = 0
            while j < len(n):
                if s[i + j] != n[j]:
                    exist = True
                    break
                j += 1

            if exist == False:
                ans += 1
                i = i + j - 1

        i += 1

    print(ans)
                

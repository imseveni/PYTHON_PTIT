def calc(s1):
    s2 = s1[::-1]
    
    for i in range(len(s1) - 1):
        d1 = abs(ord(s1[i]) - ord(s1[i + 1]))
        d2 = abs(ord(s2[i]) - ord(s2[i + 1]))

        if d1 != d2:
            print("NO")
            return

    print("YES")

T = int(input())
for _ in range(T):
    s1 = input()
    calc(s1)
    
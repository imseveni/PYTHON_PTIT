def solve():
    s1 = input()
    s2 = s1[::-1]

    for i in range(1, len(s1)):
        x = abs(ord(s1[i]) - ord(s1[i - 1]))
        y = abs(ord(s2[i]) - ord(s2[i - 1]))

        if(x != y):
            print("NO")
            return

    print("YES")

if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
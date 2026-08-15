def solve():
    n = input()

    ans = ""
    count = 0

    for i in range(len(n) -1, -1, -1):
        ans += n[i]

        count += 1
        if(i and count == 3):
            ans += ','
            count = 0

    print(ans[::-1])

if __name__ == "__main__":
    T = 1
    # T = int(input())

    for _ in range(T):
        solve()
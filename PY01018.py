def solve():
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

    while True:
        line = input().split()

        K = int(line[0])
        if(K == 0):
            break

        str = line[1]

        ans = ""
        for c in str:
            ans += P[(P.index(c) + K) % 28]

        print(ans[::-1])


if __name__ == "__main__":
    solve()
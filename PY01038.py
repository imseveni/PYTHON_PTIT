def solve():
    n = input()
    temp = int(n)

    count = 0
    while(count < 1000):
        if(temp % 7 == 0):
            print(n)
            return

        re_n = n[::-1]
        re_temp = int(re_n)

        temp += re_temp
        n = str(temp)

        count += 1

    print(-1)


if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
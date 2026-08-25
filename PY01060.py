def solve():
    n = input()

    even = odd = 0
    for i in range(len(n)):
        if(i % 2 == 0):
            if(n[i] != '0'):
                if(even == 0):
                    even += int(n[i])
                else:
                    even *= int(n[i])
        else:
            odd += int(n[i])

    print(even, odd)


if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
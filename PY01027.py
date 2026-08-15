def solve():
    n = input()

    c6 = n.count('6')
    c8 = n.count('8')

    if(c6 + c8 != len(n)):
        print("NO")
        return

    count = 0
    for c in n:
        if(c == '8'):
            if(count):
                count -= 1
            else:
                print("NO")
                return
        else:
            count = 2

    print("YES")


if __name__ == "__main__":
    T = 1
    # T = int(input())

    for _ in range(T):
        solve()
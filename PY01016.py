def solve():
    T = int(input())

    for _ in range(T):
        str = input()

        for i in range(len(str)):
            if(str[i].isdigit()):
                n = int(str[i])
                print(str[i - 1] * n, end = "")

        print()

if __name__ == "__main__":
    solve()
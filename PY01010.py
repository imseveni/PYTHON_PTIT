def solve():
    T = int(input())

    for _ in range(T):
        str = input()

        if(str[:2] == str[-2:]):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
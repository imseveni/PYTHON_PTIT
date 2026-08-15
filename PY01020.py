def solve():
    str = input()

    if(str[-2:] == "86"):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
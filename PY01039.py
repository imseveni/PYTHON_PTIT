def solve():
    n = input()

    x = n[0]
    for i in range(0, len(n), 2):
        if(n[i] != x):
            print("NO")
            return

    x = n[1]
    for i in range(1, len(n), 2):
        if(n[i] != x):
            print("NO")
            return

    print("YES")

if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
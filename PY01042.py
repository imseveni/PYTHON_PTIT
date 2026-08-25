def solve():
    n = input()

    for c in n:
        if(c != '0' and c != '1' and c != '2'):
            print("NO")
            return

    print("YES")

if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
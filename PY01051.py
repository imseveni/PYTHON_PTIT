def solve():
    n = input()

    total = 0
    for c in n:
        total += int(c)

    x = str(total)

    if(len(x) < 2):
        print("NO")
        return

    if(x == x[::-1]):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
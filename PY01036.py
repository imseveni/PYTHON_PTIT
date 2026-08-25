def solve():
    n = int(input())

    ans = 0
    if(n % 2):
        for i in range(1, n + 1, 2):
            ans += float(1) / i
    else:
        for i in range(2, n + 1, 2):
            ans += float(1) / i

    print(f"{ans:.6f}")

if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
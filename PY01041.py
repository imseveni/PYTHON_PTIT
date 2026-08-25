def solve():
    n = input()

    i = 0
    while(i + 1 < len(n) and n[i] < n[i + 1]):
        i += 1

    if(i + 1 == len(n) or n[i] == n[i + 1]):
        print("NO")
        return

    while(i + 1 < len(n) and n[i] > n[i + 1]):
        i += 1

    if(i + 1 != len(n)):
        print("NO")
        return

    print("YES")


if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
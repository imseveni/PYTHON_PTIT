def check(n):
    for i in range(0, len(n) - 1):
        if(n[i] > n[i + 1]):
            print("NO")
            return

    print("YES")

def solve():
    T = int(input())

    for _ in range(T):
        n = input()
        check(n)

if __name__ == "__main__":
    solve()
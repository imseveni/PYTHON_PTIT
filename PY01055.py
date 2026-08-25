def solve():
    n = input()

    if(len(n) == 1):
        print("YES")
    elif(len(n) % 2 == 0 or n[0] == n[1]):
        print("NO")
    else:
        for i in range(0, len(n), 2):
            if(n[i] != n[0]):
                print("NO")
                return

        print("YES")

if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
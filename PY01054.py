def solve():
    n = input()

    total = 1
    for c in n:
        if(c != '0'):
            total *= int(c)

    print(total)

if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
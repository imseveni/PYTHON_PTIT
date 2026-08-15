def solve():
    s1 = input()
    s2 = input()
    p = int(input())

    print(s1[:p - 1], s2, s1[p - 1:], sep = "")

if __name__ == "__main__":
    solve()
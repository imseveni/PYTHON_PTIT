def solve():
    s = input()

    str = ""
    sum = 0

    for c in s:
        if(c.isdigit()):
            sum += int(c)
        else:
            str += c

    res = "".join(sorted(str))
    print(res, sum, sep = "")

if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()
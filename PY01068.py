n, k = map(int, input().split())
s = sorted(list(set(input().split())))
res = [""] * k

def In():
    for i in range(k):
        print(res[i], end = " ")
    print()

def calc(i, start):
    if i == k:
        In()
        return

    for j in range(start, len(s)):
        res[i] = s[j]
        calc(i + 1, j + 1)

calc(0, 0)
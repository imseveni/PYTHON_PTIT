s = input()

n = len(s)

ans = [''] * n
used = []

def In():
    print(''.join(ans))

def Try(i):
    if i == n:
        In()
        return

    for j in range(n):
        if j not in used:
            ans[i] = s[j]
            used.append(j)
            Try(i + 1)
            used.pop()

Try(0)

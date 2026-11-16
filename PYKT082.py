import math

T = int(input())

def score(n):
    if n < 3: return 1
    elif n < 5: return 2.5
    elif n < 7: return 3
    elif n < 10: return 3.5
    elif n < 13: return 4
    elif n < 16: return 4.5
    elif n < 20: return 5
    elif n < 23: return 5.5
    elif n < 27: return 6
    elif n < 30: return 6.5
    elif n < 33: return 7
    elif n < 35: return 7.5
    elif n < 37: return 8
    elif n < 39: return 8.5
    else: return 9


for _ in range(T):
    a, b, c, d = map(float, input().split())

    a = score(a)
    b = score(b)

    ans = (a + b + c + d) / 4

    ans = math.floor(ans * 2 + 0.5) / 2

    print(ans)

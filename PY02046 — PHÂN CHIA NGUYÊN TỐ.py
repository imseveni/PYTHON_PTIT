import math

def ngto(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


n = int(input())
a = list(dict.fromkeys(map(int, input().split())))
m = len(a)

pre = [0] * (m + 1)
for i in range(1, m + 1):
    pre[i] = pre[i - 1] + a[i - 1]

found = False
for i in range(1, m):
    if ngto(pre[i]) and ngto(pre[m] - pre[i]):
        print(i - 1)
        found = True
        break

if not found:
    print("NOT FOUND")
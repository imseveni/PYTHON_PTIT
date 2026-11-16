n = int(input())

a = sorted(map(float, input().split()))

i = 1
while a[0] == a[i] and i < n:
    i += 1

j = n - 1
while a[n - 1] == a[j] and j >= 0:
    j -= 1

total = sum(a[k] for k in range(i, j + 1)) / (j - i + 1)
print("%.2f" % total)


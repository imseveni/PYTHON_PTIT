from collections import Counter

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    freq = Counter(arr)

    for val, cnt in freq.items():
        if cnt % 2 == 1:
            print(val)
            break
# Cho dãy số A[] có N phần tử. 
# Bạn cần đếm số cách phân hoạch A thành 3 tập hợp con, 
# sao cho tổng các phần tử trong mỗi tập hợp con là bằng nhau.
# 
# Input:
# Dòng đầu tiên là số lượng bộ test (T ≤ 10).
# Mỗi test bắt đầu bởi số nguyên N (N ≤ 15)
# Dòng tiếp theo gồm N số nguyên dương A[i] (1 ≤ A[i] ≤ 106).
# 
# Output:
# Với mỗi test, in ra đáp án tìm được trên một dòng.

from collections import defaultdict


def gen(a):
    d = defaultdict(int)
    n = len(a)

    def backtrack(i, s1, s2):
        if i == n:
            d[(s1, s2)] += 1
            return
        
        backtrack(i + 1, s1 + a[i], s2)

        backtrack(i + 1, s1, s2 + a[i])

        backtrack(i + 1, s1, s2)

    backtrack(0, 0, 0)

    return d

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(a)

    if total % 3 != 0:
        print(0)
        continue

    target = total // 3

    mid = n // 2

    left = gen(a[:mid])
    right = gen(a[mid:])

    ans = 0

    for (s1, s2), cnt in left.items():
        need1 = target - s1
        need2 = target - s2

        ans += cnt * right.get((need1, need2), 0)

    print(ans)
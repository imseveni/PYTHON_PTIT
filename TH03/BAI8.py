# Trên thượng lưu sông High River, một con đập lớn đang được xây dựng. 
# Do dòng sông chảy xiết, các kĩ sư thiết kế N bức tường chắn nước tại các vị trí L[i], 
# có độ cao tương ứng bằng H[i]. 
# Thiết diện mặt cắt của con đập được biểu diễn như hình vẽ. 
# Mỗi bức tường có độ dày bằng 1 đơn vị.
# Do tính phức tạp của con đập, một số bức tường vẫn đang được xây dựng tiếp theo ở phía dưới. 
# Do đó, các kĩ sư cần có hệ thống cảnh báo để xác định giới hạn vùng an toàn cho công việc xây dựng ở phía sau.
# Giả sử lưu lượng nước đổ về là K đơn vị thể tích. 
# Các bạn giúp các kĩ sư hãy tính toán xem vị trí bức tường cuối cùng sẽ bị nước tràn qua?
#
# Input
# Dòng đầu tiên là số lượng bộ test T (T <= 20).
# Mỗi test bắt đầu bởi số lượng bức tường N (N <= 10^5).
# Dòng thứ hai gồm N số nguyên L[] mô tả vị trí của các bức tường 
# (1 <= L[i] <= 10^9, L[i] > L[i-1]+1).
# Dòng thứ ba gồm N số nguyên H[] mô tả chiều cao của các bức tường (1 <= H[i] <= 10^5).
# Tiếp theo là số lượng truy vấn Q (Q <= 10^5).
# Q dòng tiếp theo, mỗi dòng gồm một số nguyên K (1 <= K <= 10^15).
# 
# Output
# Với mỗi truy vấn, hãy in ra đáp án trên một dòng. 
# Nếu bức tường thứ nhất không bị vượt qua, in ra 0.

import sys
from bisect import bisect_left

data = sys.stdin.buffer.read().split()
it = iter(data)

T = int(next(it))

def binary_search(A, n, k):
    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2

        if A[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return right

for _ in range(T):
    n = int(next(it))

    L = [0] + [int(next(it)) for _ in range(n)]
    H = [0] + [int(next(it)) for _ in range(n)]

    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + H[i]

    A = [0] * (n + 1)

    L[0] = -1
    H[0] = 100005

    stack = [0]

    for i in range(1, n + 1):
        while H[stack[-1]] < H[i]:
            stack.pop()

        j = stack[-1]

        width = L[i] - L[j] - 1

        wall = prefix[i - 1] - prefix[j]

        x = width * H[i] - wall

        A[i] = A[j] + x

        stack.append(i)

    q = int(next(it))

    out = []

    for _ in range(q):
        k = int(next(it))

        ans = bisect_left(A, k, 1, n + 1) - 1

        out.append(str(ans))

    print('\n'.join(out))
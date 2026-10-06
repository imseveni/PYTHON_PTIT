from collections import deque

results = []
q = deque(['1', '2'])

while len(results) < 1000:
    s = q.popleft()

    if s.count('2') > len(s) // 2:
        results.append(s)

    q.append(s + '0')
    q.append(s + '1')
    q.append(s + '2')


T = int(input())
for _ in range(T):
    n = int(input())

    for i in range(n):
        print(results[i], end = " ")
    print()

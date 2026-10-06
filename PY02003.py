from queue import PriorityQueue
import bisect

INF = 10**18

q = PriorityQueue()
q.put(1)

visited = {1}
results = []

while not q.empty():
    x = q.get()
    if x > INF:
        break
    results.append(x)

    for factor in (2, 3, 5):
        nxt = x * factor
        if nxt not in visited:
            visited.add(nxt)
            q.put(nxt)

T = int(input())
for _ in range(T):
    x = int(input())
    idx = bisect.bisect_left(results, x)

    if(idx < len(results) and results[idx] == x):
        print(idx + 1)
    else:
        print("Not in sequence")
            
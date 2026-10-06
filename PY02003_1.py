from queue import PriorityQueue
import sys

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

def solve(x):
    l, r = 0, len(results) - 1
    while l <= r:
        mid = (l + r) // 2
        
        if results[mid] == x:
            print(mid + 1)
            return
        elif results[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    print("Not in sequence")
    return

input_data = sys.stdin.read().split()
T = int(input_data[0])

queries = [int(x) for x in input_data[1: T + 1]]

for x in queries:
    solve(x)
            